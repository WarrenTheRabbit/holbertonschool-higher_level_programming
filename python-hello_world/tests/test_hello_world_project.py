import pytest

def test_that_file_exists():
    with open("2-print.py"):
        assert True

def test_that_file_has_correct_shebang():
    expected = '#!/usr/bin/env python3'

    with open("2-print.py") as file:
        first_line = file.readline()
        assert first_line == expected

