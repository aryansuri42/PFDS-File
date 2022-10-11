# gcd recursive function
def gcd(a, b):
    if b == 0:
        return abs(a)
    else:
        return gcd(b, a % b)


a = 12
b = 4
print(f"The gcd of 12 and 4 is: {gcd(a, b)}")


# power recursive program
def power(a, b):
    if b == 0:
        return 1
    elif b == 1:
        return a * 1
    else:
        return a * power(a, b - 1)


print(f"2 raise to power 3 is: {power(2, 3)}")
