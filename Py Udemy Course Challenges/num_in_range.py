# Write a function that checks whether a number is in a given range (inclusive of high and low)

def ran_check(num,low,high):
  if low <= num <= high:
    print("{} is in the range between {} and {}".format(num,low,high))
  else:
    print('The number is outside the range')

def ran_bool(num,low,high):
  return low < num <= high

ran_check(5,2,7)
print(ran_bool(3,1,10))