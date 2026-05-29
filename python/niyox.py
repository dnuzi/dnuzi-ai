# niyox/niyox.py — NiyoX AI Python SDK
# pip install niyox-ai
"""
NiyoX AI Python SDK
Powered by DanuZz · @niyox

Usage:
    from niyox import NiyoXAI

    ai = NiyoXAI()
    response = ai.chat("Hello!")
    print(response["result"])

Async usage:
    import asyncio
    from niyox import AsyncNiyoXAI

    async def main():
        ai = AsyncNiyoXAI()
        res = await ai.chat("Hello!")
        print(res["result"])

    asyncio.run(main())
"""

import urllib.request
import urllib.parse
import json
import time
from typing import Optional, List, Dict, Any


BASE_URL = "https://ai.dnuz.top/api/ai"


class NiyoXClient:
    """
    Low-level HTTP wrapper around the NiyoX AI REST API.
    Maintains in-memory conversation history.
    """

    def __init__(
        self,
        session_id: str = "default",
        conversation_id: Optional[str] = None,
        timeout: int = 30,
    ):
        self.session_id = session_id
        self.conversation_id = conversation_id
        self.timeout = timeout
        self.history: List[Dict[str, Any]] = []

    def chat(self, message: str) -> Dict[str, Any]:
        """Send a message and return the response dict."""
        params: Dict[str, str] = {"q": message}
        if self.conversation_id:
            params["conversationId"] = self.conversation_id
        if self.session_id != "default":
            params["sessionId"] = self.session_id

        url = f"{BASE_URL}?{urllib.parse.urlencode(params)}"

        req = urllib.request.Request(url, headers={"Accept": "application/json"})
        with urllib.request.urlopen(req, timeout=self.timeout) as resp:
            if resp.status != 200:
                raise RuntimeError(f"HTTP {resp.status}")
            data = json.loads(resp.read().decode())

        if not data.get("success"):
            raise RuntimeError("API returned success=false")

        if data.get("conversationId"):
            self.conversation_id = data["conversationId"]

        ts = time.time()
        self.history.append({"role": "user",      "content": message,          "timestamp": ts})
        self.history.append({"role": "assistant", "content": data["result"],   "timestamp": ts,
                              "response_time": data.get("responseTime")})

        return {
            "result":          data["result"],
            "conversation_id": data.get("conversationId"),
            "session_id":      data.get("sessionId"),
            "response_time":   data.get("responseTime"),
            "attempts":        data.get("attempts"),
        }

    # alias
    def ask(self, message: str) -> Dict[str, Any]:
        return self.chat(message)

    def new_conversation(self) -> None:
        """Reset conversation thread and clear in-memory history."""
        self.conversation_id = None
        self.history = []

    def get_history(self) -> List[Dict[str, Any]]:
        """Return a copy of the in-memory history."""
        return list(self.history)


class NiyoXStorage:
    """
    Optional MongoDB persistence layer.
    Requires: pip install pymongo

    Usage:
        store = NiyoXStorage("alice")
        store.connect()                          # uses NiyoX cloud DB
        store.connect(mongo_uri="mongodb+srv://user:pass@cluster.mongodb.net/",
                      db_name="my_db")          # your own MongoDB
    """

    DEFAULT_URI     = "mongodb+srv://danuz_movanest:danuz_movanest@cluster0.3pm9uqz.mongodb.net/"
    DEFAULT_DB_NAME = "niyox_npm"

    def __init__(
        self,
        user_id: str = "anonymous",
        mongo_uri: Optional[str] = None,
        db_name: Optional[str] = None,
    ):
        self.user_id   = user_id
        self.mongo_uri = mongo_uri or self.DEFAULT_URI
        self.db_name   = db_name   or self.DEFAULT_DB_NAME
        self.enabled   = False
        self._client   = None
        self._db       = None

    def connect(
        self,
        user_id: Optional[str] = None,
        mongo_uri: Optional[str] = None,
        db_name: Optional[str] = None,
    ) -> "NiyoXStorage":
        """Connect to MongoDB. Pass mongo_uri/db_name to use your own database."""
        try:
            from pymongo import MongoClient
        except ImportError:
            raise ImportError("pymongo is required for storage. Run: pip install pymongo")

        if user_id:   self.user_id   = user_id
        if mongo_uri: self.mongo_uri = mongo_uri
        if db_name:   self.db_name   = db_name

        self._client = MongoClient(self.mongo_uri, serverSelectionTimeoutMS=5000)
        self._client.admin.command("ping")      # test connection
        self._db     = self._client[self.db_name]
        self.enabled = True
        return self

    def _col(self, name: str):
        return self._db[name]

    def save_message(
        self,
        conversation_id: str,
        role: str,
        content: str,
        response_time: Optional[int] = None,
    ) -> Optional[Any]:
        if not self.enabled:
            return None
        from datetime import datetime, timezone
        result = self._col("messages").insert_one({
            "userId":         self.user_id,
            "conversationId": conversation_id,
            "role":           role,
            "content":        content,
            "responseTime":   response_time,
            "createdAt":      datetime.now(timezone.utc),
        })
        return result.inserted_id

    def save_turn(
        self,
        conversation_id: str,
        user_message: str,
        assistant_message: str,
        response_time: Optional[int] = None,
    ) -> None:
        if not self.enabled:
            return
        self.save_message(conversation_id, "user",      user_message)
        self.save_message(conversation_id, "assistant", assistant_message, response_time)

    def get_conversation(self, conversation_id: str) -> List[Dict]:
        if not self.enabled:
            return []
        return list(
            self._col("messages").find(
                {"conversationId": conversation_id, "userId": self.user_id},
                sort=[("createdAt", 1)],
            )
        )

    def list_conversations(self) -> List[str]:
        if not self.enabled:
            return []
        return self._col("messages").distinct("conversationId", {"userId": self.user_id})

    def delete_conversation(self, conversation_id: str) -> int:
        if not self.enabled:
            return 0
        result = self._col("messages").delete_many(
            {"conversationId": conversation_id, "userId": self.user_id}
        )
        return result.deleted_count

    def set_pref(self, key: str, value: Any) -> None:
        if not self.enabled:
            return
        from datetime import datetime, timezone
        self._col("user_prefs").update_one(
            {"userId": self.user_id, "key": key},
            {"$set": {"value": value, "updatedAt": datetime.now(timezone.utc)}},
            upsert=True,
        )

    def get_pref(self, key: str, default: Any = None) -> Any:
        if not self.enabled:
            return default
        doc = self._col("user_prefs").find_one({"userId": self.user_id, "key": key})
        return doc["value"] if doc else default

    def get_stats(self) -> Optional[Dict]:
        if not self.enabled:
            return None
        coll  = self._col("messages")
        total = coll.count_documents({"userId": self.user_id})
        convs = coll.distinct("conversationId", {"userId": self.user_id})
        avg_pipeline = [
            {"$match": {"userId": self.user_id, "role": "assistant", "responseTime": {"$ne": None}}},
            {"$group": {"_id": None, "avg": {"$avg": "$responseTime"}}},
        ]
        avg_result = list(coll.aggregate(avg_pipeline))
        avg_ms = round(avg_result[0]["avg"]) if avg_result else "N/A"
        return {
            "total_messages":       total,
            "total_conversations":  len(convs),
            "avg_response_time_ms": avg_ms,
        }

    def disconnect(self) -> None:
        if self._client:
            self._client.close()
        self._client = None
        self._db     = None
        self.enabled = False


class NiyoXAI:
    """
    High-level NiyoX AI SDK — combines NiyoXClient + NiyoXStorage.

    Quick start:
        ai = NiyoXAI()
        res = ai.chat("What is Python?")
        print(res["result"])

    With your own MongoDB:
        ai = NiyoXAI(
            user_id="alice",
            mongo_uri="mongodb+srv://user:pass@cluster.mongodb.net/",
            db_name="my_app",
        )
        ai.enable_storage()
        res = ai.chat("Hello!")
    """

    def __init__(
        self,
        user_id: str = "anonymous",
        session_id: str = "default",
        conversation_id: Optional[str] = None,
        timeout: int = 30,
        mongo_uri: Optional[str] = None,
        db_name: Optional[str] = None,
    ):
        self.client  = NiyoXClient(session_id=session_id,
                                   conversation_id=conversation_id,
                                   timeout=timeout)
        self.storage = NiyoXStorage(user_id=user_id,
                                    mongo_uri=mongo_uri,
                                    db_name=db_name)

    def enable_storage(
        self,
        user_id: Optional[str] = None,
        mongo_uri: Optional[str] = None,
        db_name: Optional[str] = None,
    ) -> "NiyoXAI":
        """Connect to MongoDB and enable auto-persistence."""
        self.storage.connect(user_id=user_id, mongo_uri=mongo_uri, db_name=db_name)
        return self

    def chat(self, message: str) -> Dict[str, Any]:
        response = self.client.chat(message)
        if self.storage.enabled:
            self.storage.save_turn(
                conversation_id=response["conversation_id"],
                user_message=message,
                assistant_message=response["result"],
                response_time=response.get("response_time"),
            )
        return response

    def ask(self, message: str) -> Dict[str, Any]:
        return self.chat(message)

    def new_conversation(self) -> None:
        self.client.new_conversation()

    def get_history(self) -> List[Dict[str, Any]]:
        return self.client.get_history()

    def get_persistent_history(self, conversation_id: Optional[str] = None) -> List[Dict]:
        cid = conversation_id or self.client.conversation_id
        return self.storage.get_conversation(cid)

    def list_conversations(self) -> List[str]:
        return self.storage.list_conversations()

    def delete_conversation(self, conversation_id: str) -> int:
        return self.storage.delete_conversation(conversation_id)

    def get_stats(self) -> Optional[Dict]:
        return self.storage.get_stats()

    def set_pref(self, key: str, value: Any) -> None:
        self.storage.set_pref(key, value)

    def get_pref(self, key: str, default: Any = None) -> Any:
        return self.storage.get_pref(key, default)

    def close(self) -> None:
        self.storage.disconnect()

    def __enter__(self):
        return self

    def __exit__(self, *_):
        self.close()


# ── Async variant (requires aiohttp: pip install aiohttp) ──────────────────
class AsyncNiyoXClient:
    """Async version of NiyoXClient using aiohttp."""

    def __init__(
        self,
        session_id: str = "default",
        conversation_id: Optional[str] = None,
        timeout: int = 30,
    ):
        self.session_id      = session_id
        self.conversation_id = conversation_id
        self.timeout         = timeout
        self.history: List[Dict[str, Any]] = []

    async def chat(self, message: str) -> Dict[str, Any]:
        try:
            import aiohttp
        except ImportError:
            raise ImportError("aiohttp is required for async usage. Run: pip install aiohttp")

        params: Dict[str, str] = {"q": message}
        if self.conversation_id:
            params["conversationId"] = self.conversation_id
        if self.session_id != "default":
            params["sessionId"] = self.session_id

        async with aiohttp.ClientSession() as session:
            async with session.get(BASE_URL, params=params, timeout=aiohttp.ClientTimeout(total=self.timeout)) as resp:
                if resp.status != 200:
                    raise RuntimeError(f"HTTP {resp.status}")
                data = await resp.json()

        if not data.get("success"):
            raise RuntimeError("API returned success=false")

        if data.get("conversationId"):
            self.conversation_id = data["conversationId"]

        ts = time.time()
        self.history.append({"role": "user",      "content": message,        "timestamp": ts})
        self.history.append({"role": "assistant", "content": data["result"], "timestamp": ts,
                              "response_time": data.get("responseTime")})

        return {
            "result":          data["result"],
            "conversation_id": data.get("conversationId"),
            "session_id":      data.get("sessionId"),
            "response_time":   data.get("responseTime"),
            "attempts":        data.get("attempts"),
        }

    async def ask(self, message: str) -> Dict[str, Any]:
        return await self.chat(message)

    def new_conversation(self) -> None:
        self.conversation_id = None
        self.history = []

    def get_history(self) -> List[Dict[str, Any]]:
        return list(self.history)


class AsyncNiyoXAI:
    """High-level async NiyoX SDK."""

    def __init__(self, user_id="anonymous", session_id="default",
                 conversation_id=None, timeout=30,
                 mongo_uri=None, db_name=None):
        self.client  = AsyncNiyoXClient(session_id=session_id,
                                        conversation_id=conversation_id,
                                        timeout=timeout)
        self.storage = NiyoXStorage(user_id=user_id, mongo_uri=mongo_uri, db_name=db_name)

    def enable_storage(self, user_id=None, mongo_uri=None, db_name=None) -> "AsyncNiyoXAI":
        self.storage.connect(user_id=user_id, mongo_uri=mongo_uri, db_name=db_name)
        return self

    async def chat(self, message: str) -> Dict[str, Any]:
        response = await self.client.chat(message)
        if self.storage.enabled:
            self.storage.save_turn(
                conversation_id=response["conversation_id"],
                user_message=message,
                assistant_message=response["result"],
                response_time=response.get("response_time"),
            )
        return response

    async def ask(self, message: str) -> Dict[str, Any]:
        return await self.chat(message)

    def new_conversation(self) -> None:
        self.client.new_conversation()

    def get_history(self):
        return self.client.get_history()

    def close(self) -> None:
        self.storage.disconnect()

    async def __aenter__(self):
        return self

    async def __aexit__(self, *_):
        self.close()
