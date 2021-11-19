import pexpect


class PExpectWrapper:

    def __init__(self, executable):
        self.executable = executable
        self.child = None
        self.output = None

    def start(self):
        assert self.child is None

        self.child = pexpect.spawn(self.executable, encoding='utf-8')

    def expect(self, message):
        assert self.child is not None

        output = ''
        while output == '':
            assert len(self.output) > 0
            output = self.output.pop(0)

        assert message in output

    def expect_eof(self):
        assert self.child is not None

        self.child.expect(pexpect.EOF)

    def complete(self):
        assert self.child is not None

        self.child.close()

        self.output = self.child.before.split('\r\n')

        assert self.child.signalstatus is None
        return self.child.exitstatus
