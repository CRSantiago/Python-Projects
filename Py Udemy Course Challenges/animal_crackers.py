#ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter

#Comments are first attempts

def animal_crackers(text):
  spl_text = text.split()
  return spl_text[0][0] is spl_text[1][0]
  
print(animal_crackers("Large Elephant"))