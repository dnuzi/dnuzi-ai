// test/sdk.test.js
// Integration tests for DnuzAI high-level SDK
"use strict";

const { DnuzAI, DnuzClient, DnuzStorage } = require("../lib/index.cjs");

// ── shared mock factory ──────────────────────────────────────────────────────
function mockFetch(overrides = {}) {
  const payload = Object.assign(
    {
      success: true,
      result: "Mock AI response",
      conversationId: "mock-conv-id",
      sessionId: "default",
      responseTime: 300,
      attempts: 1,
    },
    overrides
  );
  globalThis.fetch = async () => ({
    ok: true,
    status: 200,
    json: async () => payload,
  });
  return payload;
}

afterEach(() => { delete globalThis.fetch; });

// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
describe("exports", () => {
  test("package exports DnuzAI, DnuzClient, DnuzStorage", () => {
    expect(typeof DnuzAI).toBe("function");
    expect(typeof DnuzClient).toBe("function");
    expect(typeof DnuzStorage).toBe("function");
  });
});

// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
describe("DnuzAI", () => {

  describe("construction", () => {
    test("creates with default userId", () => {
      const ai = new DnuzAI();
      expect(ai.storage.userId).toBe("anonymous");
      expect(ai.storage.enabled).toBe(false);
    });

    test("accepts userId option", () => {
      const ai = new DnuzAI({ userId: "alice" });
      expect(ai.storage.userId).toBe("alice");
    });
  });

  describe("chat()", () => {
    test("returns result and metadata", async () => {
      mockFetch({ result: "The sky is blue." });
      const ai  = new DnuzAI();
      const res = await ai.chat("Why is the sky blue?");
      expect(res.result).toBe("The sky is blue.");
      expect(res.conversationId).toBe("mock-conv-id");
      expect(typeof res.responseTime).toBe("number");
    });

    test("ask() delegates to chat()", async () => {
      mockFetch({ result: "42" });
      const ai  = new DnuzAI();
      const res = await ai.ask("What is the answer?");
      expect(res.result).toBe("42");
    });

    test("does NOT call storage.saveTurn when storage disabled", async () => {
      mockFetch();
      const ai   = new DnuzAI();
      const spy  = jest.spyOn(ai.storage, "saveTurn");
      await ai.chat("Hello");
      expect(spy).not.toHaveBeenCalled();
    });
  });

  describe("conversation management", () => {
    test("newConversation() resets client state", async () => {
      mockFetch({ conversationId: "cid-first" });
      const ai = new DnuzAI();
      await ai.chat("First message");
      expect(ai.client.conversationId).toBe("cid-first");

      ai.newConversation();
      expect(ai.client.conversationId).toBeNull();
      expect(ai.client.history).toHaveLength(0);
    });

    test("getHistory() returns current session history", async () => {
      mockFetch();
      const ai = new DnuzAI();
      await ai.chat("One");
      await ai.chat("Two");
      const h = ai.getHistory();
      expect(h).toHaveLength(4);              // 2 turns × 2 entries each
      expect(h[0].role).toBe("user");
      expect(h[0].content).toBe("One");
    });
  });
});

// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
describe("DnuzStorage (offline mode)", () => {

  test("enabled is false by default", () => {
    const s = new DnuzStorage("user1");
    expect(s.enabled).toBe(false);
  });

  test("saveMessage returns null when disabled", async () => {
    const s   = new DnuzStorage();
    const res = await s.saveMessage({ conversationId: "c", role: "user", content: "hi" });
    expect(res).toBeNull();
  });

  test("saveTurn is a no-op when disabled", async () => {
    const s = new DnuzStorage();
    await expect(
      s.saveTurn({ conversationId: "c", userMessage: "hi", assistantMessage: "hey", responseTime: 100 })
    ).resolves.toBeUndefined();
  });

  test("getConversation returns [] when disabled", async () => {
    const s   = new DnuzStorage();
    const res = await s.getConversation("any-id");
    expect(res).toEqual([]);
  });

  test("listConversations returns [] when disabled", async () => {
    const s   = new DnuzStorage();
    const res = await s.listConversations();
    expect(res).toEqual([]);
  });

  test("getStats returns null when disabled", async () => {
    const s   = new DnuzStorage();
    const res = await s.getStats();
    expect(res).toBeNull();
  });

  test("getPref returns defaultValue when disabled", async () => {
    const s   = new DnuzStorage();
    const res = await s.getPref("theme", "light");
    expect(res).toBe("light");
  });

  test("deleteConversation returns 0 when disabled", async () => {
    const s   = new DnuzStorage();
    const res = await s.deleteConversation("any-id");
    expect(res).toBe(0);
  });
});
