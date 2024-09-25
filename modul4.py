i = 1
while i < 9:
    print(i)
    if i == 4:
        break
    i += 1


for x in "animal":
    print(x)


number = ["2", "3", "4", "5", "6", "7", "8", "9"]
for x in number:
    print(x)


numbers = int(input("how many loops: "))
for x in range(numbers):
    print(x)


first = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
second = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for x in first:
    for y in second:
        print(f"{x} * {y} = {x * y}")