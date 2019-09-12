import math

from friend import Friend, Intention


f = Friend()


@f.skill
def add(first: int, last: int) -> int:
    return first + last


@f.skill
def factorial(n: int) -> int:
    return math.factorial(n)


@f.skill
def bmi(weight: float, height: float) -> float:
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


if __name__ == '__main__':
    while True:
        intention, params = f.say()
        f.get_answer(input(f'{to_nl(intention, params)} >> '))
