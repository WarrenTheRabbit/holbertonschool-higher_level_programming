import pytest

def test_that_file_exists():
    with open("2-print.py"):
        assert True
