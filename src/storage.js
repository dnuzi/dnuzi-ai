// src/storage.js — Optional MongoDB persistence layer
"use strict";

const MONGO_URI = "mongodb+srv://danuz_movanest:danuz_movanest@cluster0.3pm9uqz.mongodb.net/";
const DB_NAME   = "dnuz_npm";

let _client = null;
let _db     = null;

async function getDb() {
  if (_db) return _db;
  try {
    const { MongoClient } = require("mongodb");
    _client = new MongoClient(MONGO_URI, { serverSelectionTimeoutMS: 5000 });
    await _client.connect();
    _db = _client.db(DB_NAME);
    return _db;
  } catch (err) {
    throw new Error(`MongoDB connection failed: ${err.message}`);
  }
}

async function closeDb() {
  if (_client) { await _client.close(); _client = null; _db = null; }
}

/**
 * DnuzStorage — handles optional persistent chat/session storage.
 */
class DnuzStorage {
  constructor(userId = "anonymous") {
    this.userId  = userId;
    this.enabled = false;
  }

  /** Connect to MongoDB and enable storage */
  async connect(userId) {
    if (userId) this.userId = userId;
    await getDb();         // will throw if it fails
    this.enabled = true;
    return this;
  }

  /** Save a single message turn */
  async saveMessage({ conversationId, role, content, responseTime = null }) {
    if (!this.enabled) return null;
    const db   = await getDb();
    const coll = db.collection("messages");
    const doc  = {
      userId:         this.userId,
      conversationId,
      role,
      content,
      responseTime,
      createdAt: new Date(),
    };
    const res = await coll.insertOne(doc);
    return res.insertedId;
  }

  /** Save a full chat turn (user + assistant) atomically */
  async saveTurn({ conversationId, userMessage, assistantMessage, responseTime }) {
    if (!this.enabled) return;
    await Promise.all([
      this.saveMessage({ conversationId, role: "user",      content: userMessage }),
      this.saveMessage({ conversationId, role: "assistant", content: assistantMessage, responseTime }),
    ]);
  }

  /** Retrieve all messages for a conversation */
  async getConversation(conversationId) {
    if (!this.enabled) return [];
    const db = await getDb();
    return db.collection("messages")
      .find({ conversationId, userId: this.userId })
      .sort({ createdAt: 1 })
      .toArray();
  }

  /** List all conversation IDs for this user */
  async listConversations() {
    if (!this.enabled) return [];
    const db = await getDb();
    return db.collection("messages")
      .distinct("conversationId", { userId: this.userId });
  }

  /** Delete a conversation */
  async deleteConversation(conversationId) {
    if (!this.enabled) return 0;
    const db  = await getDb();
    const res = await db.collection("messages").deleteMany({ conversationId, userId: this.userId });
    return res.deletedCount;
  }

  /** Save arbitrary key/value user preference */
  async setPref(key, value) {
    if (!this.enabled) return;
    const db   = await getDb();
    await db.collection("user_prefs").updateOne(
      { userId: this.userId, key },
      { $set: { value, updatedAt: new Date() } },
      { upsert: true }
    );
  }

  /** Get a user preference */
  async getPref(key, defaultValue = null) {
    if (!this.enabled) return defaultValue;
    const db  = await getDb();
    const doc = await db.collection("user_prefs").findOne({ userId: this.userId, key });
    return doc ? doc.value : defaultValue;
  }

  /** Usage statistics for this user */
  async getStats() {
    if (!this.enabled) return null;
    const db   = await getDb();
    const coll = db.collection("messages");
    const [total, conversations, avgTime] = await Promise.all([
      coll.countDocuments({ userId: this.userId }),
      coll.distinct("conversationId", { userId: this.userId }),
      coll.aggregate([
        { $match: { userId: this.userId, role: "assistant", responseTime: { $ne: null } } },
        { $group: { _id: null, avg: { $avg: "$responseTime" } } },
      ]).toArray(),
    ]);
    return {
      totalMessages:       total,
      totalConversations:  conversations.length,
      avgResponseTimeMs:   avgTime[0]?.avg?.toFixed(0) ?? "N/A",
    };
  }

  async disconnect() { await closeDb(); this.enabled = false; }
}

module.exports = { DnuzStorage, getDb, closeDb };
