"""
Exercise 16.1b Weather Data

Weather data code from Exercise 14.1
"""

import datetime
import urllib.request
import xml.etree.ElementTree

day_label_tuple = (
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
)


def order_day_labels(start_date):
    """
    Get the days of the week ordered by the current day

    Parameters
    ----------
    start_date : int
        Day of the week returned by a datetime object

    Returns
    -------
    tuple[str, str, str, str, str, str, str]
        Tuple containing the days of the week such that the current day
        is the first index, and the days follow sequentially
    """
    return day_label_tuple[start_date:] + day_label_tuple[:start_date]


def make_seven_day_forecast(start_date, temperatures):
    """
    Converts a sequence of temperatures into a forecast based
    on a current date

    Given a sequence of seven temperatures, and the start date
    produces a forecast as a dictionary, keyed by the the day
    of the week

    Parameters
    ----------
    start_date : int
        Day of the week represented by a `datetime` object index
        for a day of the week
    temperatures : tuple[int]
        Tuple containing a 7 day sequence of temperature values

    Returns
    -------
    Dict[str, int]
        Dictionary containing a seven day forecast as keyed by the
        day of the week and the temperature. Ordered from current day to current day + 6
    """
    # if len(temperatures) != 7:
    #    raise ValueError("temperatures must be of length 7")

    # not pythonic but consistent with what we've seen so far
    dictionary = {}
    ordered_days = order_day_labels(start_date)
    for i, t in enumerate(temperatures):
        try:
            dictionary[ordered_days[i]] = t
        except IndexError:
            break

    return dictionary


def get_weather_temp(latitude, longitude):
    """
    Return the weather temperature data at a given latitude and longitude

    Relies on US weather data, so should not be expected to work for
    latitude and longitude values outside of the US

    Parameters
    ----------
    latitude : int | float
        latitude of the location to get the weather data for
    longitude : int | float
        longitude of the location to get the weather data for

    Returns
    -------
    Forecast
        7 day forecast for the maximum temperature
        in Fahrenheit, with the current day as the first
        value
    Forecast
        7 day forecast for the minimum temperature
        in Fahrenheit, with the current day as the first
        value
    int | float
        Most recent apparent temperature value
    int | float
        Most recent dew point temperature
    """
    address = "http://forecast.weather.gov/MapClick.php"
    query = "?lat={0}&lon={1}&unit=0&lg=english&FcstType=dwml".format(
        latitude, longitude
    )
    req = urllib.request.urlopen(address + query)
    page = req.read()
    doc = xml.etree.ElementTree.fromstring(page)

    def get_temp_list(e):
        """
        Convert value subelements of an element e
        into a list of temperatures

        Parameters
        ----------
        e : XML Element
            Temperature element

        Returns
        -------
        list[int]
            list of integers corresponding to temperatures.
            If none found, then the list is empty
        """
        res = []
        for d in e.iter("value"):
            res.append(int(d.text))  # type: ignore
        return res

    def get_temp_val(e):
        """
        Convert a temperature value subelement of a
        temperature element to its value

        Parameters
        ----------
        e : XML Element
            Temperature element

        Returns
        -------
        int
            temperature value in Fahrenheit
            as an int
        """
        return get_temp_list(e)[0]

    for d in doc.iter("temperature"):
        if d.get("type") == "apparent":
            apparent_temp = get_temp_val(d)
        elif d.get("type") == "dew point":
            dew_point = get_temp_val(d)
        elif d.get("type") == "maximum":
            max_temp = get_temp_list(d)
        elif d.get("type") == "minimum":
            min_temp = get_temp_list(d)

    today = datetime.datetime.today().weekday()
    return (
        make_seven_day_forecast(today, max_temp),  # type: ignore
        make_seven_day_forecast(today, min_temp),  # type: ignore
        apparent_temp,  # type: ignore
        dew_point,  # type: ignore
    )


if __name__ == "__main__":
    latitude = 47.61
    longitude = -122.33

    max_t, min_t, apparent_t, dew_p = get_weather_temp(latitude, longitude)

    days_table_hdr = "\t".join(
        map(lambda a: str(a)[:2], max_t)
    )  # slice of the first two characters of the day of the week
    max_t_str = "\t".join(map(str, max_t.values()))
    min_t_str = "\t".join(map(str, min_t.values()))

    forecast = days_table_hdr + "\n" + max_t_str + "\n" + min_t_str

    observation_t_str = "Apparent temperature: {0}\nDew point temperature: {1}".format(
        apparent_t, dew_p
    )

    print("Temperature Information for Seattle")
    print(forecast + "\n" + observation_t_str)
