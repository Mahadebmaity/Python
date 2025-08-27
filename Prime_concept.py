# Now Discuss about prime number 
# All possible to write code to check and find prime number 
# with various logic or methods which is help in future  so that 
# ---------------------------------------------------------------------
# only check specific number 
import math # this built in library/module will be required when we use sqrt() method 

def is_prime(number):
    # Handle edge cases
    if number <= 1:
        return False

    # Check for divisibility from 2 up to the square root of the number
    for i in range(2, int(math.sqrt(number)) + 1): # dry run: number sqrt +1 , so loop run 2 to number_sqrt and each time if number sqrt getting a fraction value then it will be type conversion 
        if number % i == 0: # check out even number if found then return false and print number not prime 
            return False  # Found a divisor, so it's not prime
    
    # If no divisors found, it's prime
    return True

# Example usage:
# num = 17
# if is_prime(num):
#     print(f"{num} is a prime number.")
# else:
#     print(f"{num} is not a prime number.")

# --------------------------------------------------------------
# if I want to find out prime number in the given sequence 
# same code just add loop outside the calling function
# for num in range(1,20): # loop gives value to the function calling one by one 
#     if is_prime(num):
#         print(f"{num} is a prime number.")
#     else:
#         print(f"{num} is not a prime number.")
# ------------------------------------------------------------------
# with out using loop concept so how to write this code and solve this problem
# it's possible only RECURSION
# because without loop We can't find and calculate prime 
# specific numbers only 

def is_prime_recursive(num,divisor=2):
    if num <=1:
        return False
    # if divisor > int(math.sqrt(num)):  #this condition is beginner-friendly
    #     return True
    if divisor * divisor > num: # this condition is integer-based, faster, error-free pro use only
        return True 
    if num % divisor ==0:
        return False
    # return is_prime_recursive(num,divisor + 1) # Here is recursive call means function call itself

# num = int(input("Enter prime checking number: "))
# if is_prime_recursive(num):
#     print(f"{num} is a prime number!")
# else:
#     print(f"{num} is not a prime number!")

# ------------------------------------------------------------------
# if I want to find out prime number in the given sequence 
# I will be use loop because sequence of num 
# same code just  pass the value multiple time 
# for num in range(1,10):
#     if is_prime_recursive(num):
#         print(f"{num} is a prime number!")
#     else:
#         print(f"{num} is not a prime number!")
    
# ---------------------------------------------------------------------
# Program to find prime numbers in a given list using only loops

def prime_Checking(numbers):
    # for num in range(2,numbers+1):
        if numbers < 2:
            return False   # skip numbers less than 2
        
        is_prime = True   # assume number is prime
        
        # check divisibility using loop
        for i in range(2, int(numbers**0.5) + 1):
            if numbers % i == 0:
                is_prime = False
                break
        return is_prime

# for num in range(1,10):
#     if prime_Checking(num):
#         print(f"{num} is a prime.")
#     else:
#         print(f"{num} is not a prime.")

# ---------------------------------------------------------------
# Program to find prime numbers in a given list using only loops
def prime_check():
    numbers = [3, 8, 11, 25, 29, 50, 97, 100]

    prime_list = []

    for num in numbers:
        if num < 2:
            continue   # skip numbers less than 2
        is_prime = True   # assume number is prime
        
        # check divisibility using loop
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        
        if is_prime:
            prime_list.append(num)

    print("Given list:", numbers)
    print("Prime numbers in the list:", prime_list)

# prime_check()

# -----------------------------------------------------------------
# Now this is easiest way to solve this problem
from sympy import isprime

num = int(input("Enter a number: "))
if isprime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")

# --------------------------------------------------------------------

