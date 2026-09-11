from mylib.logistics import get_distance, total_distance, cities, estimate_travel_time


def test_get_distance():
    # Test distance between New York and Los Angeles
    dist = get_distance("New York", "Los Angeles")
    assert round(dist, 2) == 3944.42  # Approximate distance in km

    # Test distance between Chicago and Houston
    dist = get_distance("Chicago", "Houston")
    assert round(dist, 2) == 1513.97  # Approximate distance in km

    # Test invalid city
    try:
        get_distance("New York", "Invalid City")
        assert False, "Expected ValueError for invalid city"
    except ValueError:
        pass


def test_total_distance():
    # Test total distance for a dictionary of cities
    city_dict = {
        "New York": (40.7128, -74.0060),
        "Los Angeles": (34.0522, -118.2437),
        "Chicago": (41.8781, -87.6298),
    }
    dist = total_distance(city_dict)
    expected_dist = get_distance("New York", "Los Angeles") + get_distance(
        "Los Angeles", "Chicago"
    )
    assert round(dist, 2) == round(expected_dist, 2)


def test_estimate_travel_time():
    # Test travel time between New York and Los Angeles at 80 km/h
    time = estimate_travel_time("New York", "Los Angeles", speed_kmh=80)
    expected_time = get_distance("New York", "Los Angeles") / 80
    assert round(time, 2) == round(expected_time, 2)

    # Test travel time between Chicago and Houston at 100 km/h
    time = estimate_travel_time("Chicago", "Houston", speed_kmh=100)
    expected_time = get_distance("Chicago", "Houston") / 100
    assert round(time, 2) == round(expected_time, 2)

    # Test invalid city
    try:
        estimate_travel_time("New York", "Invalid City", speed_kmh=80)
        assert False, "Expected ValueError for invalid city"
    except ValueError:
        pass
