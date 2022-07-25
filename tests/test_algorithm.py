from utils import execute_algorithm

def test_algorithm_setup0() -> None:
    new_setup = ''.join(execute_algorithm('||//||\\||/\\|'))
    assert new_setup == '||///\\\\||/\\|'

def test_algorithm_setup1() -> None:
    new_setup = ''.join(execute_algorithm('|\\//||\\||/\\|'))
    assert new_setup == '\\\\///\\\\||/\\|'

def test_algorithm_setup2() -> None:
    new_setup = ''.join(execute_algorithm('||//||\\||//|'))
    assert new_setup == '||///\\\\||///'