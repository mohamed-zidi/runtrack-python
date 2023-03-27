numbers = []
i = 0
while i < 5:
    number = int(input("Entrez un nombre svp : "))
    numbers.append(number)
    i+=1

numbers.sort()

for number in numbers:
    print(number)