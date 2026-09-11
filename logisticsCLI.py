#!/usr/bin/env python3

from mylib.logistics import get_distance, total_distance, cities, estimate_travel_time
import click

@click.group()
def cli():
    """A simple CLI for logistics calculations."""

# build a click command to get the distance between two cities
@cli.command("distance")
@click.argument('city1')
@click.argument('city2')
def distance(city1, city2):
    """Get the distance between two cities."""
    try:
        dist = get_distance(city1, city2)
        click.echo(f"The distance between {city1} and {city2} is {dist:.2f} km.")
    except ValueError as e:
        click.echo(str(e))

# build a click command to get the total distance between a dictionary of cities
@cli.command("total_distance")
@click.argument('city_dict', type=click.File('r'))
def total_distance_command(city_dict):
    """Get the total distance between a dictionary of cities."""
    try:
        import json
        city_dict = json.load(city_dict)
        dist = total_distance(city_dict)
        click.echo(f"The total distance between the cities is {dist:.2f} km.")
    except ValueError as e:
        click.echo(str(e))
    except json.JSONDecodeError:
        click.echo("Invalid JSON format for city dictionary.")

#build a click command to estimate travel time between two cities given a speed
@cli.command("travel_time")
@click.argument('city1')
@click.argument('city2')
@click.option('--speed', default=80, help='Speed in km/h (default is 80 km/h)')
def travel_time(city1, city2, speed):
    """Estimate the travel time between two cities given a speed in km/h."""
    try:
        time = estimate_travel_time(city1, city2, speed)
        click.echo(f"The estimated travel time between {city1} and {city2} at {speed} km/h is {time:.2f} hours.")
    except ValueError as e:
        click.echo(str(e))

# invoke the click command line interface
if __name__ == "__main__":
    cli()