"""A one-function package for demonstrating CI and branch protection."""


def scheduled_hour(hhmm: int) -> int:
    """Return the hour of a time written as hhmm (e.g. 945 -> 9, 1730 -> 17)."""
    return hhmm // 100
