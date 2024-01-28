import pytest

TASK0 = "0-positive_or_negative.py"

#######################################
# Fixtures
#######################################
@pytest.fixture(params=[TASK0])
def task_file(request):
    return request.param


########################################
# Tests
########################################
def test_that_task_file_exists(task_file):
    with open(task_file):
        assert True
        return
    
def test_that_task_file_has_python_shebang(task_file):
    expected_shebang_line = '#!/usr/bin/python3\n'
    with open(task_file) as opened_file:
        first_line = opened_file.readline()
        assert first_line == expected_shebang_line