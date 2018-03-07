import itertools


def list_fibonacci(limit):
    nums = []
    current, nxt = 0, 1

    for _ in range(0, limit):
        current, nxt = nxt, nxt + current
        nums.append(current)

    return nums


def generator_fibonacci():
    current, nxt = 0, 1

    while True:
        current, nxt = nxt, nxt + current
        yield current


print(list_fibonacci(100)[:5])
# ERROR: print(generator_fibonacci()[:5])

print(list(itertools.islice(generator_fibonacci(), 5)))
