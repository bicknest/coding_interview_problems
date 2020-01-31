import random

def rand5():
    return random.randrange(1, 5)

def rand7():
    while True:
        roll1 = rand5()
        roll2 = rand5()

        outcome = (roll1 - 1) * 5 + (roll2 - 1) + 1

        if outcome < 22:
            return outcome % 7 + 1


