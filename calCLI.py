#!/usr/bin/env python3


from mylib.calc import add, subtract, multiply, divide, exponentiate
import click


@click.group()
def cli():
    """A simple calculator CLI"""


@cli.command("add")
@click.argument("a", type=float)
@click.argument("b", type=float)
def add_command(a, b):
    """Add two numbers"""
    result = add(a, b)
    click.echo(f"The result of adding {a} and {b} is: {result}")


@cli.command("subtract")
@click.argument("a", type=float)
@click.argument("b", type=float)
def subtract_command(a, b):
    """Subtract two numbers"""
    result = subtract(a, b)
    click.echo(f"The result of subtracting {b} from {a} is: {result}")


@cli.command("multiply")
@click.argument("a", type=float)
@click.argument("b", type=float)
def multiply_command(a, b):
    """Multiply two numbers"""
    result = multiply(a, b)
    click.echo(f"The result of multiplying {a} and {b} is: {result}")


@cli.command("divide")
@click.argument("a", type=float)
@click.argument("b", type=float)
def divide_command(a, b):
    """Divide two numbers"""
    try:
        result = divide(a, b)
        click.echo(f"The result of dividing {a} by {b} is: {result}")
    except ValueError as e:
        click.echo(f"Error: {e}")


@cli.command("exponentiate")
@click.argument("a", type=float)
@click.argument("b", type=float)
def exponentiate_command(a, b):
    """Exponentiate two numbers"""
    result = exponentiate(a, b)
    click.echo(f"The result of {a} raised to the power of {b} is: {result}")


if __name__ == "__main__":
    cli()
