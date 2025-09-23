import pytest
from src.task7 import get_status_code

def test_get_stat_code():
    status = get_status_code('https://httpbin.org/status/200')
    assert status == 200
