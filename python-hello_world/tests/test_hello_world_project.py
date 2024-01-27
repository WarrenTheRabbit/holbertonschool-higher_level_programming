import pytest
import os
import ast
import subprocess

TASK0 = "2-print.py"
TASK1 = "3-print_number.py"
TASK2 = "4-print_float.py"
TASK3 = "5-print_string.py"
TASK4 = "6-concat.py"
TASK5 = "7-edges.py"
TASK6 = "8-concat_edges.py"
TASK7 = "9-easter_egg.py"

completed = 4

#########################################
# Test Data
#########################################

task_files = [TASK0, TASK1, TASK2, TASK3, TASK4, TASK5, TASK6, TASK7][:completed]
required_task_file_line_counts = [None, 3][:completed]
task_outputs = [
    "\"Programming is like building a multilingual puzzle\n",
    "98 Battery street\n",
    "Float: 3.14\n",
    "Holberton SchoolHolberton SchoolHolberton School\nHolberton\n",
    "Welcome to Holberton School!\n",
    """First 3 letters: Hol
Last 2 letters: on
Middle word: olberto
""",
"object-oriented programming with Python\n",
"""The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
"""][:completed]

#########################################
# Test Fixtures
#########################################

@pytest.fixture
def run_script():
    def _run_script(script_name):
        result = subprocess.run([f"./{script_name}"], 
                                capture_output=True,
                                text=True)
        return result.stdout
    return _run_script


@pytest.fixture(params=task_files)
def task_file(request):
    return request.param
    

#########################################
# Tests that all task files must pass
#########################################
def test_that_task_file_exists(task_file):
    with open(task_file):
        assert True

def test_that_task_file_has_python_shebang(task_file):
    expected = '#!/usr/bin/python3\n'
    with open(task_file) as file:
        first_line = file.readline()
        assert first_line == expected

def test_that_task_file_is_executable(task_file):
    assert os.access(TASK0, os.X_OK)

@pytest.mark.parametrize(("file", "expected_line_count"), 
                         [(file, expected_line_count)
                          for file, expected_line_count
                          in zip(task_files, required_task_file_line_counts)
                          if expected_line_count is not None
                         ])
def test_that_task_file_has_required_number_of_lines(file, expected_line_count):       
    with open(file) as opened_file:
        lines = opened_file.readlines()
        assert len(lines) == expected_line_count
        

@pytest.mark.parametrize(("file", "expected_output"),
                         zip(task_files, task_outputs))
def test_that_task_file_output_is_correct(run_script, file, expected_output):
    actual_output = run_script(f"./{file}")
    assert actual_output == expected_output

#########################################
# Tests specific to task0
######################################### 
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
        
#########################################
# Tests specific to task1
#########################################        
def test_that_task1_output_is_correct():
    expected = '98 Battery street\n'
    result = subprocess.run([f"./{TASK1}"], capture_output=True, text=True)
    assert result.stdout == expected
    
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
        
#########################################
# Tests specific to task2
#########################################


#########################################
# Tests specific to task3
#########################################



#########################################
# Tests specific to task4
#########################################



#########################################
# Tests specific to task5
#########################################