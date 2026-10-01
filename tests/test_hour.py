import pytest

from hhmm_demo import scheduled_hour


@pytest.mark.parametrize(("hhmm", "hour"), [(5, 0), (945, 9), (1730, 17), (2359, 23)])
def test_scheduled_hour(hhmm: int, hour: int) -> None:
    assert scheduled_hour(hhmm) == hour
