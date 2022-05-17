from pexpect.popen_spawn import PopenSpawn
from pexpect import EOF
import logging
log = logging.getLogger("pexpect_wrapper")


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

        found = ''
        while len(self.output) > 0:
            next_line = self.output.pop(0)
            log.debug('looking for "{}" in "{}"'.format(message, next_line))
            if message in next_line:
                found = next_line
                break

        assert found != '', 'expected {} in output'.format(message)


    def expect_eof(self):
        assert self.child is not None

        self.child.expect(EOF)

    def complete(self):
        assert self.child is not None

        exit_status = self.child.wait()

        self.output = self.child.before.split('\n')

        return exit_status
