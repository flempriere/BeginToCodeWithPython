# Exercise 4.3: Weather Display
#
# Displays the Weather in Seattle

import snaps

temperature_fahrenheit = snaps.get_weather_temp(latitude=47.61, longitude=-122.33)
temperature_string = "The temperature in Seattle is: " + str(temperature_fahrenheit)

weather_descr = snaps.get_weather_description(latitude=47.61, longitude=-122.33)
weather_descr_string = "The conditions are: " + str(weather_descr)

weather_string = temperature_string + "\n" + weather_descr_string

snaps.display_message(weather_string, size=100)

input("Press enter to continue...")
