import sys
import os
import datetime
sys.path.append(os.path.abspath("./Code/src/score"))
from common_scoring import next_saturday


# Just an example of a unit test against
# a utility function common_scoring.next_saturday
def test_next_saturday():
    ethalonSaturday = datetime.date.today()
    while ethalonSaturday.strftime('%a') != 'Sat':
        ethalonSaturday += datetime.timedelta(1)
    ethalonSaturday += datetime.timedelta(7)
    saturday = next_saturday()
    assert ethalonSaturday.strftime("%Y-%m-%d") == saturday
