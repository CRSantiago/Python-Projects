from Calculator import Calculator

def artithmetic_prompt():
    while True:
        try:
            answer = int(input("Which arithmetic function would you like to execute on the numbers you provided?\n 1. Addition \n 2. Subtraction \n 3. Multiplication \n 4. Division \n"))
        except:
            print("Please select option 1,2,3 or 4 from the menu.")
            continue
        else:
            break
    return answer

def reprompt():
  checked = False
  while not checked:
    continue_prompt = input("Do you want to continue? \nEnter Yes or No\n")
    if continue_prompt.lower()[0] == 'y':
      checked = True
    elif continue_prompt.lower()[0] == 'n':
      checked = False
      break
    else:
      continue
  return checked

def main():
    while True:

        numbers_list = []
        while True:
            number_prompt = float(input("Enter a number into the calculator: \nEnter 0.0 to move to arithmetic functions\n"))
            if number_prompt == 0.0:
                break
            numbers_list.append(number_prompt)
            print("\n")

        calc = Calculator(numbers_list)
        prompt_answer = artithmetic_prompt()
        if prompt_answer == 1:
            result = calc.add()
            print("The result was: ", result)
        elif prompt_answer == 2:
            result = calc.subtract()
            print("The result was: ", result)
        elif prompt_answer == 3:
            result = calc.multiply()
            print("The result was: ", result)
        elif prompt_answer == 4:
            result = calc.division()
            print("The result was: ", result)

        if not reprompt():
            break
    
if __name__ == "__main__":
    main()