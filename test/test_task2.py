import pytest
from src.task2 import get_int, get_float, get_string, get_bool

def test_int():
    assert isinstance(get_int(), int)

def test_float():
    assert isinstance(get_float(), float)

def test_string():
    assert isinstance(get_string(), str)

def test_bool():
    assert isinstance(get_bool(), bool)
