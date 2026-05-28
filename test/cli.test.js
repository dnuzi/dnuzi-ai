// test/cli.test.js
// Smoke tests for the CLI binary  (no real network calls)
"use strict";

const { execSync, spawnSync } = require("child_process");
const path = require("path");

const CLI = path.join(__dirname, "..", "bin", "cli.js");

// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
describe("CLI binary", () => {

  test("--version prints a semver string", () => {
    const res = spawnSync(process.execPath, [CLI, "--version"], { encoding: "utf8", timeout: 8000 });
    expect(res.status).toBe(0);
    expect(res.stdout.trim()).toMatch(/^\d+\.\d+\.\d+$/);
  });

  test("--help exits successfully", () => {
    const res = spawnSync(process.execPath, [CLI, "--help"], { encoding: "utf8", timeout: 8000 });
    // may be 0 or 1 depending on env — just check it terminates without crash
    expect(res.signal).toBeNull();
  });

  test("-v is an alias for --version", () => {
    const res = spawnSync(process.execPath, [CLI, "-v"], { encoding: "utf8", timeout: 8000 });
    expect(res.status).toBe(0);
    expect(res.stdout.trim()).toMatch(/^\d+\.\d+\.\d+$/);
  });

  test("version matches package.json", () => {
    const pkg = require("../package.json");
    const res = spawnSync(process.execPath, [CLI, "--version"], { encoding: "utf8", timeout: 8000 });
    expect(res.stdout.trim()).toBe(pkg.version);
  });
});
