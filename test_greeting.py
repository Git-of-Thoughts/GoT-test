import pytest
from greeting import Greeting

def test_greeting_message():
    greeting = Greeting()
    assert greeting.message() == 'Hello, World!'
