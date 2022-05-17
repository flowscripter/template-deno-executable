from pexpect.popen_spawn import PopenSpawn
from pexpect import EOF


class PExpectWrapper:

    def __init__(self, executable):
        self.executable = executable
        self.child = None
        self.output = None

    def start(self):
        assert self.child is None

        self.child = PopenSpawn(self.executable, encoding='utf-8')

    def expect(self, message):
        assert self.child is not None

        output = ''
        while output == '':
            assert len(self.output) > 0, 'expected an output line'
            output = self.output.pop(0)

        assert message in output, 'expected {} in {}'.format(message, output)

    def expect_eof(self):
        assert self.child is not None

        self.child.expect(EOF)

    def complete(self):
        assert self.child is not None

        exit_status = self.child.wait()

        self.output = self.child.before.split('\n')

        return exit_status
