def Multiply(n):
    for i in range(1,11):
        print(f"{n} * {i} = {n*i}")

n = int(input("Enter a number: "))
Multiply(n)


def multyTable(n,x):
    for i in range(1,x+1):
        print(f"{n} * {i} = {n*i}")

n = int(input("Enter a number: "))
x = int(input("Enter a range: "))
multyTable(n,x)