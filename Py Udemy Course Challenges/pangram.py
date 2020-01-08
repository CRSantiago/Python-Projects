# Write a Python function to check whether a string is pangram or not.

# Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
# For example : "The quick brown fox jumps over the lazy dog"

# Comments are first attempt

import string

def pangram(str1,alphabet=string.ascii_lowercase):
  # str_list = []
  # for char in str1.lower():
  #   if char == ' ':
  #     continue
  #   elif char in str_list:
  #     continue
  #   else:
  #     str_list.append(char)
  # return len(str_list) == len(alphabet)

  alphaset = set(alphabet)  
  return alphaset <= set(str1.lower())

print(pangram("The quick brown fox jumps over the lazy dog"))