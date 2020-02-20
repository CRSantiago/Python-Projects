# Coin Flip program. User chooses heads or tails to determine score. 

# If user guesses correctly, their score is incremented. Else, computer score increments

from User import User
import random

def flip_coin():
    flip = random.randint(0,1)
    if flip == 0:
        return "heads"
    elif flip == 1:
        return "tails"

# prompt to see if user will continue or not
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

# Prompts for user name and assigns new User Object
user_input = input("Enter your name to play: ")
user = User(user_input)

# Scores
user_score = 0
comp_score = 0

while True:
    # Prompt with validation
    while True:
        prompt = input("Heads or Tails?\n")
        if prompt.lower()[0] not in ('h','t'):
            continue
        else:
            break
    
    # Test user prompt versus the return of coin flip
    if prompt.lower()[0] == flip_coin()[0]:
        user_score += 1
    else:
        comp_score += 1

    # Displays updated scores
    print(f'{user.name}: {user_score}\nComputer Score: {comp_score}')

    # While loop test
    if not reprompt():
        break