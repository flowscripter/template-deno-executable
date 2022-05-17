import { log } from "../deps.ts";
import { denoLib, rustLib } from "../deps.ts";

/**
 * Logs out some greetings.
 */
export function hello(): void {
  log.info("Hello");
  denoLib.world();
  log.info("Hello");
  rustLib.world();
}
