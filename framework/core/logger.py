"""
SMIP Logging Framework
"""

from datetime import datetime


def _timestamp():

    return datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )


def banner(title):

    print()

    print("=" * 80)

    print(title)

    print("=" * 80)


def line():

    print("-" * 80)


def info(message):

    print(
        f"[{_timestamp()}] INFO     {message}"
    )


def success(message):

    print(
        f"[{_timestamp()}] SUCCESS  {message}"
    )


def warning(message):

    print(
        f"[{_timestamp()}] WARNING  {message}"
    )


def error(message):

    print(
        f"[{_timestamp()}] ERROR    {message}"
    )