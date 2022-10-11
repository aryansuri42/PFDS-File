def armstrong(n):
    num_check = n
    armstrongval = 0
    while n != 0:
        temp = n % 10
        n = n // 10
        armstrongval += temp ** 3
    if num_check == armstrongval:
        print(f"True {num_check} is an armstrong number")
    else:
        print(False)


def prime(n):
    count = 0
    if n > 1:
        for i in range(1, n + 1):
            if (n % i) == 0:
                count += 1
                continue
            else:
                continue
    if count > 2:
        print(f"{n} not a prime number")
    else:
        print(f"{n} a prime number")


armstrong(153)
prime(23)
