list1 = [ "A", "B", "C", "D", "E", "F", "G", "H", "I"]
for i in range(9):
    print(list1[i], end="   ")
    if (i + 1) % 3 == 0:
        print ()