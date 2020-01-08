# Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.

# Sample String : 'Hello Mr. Rogers, how are you this fine Tuesday?'
# Expected Output : 
# No. of Upper case characters : 4
# No. of Lower case Characters : 33

def up_low(s):
  count_d = {'upper':0,'lower':0}
  for char in s:
    if char.isupper():
      count_d['upper'] += 1
    elif char.islower():
      count_d['lower'] += 1
  print("Original String : ", s)
  print("No. of Upper case characters : {}".format(count_d['upper']))
  print("No. of Lower case characters : {}".format(count_d['lower']))

up_low("Hello Mr. Rogers, how are you this fine Tuesday?")
