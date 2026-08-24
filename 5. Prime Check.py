def isPrime(num):
    if num < 2:
        return False
    
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

val = int(input("Enter a number to check prime: "))
print("Is Prime?:", isPrime(val))