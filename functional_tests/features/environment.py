import os


def before_all(context):

    context.executable = os.environ.get('EXECUTABLE')
