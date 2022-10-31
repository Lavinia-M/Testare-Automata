from behave import *
from time import sleep


@Given('I am on the Jules SignIn page')
def step_impl(context):
    context.sign_in.go_home()


@When('I click sign up button')
def step_impl(context):
    context.sign_in.sign_up_button()
    sleep(2)


@Then('I am redirected on the Sign up page')
def step_impl(context):
    assert context.sign_up.verify_url()
    sleep(2)


@When('I click login button')
def step_impl(context):
    context.sign_up.go_to_login_btn()


@Then('I am again on the Signin page')
def step_impl(context):
    assert context.sign_in.verify_url()
    sleep(2)

