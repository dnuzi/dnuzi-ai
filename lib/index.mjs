// lib/index.mjs — ESM re-export wrapper
import cjs from "../lib/index.cjs";
export const { DAI, DAIClient, DAIStorage } = cjs;
export default cjs.DAI;
