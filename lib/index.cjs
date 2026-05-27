// lib/index.cjs — Dnuzi AI SDK  (CommonJS)
"use strict";

const { DnuziClient } = require("../src/client.js");
const { DnuziStorage } = require("../src/storage.js");

/**
 * DnuziAI — high-level SDK combining the API client + optional DB storage.
 *
 * Quick start:
 *   const { DnuziAI } = require("dnuzi");
 *   const ai = new DnuziAI();
 *   const { result } = await ai.chat("Hello!");
 *   console.log(result);
 *
 * With MongoDB storage:
 *   const ai = new DnuziAI({ userId: "alice" });
 *   await ai.enableStorage();
 *   const { result } = await ai.chat("Hello!");
 */
class DnuziAI {
  constructor(options = {}) {
    this.client  = new DnuziClient(options);
    this.storage = new DnuziStorage(options.userId || "anonymous");
  }

  /** Enable persistent MongoDB storage */
  async enableStorage(userId) {
    await this.storage.connect(userId);
    return this;
  }

  /** Send a message; auto-persists if storage is enabled */
  async chat(message) {
    const response = await this.client.chat(message);
    if (this.storage.enabled) {
      await this.storage.saveTurn({
        conversationId:   response.conversationId,
        userMessage:      message,
        assistantMessage: response.result,
        responseTime:     response.responseTime,
      });
    }
    return response;
  }

  /** Alias */
  async ask(message) { return this.chat(message); }

  /** Start a fresh conversation thread */
  newConversation() { this.client.newConversation(); }

  /** In-memory history for the current session */
  getHistory() { return this.client.getHistory(); }

  /** Persistent history from MongoDB (requires enableStorage) */
  async getPersistentHistory(conversationId) {
    return this.storage.getConversation(conversationId || this.client.conversationId);
  }

  /** List all stored conversation IDs */
  async listConversations() { return this.storage.listConversations(); }

  /** Delete a stored conversation */
  async deleteConversation(id) { return this.storage.deleteConversation(id); }

  /** Get usage stats from MongoDB */
  async getStats() { return this.storage.getStats(); }

  /** Set/get user preferences in MongoDB */
  async setPref(k, v) { return this.storage.setPref(k, v); }
  async getPref(k, def) { return this.storage.getPref(k, def); }

  /** Gracefully close MongoDB connection */
  async close() { await this.storage.disconnect(); }
}

module.exports = { DnuziAI, DnuziClient, DnuziStorage };
