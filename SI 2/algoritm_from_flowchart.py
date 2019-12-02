
numbers =[]
print(numbers)
x = 0

numbers_cerere = int(input("Cate elemente are lista?"))
i= 1

while (x < numbers_cerere):
    g = int(input("Elementul " + str (x) + ": "))
    numbers.append(g)
    x = x+1

n = int(len(numbers))   
while (i <= n):

    j= 0
    while j<= n - 2:
        while numbers[j] > numbers[j + 1]:
            temp = numbers[j +1]
            numbers[j +1] =numbers[j]
            numbers[j] = temp

        j = j +1
    
    i = i +1

print(numbers)