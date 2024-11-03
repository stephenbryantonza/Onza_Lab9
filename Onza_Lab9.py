rows = int(input("Enter a number of rows to generate: "))
startnum = 1

for number in range(1, rows + 1):
    for number in range(number):
        print(startnum, end=' ')
        startnum += 1
    print()
