from click.testing import CliRunner
import pytest

from helloworld import hello as hll

@pytest.fixture(scope="module")
def runner():
    return CliRunner()

def test_named_hello(runner):
    result = runner.invoke(hll)
    assert result.exit_code == 0
    assert result.output == 'Hello World!\n'
