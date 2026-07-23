def Check(n):
    if n&1 ==0:
        print(f"{n} is Even")
    else:
        print(f"{n} is Odd")

n = int(input("Enter a number: "))
Check(n)