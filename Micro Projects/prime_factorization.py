# Prime Factorization - Have the user enter a number and find all Prime Factors (if there are any) and display them.

import math

def find_prime_factors(n):
    while n%2==0:
        yield 2
        n/=2
        
    for i in range(3,int(math.sqrt(n))+1,2):

        while n%i==0:
            yield i
            n/=i

    if n>2:
        yield n

user_input = int(input("Enter a number:\n"))
print("\nLet's see what are prime factors of the number you entered.")
for factor in find_prime_factors(user_input):
    print(factor)
