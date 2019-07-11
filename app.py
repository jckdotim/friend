import math
from copy import deepcopy

from friend import Friend, Intention


f = Friend()


@f.skill
def add(first: int, last: int) -> int:
    return first + last


@f.skill
def factorial(n: int) -> int:
    return math.factorial(n)


@f.skill
def bmi(weight: int, height: int) -> float:
    return weight / (height * 0.01) ** 2


@f.skill
def reverse(value: bool):
    return not value


def to_nl(intention, params):
    return {
        Intention.ASK_FUNCTION: 'What do you want?',
        Intention.ASK_PARAMETER: 'Please tell me about {0}',
        Intention.ANSWER: 'The result is {0}',
    }[intention].format(*params)


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


if __name__ == '__main__':
    while True:
        intention, params = f.say()
        f.get_answer(input(f'{to_nl(intention, params)} >> '))
