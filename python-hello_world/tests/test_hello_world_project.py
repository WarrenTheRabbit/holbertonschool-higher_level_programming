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

   
def test_that_script_uses_print_function():
    expected = 'print('
    with open(FILE) as file:
        for line in file:
            if expected in line:
                assert True
                return
    assert False
def test_that_ast_of_task0_file_contains_print():
    with open(FILE) as file:
        tree = ast.parse(file.read())
        for node in ast.walk(tree):
            if (isinstance(node, ast.Call) 
                and isinstance(node.func, ast.Name) 
                and node.func.id == 'print'):
                assert True
                return
    assert False
