n = int(input("Enter number of rows: "))
for i in range(n):
    print(" " * (n - i - 1) + "* " * n)