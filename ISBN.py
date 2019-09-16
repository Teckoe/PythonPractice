ISBN = int(input("Please Enter the first 12 ISBN digits: "))
digit13 = int(input("Please Enter the last digit: "))

if ISBN % 2 == 0:
    print(ISBN + digit13)
else:
    print(ISBN, digit13 * 3)


print((ISBN, digit13) % 10)

