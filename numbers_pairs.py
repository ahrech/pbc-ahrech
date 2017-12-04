# Duplicated pairs are not removed from the output yet :)

def numbers_pairs(*number):
    if len(number) < 2:
        print "There must be at least 2 numbers"
        return
    for i in range(len(number)):
        a = number[i]
        for j in range(i + 1, len(number)):
            b = number[j]
            if a + b == 10:
                print str(a) + '+' + str(b)
