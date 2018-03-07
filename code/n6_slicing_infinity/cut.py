def list_fibonacci(limit):
    nums = []
    current, nxt = 0, 1

    while current < limit:
        current, nxt = nxt, nxt + current
        nums.append(current)
    
    return nums



def generator_fibonacci():
    current, nxt = 0, 1

    #while current < 100000:
    while True:
        current, nxt = nxt, nxt + current
        yield current



print(list_fibonacci(100)[:5])
# ERROR: print(generator_fibonacci()[:5])

import itertools
print(list(itertools.islice(generator_fibonacci(), 5)))