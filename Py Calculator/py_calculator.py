def prompt():
  while True:
    try:
      num1 = float(input("Enter the first number: "))
    except ValueError:
      print("Please enter a valid number")
      continue
    else:
      break

  while True:
    try:
      num2 = float(input("Enter second number: "))
    except ValueError:
      print("Please enter a valid number")
      continue
    else:
      break

  while True:
    try:
      answer = int(input("Which arithmetic function would you like to execute?\n 1. Addition \n 2. Subtraction \n 3. Multiplication \n 4. Division \n"))
    except:
      print("Please select option 1,2,3 or 4 from the menu.")
      continue
    else:
      break
  return num1,num2,answer


def addition(num1,num2):
  return num1 + num2

def subtraction(num1, num2):
  return num1 - num2

def multiplication(num1,num2):
  return num1 * num2

def division(num1,num2):
  return num1/num2

def return_data():
  num1, num2, prompt_result = prompt()
  return num1, num2, prompt_result

def reprompt():
  checked = False
  while checked == False:
    continue_prompt = input("Do you want to continue? \n Enter Yes or No\n")
    if continue_prompt.lower()[0] == 'y':
      checked = True
    elif continue_prompt.lower()[0] == 'n':
      checked = False
      break
    else:
      continue
  return checked

while True:
  num1, num2, prompt_result = return_data()
  if prompt_result == 1:
    result = addition(num1,num2)
    print("The result was: ", result)
  elif prompt_result == 2:
    result = subtraction(num1,num2)
    print("The result was: ", result)
  elif prompt_result == 3:
    result = multiplication(num1,num2)
    print("The result was: ", result)
  elif prompt_result == 4:
    result = division(num1,num2)
    print("The result was: ", result)
  else:
    print("Invalid entry")
    
  if not reprompt():
    break