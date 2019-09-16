file = open("team.txt", "r")



file.readline()
file.readline()

file.read(1)
print("second character: ", file.read(1))

print("Third Character: ", file.read(1))
file.readline()

file.close()