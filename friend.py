import enum
from distutils.util import strtobool
from inspect import signature


class Intention(enum.Enum):
    ANSWER = 0
    ASK_FUNCTION = 1
    ASK_PARAMETER = 2


class Friend:
    def __init__(self):
        self.skills = []
        self.converters = {
            int: lambda v: int(v),
            bool: lambda v: strtobool(v),
        }
        self.memories = []

    def skill(self, func):
        self.skills.append(func)

    def say(self):
        if (len(self.memories) > 0 and
           len(self.memories) == len(
               signature(self.memories[0]).parameters.keys()
           ) + 1):
            result = self.memories[0](*self.memories[1:])
            self.memories = []
            return Intention.ANSWER, [result]
        elif not len(self.memories):
            return Intention.ASK_FUNCTION, []
        else:
            return Intention.ASK_PARAMETER, [self.get_current_parameter()[0]]

    def get_current_parameter(self):
        return list(
            signature(self.memories[0]).parameters.items()
        )[len(self.memories)-1]

    def get_answer(self, answer):
        if not len(self.memories):
            for skill in self.skills:
                if skill.__name__ in answer:
                    self.memories.append(skill)
        else:
            anno = self.get_current_parameter()[1].annotation
            if anno and anno in self.converters:
                self.memories.append(self.converters[anno](answer))
            elif anno:
                self.memories.append(anno(answer))
            else:
                self.memories.append(answer)
