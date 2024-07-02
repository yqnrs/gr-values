n = int(input("what number in the fibonacci's sequence are you trying to find?"))

def fib(n):

    if n < 0:
        print('not a valid number')

    elif n == 0:
        return 0

    elif n == 1 or n == 2:
        return 1

    else:
        return fib(n - 1) + fib(n - 2)

result = fib(n)
if n % 10 == 1 and n != 11:
    print(f" the {n}st number for the fibonacci's sequence is {result}")

elif n % 10 == 2 and n != 12:
    print(f" the {n}nd number for the fibonacci's sequence is {result}")

elif n % 10 == 3 and n != 13:
    print(f" the {n}rd number for the fibonacci's sequence is {result}")

else:
    print(f" the {n}th number for the fibonacci's sequence is {result}")


