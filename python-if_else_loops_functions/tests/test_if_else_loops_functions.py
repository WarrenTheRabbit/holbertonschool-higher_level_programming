import pytest
import subprocess

TASK0 = "0-positive_or_negative.py"

#######################################
# Fixtures
#######################################
@pytest.fixture(params=[TASK0])
def task_file(request):
    return request.param

@pytest.fixture
def run_script():
    def _run_script(task_file):
        process = subprocess.run([f"{task_file}"], 
                                 capture_output=True, 
                                 text=True)
        return process
        
    return _run_script
@pytest.fixture
def run_task0(tmp_path, run_script):
    def _run_script(task_file, mock_int) -> subprocess.CompletedProcess:
        with open(task_file, "r") as opened_file:
            script_content = opened_file.read()
        mock_script = script_content.replace(
            "random.randint(-10, 10)",
            str(mock_int)
        )
     
        script_path = tmp_path / "tmp_script.py"
        print(script_path)
        with open(script_path, "w") as opened_file:
            opened_file.write(mock_script)
            
        os.chmod(script_path, os.stat(task_file).st_mode | stat.S_IEXEC)
            
        process:subprocess.CompletedProcess = run_script(script_path)
        
        return process

    return _run_script

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