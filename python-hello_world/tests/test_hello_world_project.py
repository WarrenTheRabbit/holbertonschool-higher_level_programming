import pytest
import os
import ast
import subprocess

TASK0 = "2-print.py"
TASK1 = "3-print_number.py"

task_files = [TASK0, TASK1]

@pytest.fixture(params=task_files)
def task_file(request):
    return request.param

def test_that_task_files_exist(task_file):
    with open(task_file):
        assert True

def test_that_task0_file_has_correct_shebang():
    expected = '#!/usr/bin/python3\n'
    with open(TASK0) as file:
        first_line = file.readline()
        assert first_line == expected

def test_that_task0_file_is_executable():
    assert os.access(TASK0, os.X_OK)

def test_that_source_of_task0_file_contains_print():
    expected = 'print('
    with open(TASK0) as file:
        for line in file:
            if expected in line:
                assert True
                return
    assert False

def test_that_ast_of_task0_file_contains_print():
    with open(TASK0) as file:
        tree = ast.parse(file.read())
        for node in ast.walk(tree):
            if (isinstance(node, ast.Call) 
                and isinstance(node.func, ast.Name) 
                and node.func.id == 'print'):
                assert True
                return
    assert False
    
def test_that_task0_file_outputs_correct_string():
    expected = "\"Programming is like building a multilingual puzzle\n"
    result = subprocess.run([f"./{TASK0}"], capture_output=True, text=True)
    assert result.stdout == expected

def test_that_task1_file_exists():
    with open(TASK1):
        assert True
        
def test_that_task1_file_has_correct_shebang():
    with open(TASK1) as file:
        first_line = file.readline()
        assert first_line == '#!/usr/bin/python3\n'
    

def test_that_task1_file_is_executable():
    assert os.access(TASK1, os.X_OK)
    
def test_that_task1_output_is_correct():
    expected = '98 Battery street\n'
    result = subprocess.run([f"./{TASK1}"], capture_output=True, text=True)
    assert result.stdout == expected
    
def test_that_task1_file_is_three_lines():
    with open(TASK1) as file:
        lines = file.readlines()
        assert len(lines) == 3
    
def test_that_source_of_task1_uses_fstring():
    with open(TASK1) as file:
        for line in file:
            if "print(f\"" in line:
                assert True
                return
    assert False
    
def test_that_ast_of_task1_uses_fstring():
    found_correctly_interpolated_fstring = False
    with open(TASK1) as file:
        tree = ast.parse(file.read())
    
    for node in ast.walk(tree):
        if (isinstance(node, ast.Call)
            and node.func.id == 'print'
            and any(isinstance(node, ast.JoinedStr) 
                    for node 
                    in node.args)
            and node.args[0].values[0].value.id == 'number'
        ):
            found_correctly_interpolated_fstring = True
            break
    assert found_correctly_interpolated_fstring, \
        "No evidence of f-string with variable 'number' found in task1."