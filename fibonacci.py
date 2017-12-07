def fibonacci(n):
    if type(n) != int or n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_elements = [0, 1]
        m = 0
        k = 1
        i = 0
        while i < n-2:
            p = m + k
            fib_elements.append(p)
            m = k
            k = p
            i += 1
        return fib_elements
