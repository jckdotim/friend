from copy import deepcopy

from friend import Intention
from app import f


def test_friend():
    test_f = deepcopy(f)
    assert test_f.say()[0] == Intention.ASK_FUNCTION

    test_f.get_answer('bmi')
    assert test_f.say()[0] == Intention.ASK_PARAMETER
    assert test_f.say()[1][0] == 'weight'

    test_f.get_answer('70')
    assert test_f.say()[0] == Intention.ASK_PARAMETER
    assert test_f.say()[1][0] == 'height'

    test_f.get_answer('170')
    assert test_f.say()[0] == Intention.ANSWER
