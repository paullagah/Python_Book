import pytest
from Labs import beg1

def test1():
    assert beg1.output() == "Hello World!"

def test2():
    assert beg1.output1() == "Hello World!"

def test3():
    assert beg1.output2() != ""