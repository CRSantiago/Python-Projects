# Write a Python function that checks whether a passed in string is palindrome or not.

# Note: A palindrome is word, phrase, or sequence that reads the same backward as forward, e.g., madam or nurses run.

# Comments are first attempt

def palindrome(s):
  # new_str = ''
  # for char in s[::-1]:
  #   new_str += char
  # if new_str == s:
  #   return True
  # else: 
  #   return False

  pal_s = s.replace(' ','')
  return s == pal_s[::-1]

print(palindrome('madam'))