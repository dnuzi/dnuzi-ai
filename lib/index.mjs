// lib/index.mjs — ESM re-export wrapper
import cjs from "../lib/index.cjs";
export const { HiazAI, HiazClient, HiazStorage } = cjs;
export default cjs.HiazAI;
