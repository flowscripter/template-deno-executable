# template-deno-executable

[![version](https://img.shields.io/github/v/release/flowscripter/template-deno-executable?sort=semver)](https://github.com/flowscripter/template-deno-executable/releases)
[![build](https://img.shields.io/github/workflow/status/flowscripter/template-deno-executable/release-deno-executable)](https://github.com/flowscripter/template-deno-executable/actions/workflows/release-deno-executable.yml)
[![coverage](https://codecov.io/gh/flowscripter/template-deno-executable/branch/main/graph/badge.svg?token=EMFT2938ZF)](https://codecov.io/gh/flowscripter/template-deno-executable)
[![dependencies](https://img.shields.io/endpoint?url=https%3A%2F%2Fdeno-visualizer.danopia.net%2Fshields%2Fupdates%2Fhttps%2Fraw.githubusercontent.com%2Fflowscripter%2Ftemplate-deno-executable%2Fmain%2Fmod.ts)](https://github.com/flowscripter/template-deno-executable/blob/main/deps.ts)
[![deno doc](https://doc.deno.land/badge.svg)](https://doc.deno.land/https/raw.githubusercontent.com/flowscripter/template-deno-executable/main/mod.ts)
[![license: MIT](https://img.shields.io/github/license/flowscripter/template-deno-executable)](https://github.com/flowscripter/template-deno-executable/blob/main/LICENSE)

> Project template for a Deno executable.

## Project Template Usage

1. Use as a
   [template](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/creating-a-repository-from-a-template)
   to create a new repository.
2. Update links and references in `README.md`.

## Binary Executable Usage

Download and extract zip from: https://github.com/flowscripter/template-deno-executable/releases

Run the executable: `./template-deno-executable`

## Development

Run: `deno run --unstable --allow-env --allow-read --allow-write --allow-ffi --allow-net mod.ts`

Test: `deno test -A --unstable`

Lint: `deno fmt mod.ts deps.ts src/ tests/`

Compile: `deno compile --unstable --allow-env --allow-read --allow-write --allow-ffi --allow-net mod.ts`

## Functional Tests

Refer to [functional_tests/README.md](functional_tests/README.md)

## Documentation

### Overview

PNG image generated from `images/uml_diagram.mermaid`:

![UML Diagram](https://raw.githubusercontent.com/flowscripter/template-deno-executable/main/images/uml_diagram.png "UML Diagram")

### API

Link to auto-generated API docs for the library:

[API Documentation](https://doc.deno.land/https/raw.githubusercontent.com/flowscripter/template-deno-executable/main/mod.ts)

## License

MIT © Flowscripter
