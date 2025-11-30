# Example 5.11: Snaps get_string function

import time
import snaps

name = snaps.get_string("Enter your name: ")
snaps.display_message("Hello " + name)

time.sleep(5)
