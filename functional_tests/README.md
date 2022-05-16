## Executable Functional Tests

#### Setup

Ensure the executable is built:

    deno compile --unstable --allow-env --allow-read --allow-write --allow-ffi --allow-net --output /tmp/template-deno-executable ../mod.ts

Install requirements:

    pip3 install -r pip-requirements.txt

#### Testing

Run the functional tests:

    export EXECUTABLE=/tmp/template-deno-executable
    behave
