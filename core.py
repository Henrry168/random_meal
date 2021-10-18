import random


def clone(self):
    result = []
    for i in range(1000):
        for x in self:
            result.append(x)

    return result


def shuffle(lis):
    result = []
    while lis:
        p = random.randrange(0, len(lis))
        result.append(lis[p])
        lis.pop(p)
    return result
