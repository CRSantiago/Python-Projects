import random

# Create a generator that generates the squares of numbers up to some number N.
def gen_square(n):
    
    for i in range(n):
        yield i**2

for x in gen_square(10):
    print(x)

# Create a generator that yields "n" random numbers between a low and high number 
# (that are inputs).

def rand_num(low,high,n):

    for i in range(n):
        yield random.randint(low,high)

for num in rand_num(1,10,22):
    print(num)

# Use the iter() function to convert the string below into an iterator:
s = 'hello'
s_iter = iter(s)
print(next(s_iter))