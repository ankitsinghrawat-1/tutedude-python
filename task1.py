def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n-1)

num = int(input("enter a number: "))
fact = factorial(num)
print("Factorial of",num,"is",fact)