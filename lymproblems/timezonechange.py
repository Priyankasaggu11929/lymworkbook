# Change the system's timezone to the same of SFO, USA

import os
import sys
from .utils import system, success, fail


def setup():
    "Setup timezonechange"
    pass  # Nothing to do.


def verify():
    "Verify timezonechange"

    SFOtimezone = "/usr/share/zoneinfo/US/Pacific"
    localtimezone = "/etc/localtime"

    if os.popen("zdump {}".format(localtimezone)).read().strip(
        localtimezone
    ) != os.popen("zdump {}".format(SFOtimezone)).read().strip(SFOtimezone):
        fail("Time zone not changed")
    success()
