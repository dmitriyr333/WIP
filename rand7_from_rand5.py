from random import randint

def rand5():
    return randint(1,5)

def rand7():
    r = rand5() + (rand5() - 1) * 5 # [1...5] + [0 5 10 15 20]
    return (r % 7) + 1 if r < 21 else rand7()

print rand7()