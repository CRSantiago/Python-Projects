#OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name

def old_mcdonald(name):
  #return name[:4].upper() + name[4:]
  if len(name) > 3:
      return name[:3].capitalize() + name[3:].capitalize()
  else:
      return 'Name is too short!'

print(old_mcdonald('Macdonald'))