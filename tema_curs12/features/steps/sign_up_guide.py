from behave import *
from time import sleep


@given('I am on the Sign in page')
def step_impl(context):
    context.sign_in.go_home()


@when('I click Sign up link')
def step_impl(context):
    context.sign_in.sign_up_button()
    sleep(2)


@when('I click Person option')
def step_impl(context):
    context.sign_up.person_button()


@when('I click continue')
def step_impl(context):
    context.sign_up.continue_button()


@when('I input "{first_name}" to the first name field')
def step_impl(context, first_name):
    context.sign_up.input_field(first_name)


# @when('I click continue')
# def step_impl(context):
#     context.sign_up.continue_button()


@when('I input "{last_name}" to the last name')
def step_impl(context, last_name):
    context.sign_up.input_field(last_name)


# @when('I click continue')
# def step_impl(context):
#     context.sign_up.continue_button()


@when('I input "{email}" to the email field')
def step_impl(context, email):
    context.sign_up.input_field(email)


@then('I verify that message is "<on/off>"')
def step_impl(context):
    pass
