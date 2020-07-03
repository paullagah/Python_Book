import pytest
from Labs import beg1
from Labs.beg1 import *

def test_one():
    assert beg1.output() == "Hello World!"

def test_two():
    assert beg1.output1(hello) == "Hello World"

def test_three():
    assert beg1.output2(input1) != ""

def test_four():
    assert beg1.output3(num1, num2) == (num1 + num2)

def test_five():
    assert beg1.output4("True", num3, num4) == (num3 + num4)
    assert beg1.output4(False, num3, num4) == (num3 * num4)