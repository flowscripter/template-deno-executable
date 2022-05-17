from behave import when, then


@when('the executable is launched')
def step_impl(context):
    context.pexpect_wrapper.start()


@then('the executable should complete successfully')
def step_impl(context):
    context.pexpect_wrapper.expect_eof()
    status = context.pexpect_wrapper.complete()
    assert status == 0, 'unexpected exit status: {}'.format(status)


@then('the executable should have output "{message}"')
def step_impl(context, message):
    context.pexpect_wrapper.expect(message)
