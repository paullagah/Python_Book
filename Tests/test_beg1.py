import pytest
from Labs import beg1
from Labs.beg1 import *


# def test_one():
#     assert beg1.output() == "Hello World!"
#
# def test_two():
#     assert beg1.output1(hello) == "Hello World"
#
# def test_three():
#     assert beg1.output2(input1) != ""
#
# def test_four():
#     assert beg1.output3(num1, num2) == (num1 + num2)
#
# def test_five():
#     assert beg1.output4("True", num3, num4) == (num3 + num4)
#     assert beg1.output4(False, num3, num4) == (num3 * num4)
#
# def test_six():
#     assert beg1.output5(bool2, 0, num6) == num6
#     assert beg1.output5(bool2, num5, 0) == num5
#     assert beg1.output5("True", num5, num6) == (num5 + num6)
#     assert beg1.output5(False, num5, num6) == (num5 * num6)
#
# def test_seven():
#     assert beg1.output6() == loop
#
# def test_eight():
#     assert beg1.output7(l1) == l1[0]
#
# def test_nine():
#     assert beg1.output8(l1) == l1[::1]

def test_ten():
    assert beg1.output9(l2) == (l2 * 10)
