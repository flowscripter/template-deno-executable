from behave import when, then


@when('the executable is launched')
def step_impl(context):
    context.pexpect_wrapper.start()


@then('the executable should complete successfully')
def step_impl(context):
    context.pexpect_wrapper.expect_eof()
    assert context.pexpect_wrapper.complete() == 0


@then('the executable should have output "{message}"')
def step_impl(context, message):
    context.pexpect_wrapper.expect(message)
