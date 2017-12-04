def fibonacci(n):
    if n <= 0:
        print 'The argument must be positive'
    elif n == 1:
        print 0
    elif n == 2:
        print 0
        print 1
    else:
        print 0
        print 1
        m = 0
        k = 1
        i = 0
        while i < n-2:
            p = m + k
            print p
            m = k
            k = p
            i += 1
