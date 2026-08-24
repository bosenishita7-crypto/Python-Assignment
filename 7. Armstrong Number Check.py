def checkArmstrong(num):
    temp = str(num)
    digits = len(temp)
    total = 0
    
    for ch in temp:
        total += int(ch) ** digits
        
    return total == num

val = int(input("Enter a number: "))
if checkArmstrong(val):
    print(val, "is an Armstrong number")
else:
    print(val, "is not an Armstrong number")
