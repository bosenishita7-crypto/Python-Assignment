def doSum(num):
    total = 0
    
    for digit in str(abs(num)):
        total += int(digit)
    return total

val = int(input("Enter number: "))
print("Sum of digits:", doSum(val))