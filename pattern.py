print("Number Pattern")
row = 5

for i in range(1, row + 1):
    for j in range(1, i + 1):
        print(j, end=' ')
    print("")

for i in range(row - 1, 0, -1):
    for j in range(1, i + 1):
        print(j, end=' ')
    print("")