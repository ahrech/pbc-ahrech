def numbers_pairs(*number):
    pairs = set()

    if len(number) < 2:
        return pairs

    for i in range(len(number)):
        a = number[i]
        for j in range(i + 1, len(number)):
            b = number[j]
            if a + b == 10:
                pairs.add((min(a, b), max(a, b)))
    return pairs