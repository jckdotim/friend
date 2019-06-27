import math

from friend import Friend


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


if __name__ == '__main__':
    while True:
        f.get_answer(input(f'{f.say()} >> '))
