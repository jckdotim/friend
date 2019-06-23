from inspect import signature


class Friend:
    def __init__(self):
        self.skills = []
        self.memories = []
        self.cursor = 0

    def skill(self, func):
        self.skills.append(func)

    def say(self):
        if (len(self.memories) > 0 and
           len(self.memories) == len(
               signature(self.memories[0]).parameters.keys()
           ) + 1):
            result = self.memories[0](*self.memories[1:])
            self.memories = []
            return result
        elif not len(self.memories):
            return 'What do you want?'
        else:
            return f'Please tell me about {self.get_current_parameter()[0]}.'

    def get_current_parameter(self):
        return list(
            signature(self.memories[0]).parameters.items()
        )[len(self.memories)-1]

    def get_answer(self, answer):
        if not len(self.memories):
            for skill in self.skills:
                if skill.__name__ == answer:
                    self.memories.append(skill)
        else:
            if(self.get_current_parameter()[1].annotation):
                self.memories.append(
                    self.get_current_parameter()[1].annotation(answer)
                )
            else:
                self.memories.append(answer)


f = Friend()

def add(first: int, last: int):
    return first + last

f.skills.append(add)
