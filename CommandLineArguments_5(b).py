from sys import argv

n = len(argv)

large = argv[1]
if n <= 4:
    for i in range(1, n):
        if argv[i] > large:
            large = argv[i]
    print("Biggest number is = ", large)
else:
    print("Enter only 3 numbers")
