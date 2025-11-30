# Example 5.12: Theme Park Snaps Display
# Reimplments the shell of the Ride Selector Menu using Snaps

import time
import snaps


snaps.display_image("themepark.png")

prompt = """Welcome to our Theme Park
      These are the available ride:

      1. Scenic River Cruise
      2. Carnival Carousel
      3. Jungle Adventure Water Splash
      4. Downhill Mountain Run
      5. The Regurgitator

      Select your ride: """

ride_number_text = snaps.get_string(prompt, vert="bottom", max_line_length=3)
confirm = "Ride " + ride_number_text

snaps.display_message(confirm)
time.sleep(5)  # gives user time to read the output
