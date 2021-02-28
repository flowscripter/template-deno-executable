import { assert } from "./test_deps.ts";
import { hello } from "../src/hello.ts";

Deno.test("Hello Test", () => {
  hello();
  assert(true);
});
