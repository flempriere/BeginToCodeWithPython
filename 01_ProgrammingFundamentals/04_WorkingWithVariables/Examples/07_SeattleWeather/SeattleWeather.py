# Example 4.7: Seattle Weather
#
# Uses snaps to get a description of the weather in Seattle

import snaps

desc = snaps.get_weather_description(latitude=47.61, longitude=-122.33)
print("The conditions are:", desc)
