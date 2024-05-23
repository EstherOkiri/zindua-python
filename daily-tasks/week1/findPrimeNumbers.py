
#exclude 0 and 1
def find_primes(testNum):
    for n in range(testNum):
        if (n > 1):
            if (n / n == 1) & (n / 1 == n):
                print(f"{n} is a prime number")
            else : 
                print(f"{n} is not a prime number")
        else:
            print(f"Prime number cannot be less than 0")


testNum = int(input("Enter a number : "))
find_primes(testNum)
        
