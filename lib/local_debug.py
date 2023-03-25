"""
Module to help with mocking/bypassing
RaspberryPi specific code to enable for
debugging on a Mac or Windows host.
"""

from packaging import version
import platform
import sys

REQUIRED_PYTHON_VERSION = "3.5"
IS_LINUX = 'linux' in sys.platform
DETECTED_CPU = platform.machine()
IS_PI = True


def validate_python_version():
    """
    Checks to make sure that the correct version of Python is being used.

    Raises:
        Exception -- If the  version of Python is not new enough.
    """
    python_version = platform.python_version()
    if version.parse(python_version) < version.parse(REQUIRED_PYTHON_VERSION):
        error_text = (
            f"Requires Python {REQUIRED_PYTHON_VERSION}, "
            f"got {python_version}"
        )
        print(error_text)
        raise Exception(error_text)


def is_debug():
    """
    returns True if this should be run as a local debug (Mac or Windows).
    """

    return sys.platform in ["win32", "darwin"] or (IS_LINUX and not IS_PI)


validate_python_version()
