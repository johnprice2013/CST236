from behave import given, when, then
import sys
import os

sys.path.insert(0, os.path.abspath(".."))

import source.program

@given('file used for initialization is correct')
def step_impl(context):
    context.testProgram = source.program.Program('cities.txt')

@when('initialize is called')
def step_impl(context):
    context.testProgram.initialize()

@then('the cities will be read from file')
def step_impl(context):
    assert context.testProgram.readSuccessful is True

@given('file used for initialization is incorrect')
def step_impl(context2):
        context2.testProgram = source.program.Program('citiesnotthere.txt')

@when('initialize is called 2')
def step_impl(context2):
    context2.testProgram.initialize()

@then('the program will respond with error')
def stepImpl(context2):
    context2.testProgram.readSuccessful is False
import source.city

