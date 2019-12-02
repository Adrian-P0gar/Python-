
def fib(nr):
    a, b, c = 0, 1, 1
    print("1." + str(a))
    print("2." + str(b))

    i = 3
    while i <= nr:
        print(str(i) + ". " + str(c))
        a = b
        b = c
        c = a + b
        i += 1


fib(100)
