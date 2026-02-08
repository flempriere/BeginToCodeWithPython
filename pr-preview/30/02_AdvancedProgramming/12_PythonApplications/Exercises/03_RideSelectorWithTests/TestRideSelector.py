# Exercise 12.3b Test Ride Selector
#
# unittest based testing framework for Ride Selector


import unittest

import RideSelector

# tests for Ride

always_valid_middle_age = (
    RideSelector.Ride.ride_min_age + RideSelector.Ride.ride_max_age
) // 2


class TestRide(unittest.TestCase):
    """
    Test class implementing unit tests for the `Ride` class
    """

    # Test case for `is_valid_age_limit`

    def test_is_valid_age_accepts_normal_age(self):
        self.assertTrue(RideSelector.Ride.is_valid_age_limit(always_valid_middle_age))

    def test_is_valid_age_accepts_min_age(self):
        self.assertTrue(
            RideSelector.Ride.is_valid_age_limit(RideSelector.Ride.ride_min_age)
        )

    def test_is_valid_age_accepts_max_age(self):
        self.assertTrue(
            RideSelector.Ride.is_valid_age_limit(RideSelector.Ride.ride_max_age)
        )

    def test_is_valid_age_rejects_less_than_min_age(self):
        self.assertFalse(
            RideSelector.Ride.is_valid_age_limit(RideSelector.Ride.ride_min_age - 1)
        )

    def test_is_valid_age_rejects_greater_than_max_age(self):
        self.assertFalse(
            RideSelector.Ride.is_valid_age_limit(RideSelector.Ride.ride_max_age + 1)
        )

    # Test cases for init

    def test_init_sets_attributes_correctly(self):
        ride = RideSelector.Ride(
            "Test", min_age=always_valid_middle_age, max_age=always_valid_middle_age
        )
        self.assertEqual(ride.name, "Test")
        self.assertEqual(ride.min_age, always_valid_middle_age)
        self.assertEqual(ride.max_age, always_valid_middle_age)

    def test_init_raises_valueerror_on_invalid_min_age(self):
        with self.assertRaises(ValueError):
            ride = RideSelector.Ride(  # noqa: F841
                "Test",
                min_age=RideSelector.Ride.ride_min_age - 1,
                max_age=always_valid_middle_age,
            )

    def test_init_raises_valueerror_on_invalid_max_age(self):
        with self.assertRaises(ValueError):
            ride = RideSelector.Ride(  # noqa: F841
                "Test",
                min_age=always_valid_middle_age,
                max_age=RideSelector.Ride.ride_max_age + 1,
            )

    def test_init_raises_value_error_if_max_age_less_than_min_age(self):
        with self.assertRaises(ValueError):
            ride = RideSelector.Ride(  # noqa: F841
                "Test",
                min_age=RideSelector.Ride.ride_max_age + 1,
                max_age=RideSelector.Ride.ride_min_age - 1,
            )

    def test_str_returns_ride_name(self):
        ride = RideSelector.Ride(
            "Test",
            min_age=always_valid_middle_age,
            max_age=always_valid_middle_age,
        )
        self.assertEqual(str(ride), "Test")

    def test_in_age_limit_accepts_valid_age(self):
        ride = RideSelector.Ride(
            "Test",
            min_age=always_valid_middle_age,
            max_age=always_valid_middle_age,
        )
        self.assertTrue(ride.in_age_limit(always_valid_middle_age))

    def test_in_age_limit_rejects_too_small_age(self):
        ride = RideSelector.Ride(
            "Test",
            min_age=always_valid_middle_age,
            max_age=always_valid_middle_age,
        )
        self.assertFalse(ride.in_age_limit(ride.min_age - 1))

    def test_in_age_limit_rejects_too_large_age(self):
        ride = RideSelector.Ride(
            "Test",
            min_age=always_valid_middle_age,
            max_age=always_valid_middle_age,
        )
        self.assertFalse(ride.in_age_limit(ride.max_age + 1))


# Test RideSelector


class TestRideSelector(unittest.TestCase):
    """
    Test cases for the `RideSelector` class
    """

    # test str method
    def test_str_creates_enumerated_table(self):
        ride_selector = RideSelector.RideSelector()
        expected_str = """1. Scenic River Cruise
2. Carnival Carousel
3. Jungle Adventure Water Splash
4. Downhill Mountain Run
5. The Regurgitator"""
        self.assertEqual(str(ride_selector), expected_str)

    # test get_ride method

    def test_get_ride_returns_expected_ride(self):
        ride_selector = RideSelector.RideSelector()
        ride = ride_selector.get_ride(1)
        self.assertEqual(str(ride), "Scenic River Cruise")

    def test_get_ride_raises_valueerror_on_zero_index(self):
        ride_selector = RideSelector.RideSelector()

        with self.assertRaises(ValueError):
            ride_selector.get_ride(0)

    def test_get_ride_raises_valueerror_on_invalid_index(self):
        ride_selector = RideSelector.RideSelector()

        with self.assertRaises(IndexError):
            ride_selector.get_ride(99)

    # test check age against ride

    def test_too_young_for_any_ride(self):
        ride_selector = RideSelector.RideSelector()
        ride = ride_selector.get_ride(1)
        self.assertEqual(
            "You are too young to go on any rides",
            ride_selector.check_age_against_ride(
                ride, RideSelector.Ride.ride_min_age - 1
            ),
        )

    def test_too_old_for_any_ride(self):
        ride_selector = RideSelector.RideSelector()
        ride = ride_selector.get_ride(1)
        self.assertEqual(
            "You are too old to go on any rides",
            ride_selector.check_age_against_ride(
                ride, RideSelector.Ride.ride_max_age + 1
            ),
        )

    def test_too_young_for_specific_ride(self):
        ride_selector = RideSelector.RideSelector()
        ride = ride_selector.get_ride(5)
        self.assertEqual(
            "Sorry, you are too young",
            ride_selector.check_age_against_ride(ride, ride.min_age - 1),
        )

    def test_too_old_for_specific_ride(self):
        ride_selector = RideSelector.RideSelector()
        ride = ride_selector.get_ride(5)
        self.assertEqual(
            "Sorry, you are too old",
            ride_selector.check_age_against_ride(ride, ride.max_age + 1),
        )

    def test_valid_age_is_accepted(self):
        ride_selector = RideSelector.RideSelector()
        ride = ride_selector.get_ride(5)
        self.assertEqual(
            "You can go on the ride",
            ride_selector.check_age_against_ride(ride, ride.min_age),
        )


unittest.main(verbosity=2)
