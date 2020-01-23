# Advanced Numbers
print('Problem 1: Convert 1024 to binary and hexadecimal representation')
print(hex(1024))
print(bin(1024))

print('\nProblem 2: Round 5.23222 to two decimal places')
print(round(5.23222,2))

# Advanced Strings
print('\nProblem 3: Check if every letter in the string s is lower case')
s = 'hello how are you Mary, are you feeling okay?'
print(s)
print(s.islower())

print("\nProblem 4: How many times does the letter 'w' show up in the string below?")
s = 'twywywtwywbwhsjhwuwshshwuwwwjdjdid'
print(s)
print(s.count('w'))

# Advanced Sets
print('\nProblem 5: Find the elements in set1 that are not in set2:')
set1 = {2,3,1,5,6,8}
set2 = {3,1,7,5,6,8}
print(set1)
print(set2)
print(set1.difference(set2))

print('\nProblem 6: Find all elements that are in either set:')
print(set1)
print(set2)
print(set1.intersection(set2))

#Advanced Dictionaries
print('\nProblem 7: Create this dictionary: {0: 0, 1: 1, 2: 8, 3: 27, 4: 64} using a dictionary comprehension.')
print({i:i**3 for i in range(5)})

#Advanced Lists
print('\nProblem 8: Reverse the list below:')
list1 = [1,2,3,4]
print(list1)
list1.reverse()
print(list1)

print('\nProblem 9: Sort the list below:')
list2 = [3,4,2,5,1]
print(list2)
list2.sort()
print(list2)