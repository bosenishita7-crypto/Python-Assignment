def factorial(n):
    if n < 0:
        return "Please enter a positive number"
    
    ans = 1
    for i in range(1, n + 1):
        ans = ans * i
    return ans

num = int(input("Enter number: "))
print("Factorial is:", factorial(num))
