# Exercise 12.3a Ride Selector
#
# Refactors the Ride Selector Program to be suitable for testing

import BTCInput


class Ride:
    """
    A class representing a theme park amuse ride rider limitations

    Attributes
    ----------
    name : str
        name of the ride

    min_age : int
        minimum age in years to ride

    max_age : int
        maximum age in years to ride, must be greater than or equal to `min_age`

    Class Attributes
    ----------------
    ride_min_age : int
        minimum `min_age` for any ride

    ride_max_age : int
        maximum `max_age` for any ride

    """

    ride_min_age = 1
    ride_max_age = 95

    @staticmethod
    def is_valid_age_limit(age):
        """
        Check a proposed ride age limit is valid

        Parameters
        ----------
        age : int
            proposed age limit in years

        Returns
        -------
        bool
            `True` if `age` is an allowed age limit, else `False`

        See Also
        --------
        Ride.ride_min_age : minimum valid age limit for a ride
        Ride.ride_max_age : maximum valid age limit for a ride
        """
        return Ride.ride_min_age <= age <= Ride.ride_max_age

    def __init__(self, name, min_age, max_age):
        """
        Creates a new `Ride` instance

        Parameters
        ----------
        name : str
            name of the ride
        min_age : int
            minimum age (inclusive) to ride in years
        max_age : int
            maximum age to ride (inclusive) to ride in years.
            `max_age` must be `>= min_age`

        Raises
        ------
        ValueError
            Raised if `max_age` is `< min_age`
        ValueError
            Raised if `min_age` or `max_age` is not a valid age limit

        See Also
        --------
        Ride.is_valid_age_limit : Checks that ages are valid
        """
        if not Ride.is_valid_age_limit(min_age):
            raise ValueError(
                "{0} is not a valid age for the minimum age limit".format(min_age)
            )
        if not Ride.is_valid_age_limit(max_age):
            raise ValueError(
                "{0} is not a valid age for the maximum age limit".format(max_age)
            )
        if max_age < min_age:
            raise ValueError(
                "maximum age ({0}) must be greater than or equal to minimum age ({1})".format(
                    max_age, min_age
                )
            )
        self.name = name
        self.min_age = min_age
        self.max_age = max_age

    def __str__(self):
        return str(self.name)

    def in_age_limit(self, age):
        """
        Validate that an age is within the limits of the ride

        Parameters
        ----------
        age : int
            age in years to validate is within the age limit

        Returns
        -------
        bool
            `True` if the age is within the ride limits, else `False`
        """
        return self.min_age <= age <= self.max_age


class RideSelector:
    """
    Provides a text-based interface for a Ride Selector
    """

    def __init__(self):
        """
        Create a new `RideSelector` instance
        """
        self._rides = (
            Ride(
                "Scenic River Cruise",
                min_age=Ride.ride_min_age,
                max_age=Ride.ride_max_age,
            ),
            Ride("Carnival Carousel", min_age=3, max_age=Ride.ride_max_age),
            Ride("Jungle Adventure Water Splash", min_age=6, max_age=Ride.ride_max_age),
            Ride("Downhill Mountain Run", min_age=12, max_age=Ride.ride_max_age),
            Ride("The Regurgitator", min_age=12, max_age=70),
        )

    def __str__(self):
        return "\n".join(
            map(
                lambda enumerate_pair: "{0}. {1}".format(
                    enumerate_pair[0] + 1, enumerate_pair[1]
                ),
                enumerate(self._rides),
            )
        )

    def get_ride(self, index):
        """
        Get's the ride associated with a given index

        Parameters
        ----------
        index : int
            integer greater than zero corresponding a ride index

        Returns
        -------
        Ride
            the ride stored by the given index

        Raises
        ------
        ValueError
            Raised if `index <= 0`
        IndexError
            Raised if the no ride exists for the given index
        """
        if index <= 0:
            raise ValueError("index must be a positive integer")
        return self._rides[index - 1]

    def check_age_against_ride(self, ride, age):
        """
        Provides a string describing in a rider of `age` years can ride the Ride `ride`

        Parameters
        ----------
        ride : Ride
            ride to check the age against
        age : int
            age of the prospective rider in years

        Returns
        -------
        str
            string describing if a rider of `age` years can ride `ride`
        """
        if age < Ride.ride_min_age:
            return "You are too young to go on any rides"
        elif age > Ride.ride_max_age:
            return "You are too old to go on any rides"
        elif age < ride.min_age:
            return "Sorry, you are too young"
        elif age > ride.max_age:
            return "Sorry, you are too old"
        else:
            return "You can go on the ride"

    def run_main_menu(self):
        """
        Provides a looping main menu

        Returns
        -------
        None
        """
        main_menu = """Welcome to our Theme Park
These are the available rides:
{0}
Press 0 to quit the program

Please enter the ride number you want: """.format(str(self))

        while True:
            ride_number = BTCInput.read_int_ranged(main_menu, 0, len(self._rides) + 1)

            if ride_number == 0:
                break
            else:
                try:
                    ride = self.get_ride(ride_number)
                    age = BTCInput.read_int("Please enter your age: ")
                    out_string = self.check_age_against_ride(ride, age)
                    print(
                        "You have selected {0}\n{1}".format(ride, out_string)
                        if Ride.is_valid_age_limit(age)
                        else out_string
                    )

                except IndexError:
                    print("Error: No ride found for that option! Choose again")


if __name__ == "__main__":
    app = RideSelector()
    app.run_main_menu()
