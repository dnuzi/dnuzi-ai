"""
dnuzi/python/dnuzi.py
Dnuzi AI — Python SDK
Powered by DanuZz (@dnuzi)

Install deps:  pip install requests pymongo
"""

import time
import uuid
from typing import Optional
from dataclasses import dataclass, field
from datetime import datetime

try:
    import requests
except ImportError:
    raise ImportError("Please install requests:  pip install requests")


BASE_URL = "https://ai.dnuz.top/api/ai"


@dataclass
class ChatResponse:
    result: str
    conversation_id: str
    session_id: str
    response_time: int
    attempts: int


class DnuziClient:
    """
    Core Dnuzi AI client.

    Usage:
        from dnuzi import DnuziClient
        client = DnuziClient()
        resp = client.chat("Hello!")
        print(resp.result)
    """

    def __init__(
        self,
        session_id: str = "default",
        conversation_id: Optional[str] = None,
        timeout: int = 30,
    ):
        self.session_id      = session_id
        self.conversation_id = conversation_id
        self.timeout         = timeout
        self.history: list   = []

    def chat(self, message: str) -> ChatResponse:
        params = {"q": message}
        if self.conversation_id:
            params["conversationId"] = self.conversation_id
        if self.session_id != "default":
            params["sessionId"] = self.session_id

        resp = requests.get(BASE_URL, params=params, timeout=self.timeout)
        resp.raise_for_status()
        data = resp.json()

        if not data.get("success"):
            raise RuntimeError("API returned success=false")

        if data.get("conversationId"):
            self.conversation_id = data["conversationId"]

        ts = datetime.now()
        self.history.append({"role": "user",      "content": message,        "timestamp": ts})
        self.history.append({"role": "assistant", "content": data["result"], "timestamp": ts,
                              "response_time": data.get("responseTime")})

        return ChatResponse(
            result          = data["result"],
            conversation_id = data.get("conversationId", ""),
            session_id      = data.get("sessionId", ""),
            response_time   = data.get("responseTime", 0),
            attempts        = data.get("attempts", 1),
        )

    # Alias
    def ask(self, message: str) -> ChatResponse:
        return self.chat(message)

    def new_conversation(self):
        self.conversation_id = None
        self.history.clear()

    def get_history(self) -> list:
        return list(self.history)


class DnuziStorage:
    """
    Optional MongoDB storage layer.

    Usage:
        from dnuzi import DnuziStorage
        storage = DnuziStorage(user_id="alice")
        storage.connect()
        storage.save_turn(conversation_id="abc", user_message="Hi", assistant_message="Hello!", response_time=500)
    """

    MONGO_URI = "mongodb+srv://danuz_movanest:danuz_movanest@cluster0.3pm9uqz.mongodb.net/"
    DB_NAME   = "dnuzi_npm"

    def __init__(self, user_id: str = "anonymous"):
        self.user_id = user_id
        self.enabled = False
        self._db     = None

    def connect(self, user_id: Optional[str] = None) -> "DnuziStorage":
        try:
            from pymongo import MongoClient
        except ImportError:
            raise ImportError("Please install pymongo:  pip install pymongo[srv]")

        if user_id:
            self.user_id = user_id

        client   = MongoClient(self.MONGO_URI, serverSelectionTimeoutMS=5000)
        client.admin.command("ping")   # verify connection
        self._db     = client[self.DB_NAME]
        self.enabled = True
        return self

    def save_turn(self, *, conversation_id: str, user_message: str, assistant_message: str, response_time: int = 0):
        if not self.enabled:
            return
        docs = [
            {"userId": self.user_id, "conversationId": conversation_id, "role": "user",
             "content": user_message, "responseTime": None, "createdAt": datetime.utcnow()},
            {"userId": self.user_id, "conversationId": conversation_id, "role": "assistant",
             "content": assistant_message, "responseTime": response_time, "createdAt": datetime.utcnow()},
        ]
        self._db["messages"].insert_many(docs)

    def get_conversation(self, conversation_id: str) -> list:
        if not self.enabled:
            return []
        return list(self._db["messages"].find(
            {"conversationId": conversation_id, "userId": self.user_id},
            sort=[("createdAt", 1)]
        ))

    def list_conversations(self) -> list:
        if not self.enabled:
            return []
        return self._db["messages"].distinct("conversationId", {"userId": self.user_id})

    def get_stats(self) -> dict:
        if not self.enabled:
            return {}
        coll  = self._db["messages"]
        total = coll.count_documents({"userId": self.user_id})
        convs = coll.distinct("conversationId", {"userId": self.user_id})
        avg   = list(coll.aggregate([
            {"$match": {"userId": self.user_id, "role": "assistant", "responseTime": {"$ne": None}}},
            {"$group": {"_id": None, "avg": {"$avg": "$responseTime"}}},
        ]))
        return {
            "total_messages":       total,
            "total_conversations":  len(convs),
            "avg_response_time_ms": round(avg[0]["avg"]) if avg else "N/A",
        }


class DnuziAI:
    """
    High-level Dnuzi AI client with optional MongoDB storage.

    Usage:
        from dnuzi import DnuziAI
        ai = DnuziAI()
        resp = ai.chat("Tell me a joke")
        print(resp.result)

        # With storage:
        ai = DnuziAI(user_id="alice")
        ai.enable_storage()
        resp = ai.chat("Hello!")
    """

    def __init__(self, *, user_id: str = "anonymous", session_id: str = "default"):
        self.client  = DnuziClient(session_id=session_id)
        self.storage = DnuziStorage(user_id=user_id)

    def enable_storage(self, user_id: Optional[str] = None) -> "DnuziAI":
        self.storage.connect(user_id)
        return self

    def chat(self, message: str) -> ChatResponse:
        response = self.client.chat(message)
        if self.storage.enabled:
            self.storage.save_turn(
                conversation_id   = response.conversation_id,
                user_message      = message,
                assistant_message = response.result,
                response_time     = response.response_time,
            )
        return response

    def ask(self, message: str) -> ChatResponse:
        return self.chat(message)

    def new_conversation(self):
        self.client.new_conversation()

    def get_history(self) -> list:
        return self.client.get_history()

    def list_conversations(self) -> list:
        return self.storage.list_conversations()

    def get_stats(self) -> dict:
        return self.storage.get_stats()


# ─── CLI (python -m dnuzi) ──────────────────────────────────────────────────
if __name__ == "__main__":
    import sys

    print("\n  ██████╗ ███╗   ██╗██╗   ██╗███████╗██╗")
    print("  ██╔══██╗████╗  ██║██║   ██║╚══███╔╝██║")
    print("  ██║  ██║██╔██╗ ██║██║   ██║  ███╔╝ ██║")
    print("  ██║  ██║██║╚██╗██║██║   ██║ ███╔╝  ██║")
    print("  ██████╔╝██║ ╚████║╚██████╔╝███████╗██║")
    print("  ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝ ╚══════╝╚═╝")
    print("  Powered by DanuZz  •  @dnuzi\n")

    if len(sys.argv) > 1:
        q   = " ".join(sys.argv[1:])
        ai  = DnuziAI()
        r   = ai.chat(q)
        print(f"  AI: {r.result}\n  ⚡ {r.response_time}ms\n")
    else:
        ai  = DnuziAI()
        print("  Type your message. Ctrl+C to quit.\n")
        while True:
            try:
                msg = input("  ❯ ").strip()
                if not msg:
                    continue
                if msg in ("/exit", "/quit"):
                    break
                r = ai.chat(msg)
                print(f"\n  AI: {r.result}\n  ⚡ {r.response_time}ms\n")
            except KeyboardInterrupt:
                print("\n  Bye! ✨\n")
                break
