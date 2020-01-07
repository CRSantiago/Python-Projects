#LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even, but returns the greater if one or both numbers are odd

#Comments are first attempts

def lesser_of_two_even(num1,num2):
  if (num1 % 2 == 0) and (num2 % 2 == 0):
    #if num1 < num2:
      #return num1
    #else: 
      #return num2
      return min(num1,num2)
  elif (num1 % 2 == 0) or (num2 % 2 ==0):
    #if num1 > num2:
      #return num1
    #else: 
      #return num1
    return max(num1,num2)
  
print(lesser_of_two_even(12,3))