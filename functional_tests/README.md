## Executable Functional Tests

#### Setup

Ensure the executable is built:

    deno compile --unstable-ffi --allow-env --allow-read --allow-write --allow-ffi --allow-net --output /tmp/template-deno-executable ../mod.ts

Install requirements:

    pip3 install -r pip-requirements.txt

#### Testing

Run the functional tests:

    export EXECUTABLE=/tmp/template-deno-executable
    behave

To run with logging output from the test steps (this is the best set of arguments I can find):

    behave --no-logcapture --no-color --logging-level=DEBUG
