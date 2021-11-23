import os

from support.pexpect_wrapper import PExpectWrapper


def before_all(context):

    context.pexpect_wrapper = PExpectWrapper(os.environ.get('EXECUTABLE'))
