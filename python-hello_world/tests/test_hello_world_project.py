import pytest
import os

FILE = "2-print.py"

def test_that_file_exists():
    with open(FILE):
        assert True

def test_that_file_has_correct_shebang():
    expected = '#!/usr/bin/env python3\n'
    with open(FILE) as file:
        first_line = file.readline()
        assert first_line == expected

def test_that_file_is_executable():
    assert os.access(FILE, os.X_OK)
    