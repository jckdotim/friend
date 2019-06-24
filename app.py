from friend import Friend


f = Friend()


@f.skill
def add(first: int, last: int):
    return first + last


if __name__ == '__main__':
    while True:
        f.get_answer(input(f'{f.say()} >> '))
