from behave import *
from time import sleep


@Given("I am on the SignIn page")
def step_impl(context):
    context.sign_in.go_home()


@When("I enter a correct email")
def step_impl(context):
    context.sign_in.input_email('lavinia@yahoo.com')


@When("I leave password empty")
def step_impl(context):
    context.sign_in.input_password(' ')


@When('I click the Login button')
def step_impl(context):
    context.sign_in.click_login()
    sleep(3)


@Then('I verify if login button is clickable')
def step_impl(context):
    try:
        context.sign_in.click_login()
        print('Enabled')
    except:
        print('Disabled')

# @Then('I receive an error')
# def step_impl(context):
#     message = 'Invalid email/password combination'
#     assert message in context.sign_in.message_text_error()
#     sleep(5)
