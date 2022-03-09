def gcd(a, b):
    # Euclidean Algorithm
    # input: int a, int b
    # output: max common divisor of a and b
    if a < b:
        temp = a
        a = b
        b = temp
    while b != 0:
        a, b = b, a % b
    if b == 0:
        return abs(a)
