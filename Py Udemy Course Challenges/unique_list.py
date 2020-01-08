# Write a Python function that takes a list and returns a new list with unique elements of the first list.

# Sample List : [1,1,1,1,2,2,3,3,3,3,4,5]
# Unique List : [1, 2, 3, 4, 5]

def unique_list(lst):
  unq_list = []

  for el in lst:
    if el not in unq_list:
      unq_list.append(el)
  
  return unq_list

print(unique_list([1,1,1,1,2,2,3,3,3,3,4,5]))