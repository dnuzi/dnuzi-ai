// test/client.test.js
// Unit tests for NiyoXClient — API layer
"use strict";

const https = require("https");
const { NiyoXClient } = require("../src/client.js");

// ── minimal fetch mock ───────────────────────────────────────────────────────
function mockFetch(payload, status = 200) {
  globalThis.fetch = async (url) => ({
    ok: status >= 200 && status < 300,
    status,
    statusText: status === 200 ? "OK" : "Error",
    json: async () => payload,
  });
}

afterEach(() => { delete globalThis.fetch; });

// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
describe("NiyoXClient", () => {

  // ── construction ────────────────────────────────────────────────────────
  describe("construction", () => {
    test("creates with default options", () => {
      const c = new NiyoXClient();
      expect(c.sessionId).toBe("default");
      expect(c.conversationId).toBeNull();
      expect(c.history).toEqual([]);
    });

    test("accepts custom sessionId and conversationId", () => {
      const c = new NiyoXClient({ sessionId: "s1", conversationId: "cid" });
      expect(c.sessionId).toBe("s1");
      expect(c.conversationId).toBe("cid");
    });
  });

  // ── successful chat ──────────────────────────────────────────────────────
  describe("chat()", () => {
    const MOCK_RESPONSE = {
      success: true,
      result: "Hello from NiyoX AI!",
      conversationId: "conv-abc-123",
      sessionId: "default",
      responseTime: 512,
      attempts: 1,
    };

    beforeEach(() => mockFetch(MOCK_RESPONSE));

    test("returns result string", async () => {
      const c   = new NiyoXClient();
      const res = await c.chat("Hello!");
      expect(res.result).toBe("Hello from NiyoX AI!");
    });

    test("returns correct metadata fields", async () => {
      const c   = new NiyoXClient();
      const res = await c.chat("Hi");
      expect(res.conversationId).toBe("conv-abc-123");
      expect(res.responseTime).toBe(512);
      expect(res.attempts).toBe(1);
    });

    test("persists conversationId after first response", async () => {
      const c = new NiyoXClient();
      expect(c.conversationId).toBeNull();
      await c.chat("Hi");
      expect(c.conversationId).toBe("conv-abc-123");
    });

    test("appends two entries to history per turn", async () => {
      const c = new NiyoXClient();
      await c.chat("test message");
      const hist = c.getHistory();
      expect(hist).toHaveLength(2);
      expect(hist[0].role).toBe("user");
      expect(hist[0].content).toBe("test message");
      expect(hist[1].role).toBe("assistant");
      expect(hist[1].content).toBe("Hello from NiyoX AI!");
    });

    test("accumulates history across multiple turns", async () => {
      const c = new NiyoXClient();
      await c.chat("message one");
      await c.chat("message two");
      expect(c.getHistory()).toHaveLength(4);
    });

    test("ask() is an alias for chat()", async () => {
      const c   = new NiyoXClient();
      const res = await c.ask("Hello");
      expect(res.result).toBe("Hello from NiyoX AI!");
    });
  });

  // ── error handling ───────────────────────────────────────────────────────
  describe("error handling", () => {
    test("throws on non-OK HTTP status", async () => {
      mockFetch({ success: false }, 500);
      const c = new NiyoXClient();
      await expect(c.chat("test")).rejects.toThrow("HTTP 500");
    });

    test("throws when success is false", async () => {
      mockFetch({ success: false, result: "nope" });
      const c = new NiyoXClient();
      await expect(c.chat("test")).rejects.toThrow("success=false");
    });
  });

  // ── newConversation ──────────────────────────────────────────────────────
  describe("newConversation()", () => {
    test("resets conversationId and history", async () => {
      mockFetch({
        success: true, result: "Hi", conversationId: "cid-1",
        sessionId: "default", responseTime: 100, attempts: 1,
      });
      const c = new NiyoXClient();
      await c.chat("Hello");
      expect(c.conversationId).toBe("cid-1");
      expect(c.history.length).toBeGreaterThan(0);

      c.newConversation();
      expect(c.conversationId).toBeNull();
      expect(c.history).toEqual([]);
    });
  });

  // ── getHistory ───────────────────────────────────────────────────────────
  describe("getHistory()", () => {
    test("returns a copy, not the original array", async () => {
      mockFetch({
        success: true, result: "OK", conversationId: "x",
        sessionId: "default", responseTime: 50, attempts: 1,
      });
      const c = new NiyoXClient();
      await c.chat("test");
      const h1 = c.getHistory();
      h1.push({ injected: true });
      expect(c.getHistory()).toHaveLength(2);   // still original length
    });
  });
});
