# Example 4.6: Seattle Temperature
# Get the current temperature in Seattle

import snaps

temp = snaps.get_weather_temp(latitude=47.61, longitude=-122.33)

print("The temperature in Seattle is:", temp)
