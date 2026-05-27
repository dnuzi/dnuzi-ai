// lib/index.mjs — ESM re-export wrapper
import cjs from "../lib/index.cjs";
export const { DnuziAI, DnuziClient, DnuziStorage } = cjs;
export default cjs.DnuziAI;
