from mylib.calc import add, subtract, multiply, divide, exponentiate
from calCLI import cli

# write a test for each command in calCLI.py using click.testing.CliRunner
from click.testing import CliRunner


def test_add_command():
    runner = CliRunner()
    result = runner.invoke(cli, ["add", "2", "3"])
    assert result.exit_code == 0
    assert "The result of adding 2.0 and 3.0 is: 5.0" in result.output


def test_subtract_command():
    runner = CliRunner()
    result = runner.invoke(cli, ["subtract", "5", "3"])
    assert result.exit_code == 0
    assert "The result of subtracting 3.0 from 5.0 is: 2.0" in result.output


def test_multiply_command():
    runner = CliRunner()
    result = runner.invoke(cli, ["multiply", "2", "3"])
    assert result.exit_code == 0
    assert "The result of multiplying 2.0 and 3.0 is: 6.0" in result.output


def test_divide_command():
    runner = CliRunner()
    result = runner.invoke(cli, ["divide", "6", "2"])
    assert result.exit_code == 0
    assert "The result of dividing 6.0 by 2.0 is: 3.0" in result.output

    # Test division by zero
    result = runner.invoke(cli, ["divide", "6", "0"])
    assert result.exit_code == 0
    assert "Error: Cannot divide by zero" in result.output


def test_exponentiate_command():
    runner = CliRunner()
    result = runner.invoke(cli, ["exponentiate", "2", "3"])
    assert result.exit_code == 0
    assert "The result of 2.0 raised to the power of 3.0 is: 8.0" in result.output


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0


def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(1, 1) == 0
    assert subtract(0, 0) == 0


def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-1, 1) == -1
    assert multiply(0, 0) == 0


def test_divide():
    assert divide(6, 2) == 3
    assert divide(1, 1) == 1
    assert divide(0, 1) == 0


def test_exponentiate():
    assert exponentiate(2, 3) == 8
    assert exponentiate(-1, 1) == -1
    assert exponentiate(0, 0) == 1
