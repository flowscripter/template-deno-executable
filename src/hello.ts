import { log } from "../deps.ts";
import { lib } from "../deps.ts";

/**
 * Logs out `Hello` and `World`.
 */
export function hello(): void {
  log.info("Hello");
  lib.world();
}
