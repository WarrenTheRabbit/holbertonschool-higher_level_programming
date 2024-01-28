import pytest

TASK0 = "0-positive_or_negative.py"


@pytest.fixture(params=[TASK0])
def task_file(request):
    return request.param

def test_that_task_file_exists(task_file):
    with open(task_file):
        assert True
        return
    pytest.fail("Task file does not exist.")