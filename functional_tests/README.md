## Executable Functional Tests

#### Setup

Ensure the executable is built:

    deno compile --lite --unstable --output /tmp/template-deno-executable ../mod.ts

Install requirements:

    pip3 install -r pip-requirements.txt

#### Testing

Run the functional tests:

    export EXECUTABLE=/tmp/template-deno-executable
    behave
