# Assign sudo-user/superuser privileges to a current user "lym".

import os
import sys
from .utils import system, success, fail, find_path_data


def setup():
    "Setup problemname"
    pass  # Nothing to do.


def verify():
    "Verify problemname"
    user = "lym"

    if user not in os.popen("getent group sudo").read():
        fail("User {} is not allowed to run sudo on test-server.".format(user))
    success()
