from utils import execute_inverted_algorithm


def test_inverted_algorithm_default_setup0() -> None:
    new_setup = ''.join(execute_inverted_algorithm('||///\\\\||/\\|'))
    assert new_setup == '||//||\\||/\\|'


def test_inverted_algorithm_setup1() -> None:
    new_setup = ''.join(execute_inverted_algorithm('\\\\///\\\\||/\\|'))
    assert new_setup == '|\\//||\\||/\\|'


def test_inverted_algorithm_setup2() -> None:
    new_setup = ''.join(execute_inverted_algorithm('||///\\\\||///'))
    assert new_setup == '||//||\\||//|'
