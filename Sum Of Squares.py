def Sum(n):
    return n*(n+1)*(2*n+1)//6
n = int(input("Enter the number:"))
print(f"The sum of first {n} natural numbers is {Sum(n)}")