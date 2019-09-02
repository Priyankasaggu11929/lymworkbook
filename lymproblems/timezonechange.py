# Change the system's timezone to the same of SFO, USA

import os
import sys
import pytz
from datetime import datetime
from .utils import system, success, fail


def setup():
    "Setup timezonechange"
    pass  # Nothing to do.


def verify():
    "Verify timezonechange"

    if os.popen("date +%T").read().strip("\n") != str(
        datetime.now(pytz.timezone("US/Pacific")).strftime("%H:%M:%S")
    ):
        fail("Time zone not changed")
    success()
