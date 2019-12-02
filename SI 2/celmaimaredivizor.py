def gcd_recursive(a, b):

    if b == 0:
        return a
    else:
        return gcd_recursive(b, a % b)


#x = input("xxx")
#c = input ( "bbb")
a = int(input("Ce numar"))
b = int(input("Ce numar 2: "))
print(gcd_recursive(a,b))