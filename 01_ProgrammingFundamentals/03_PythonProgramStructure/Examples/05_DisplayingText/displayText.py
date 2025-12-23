# ruff:  noqa: F405, F403
# Example 3.5.1 Displaying Text via Snaps

import time

from snaps import *

display_message("hello world")
time.sleep(5)  # add a sleep so the window doesn't autoclose
