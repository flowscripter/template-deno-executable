import { log } from "../deps.ts";
import { denoLib } from "../deps.ts";

/**
 * Logs out some greetings.
 */
export function hello(): void {
  log.info("Hello");
  denoLib.world();
}
