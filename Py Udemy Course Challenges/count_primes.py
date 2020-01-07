# COUNT PRIMES: Write a function that returns the number of prime numbers that exist up to and including a given number
# count_primes(100) --> 25

def count_primes(num):
  #check for 0 or 1 input
  if num < 2:
    return 0

  # 2 or greater

  #store prime numbers
  primes = [2]
  #counter going up to input num
  x = 3

  #xis going through every number up to input num
  while x <= num:
    #check if x is prime
    for y in range(3,x,2):
      if x % y == 0:
        x += 2
        break
    else:
      primes.append(x)
      x += 2
  print(primes)
  return len(primes)

print(count_primes(100))