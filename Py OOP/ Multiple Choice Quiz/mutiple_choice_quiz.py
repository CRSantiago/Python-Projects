from Question import Question

question_prompts = [
  "Which is not an element?\n (a) Fire\n (b) Earth\n (c) Steel\n (d) Air\n\n",
  "Which is not a Game of Thrones Book title?\n (a) Clash of Kings\n (b) Feast of Crows\n (c) Storm of Swords\n (d) Dawn of Winter\n\n",
  "What anime doesn't involve demons?\n (a) Naruto\n (b) Inuyasha\n (c) Demon Slayer\n (d) Sword Art\n\n" 
]

questions = [
  Question(question_prompts[0], "c"),
  Question(question_prompts[1], "d"),
  Question(question_prompts[2],"d")
]

def run_test(questions):
  score = 0
  for question in questions:
    answer = input(question.prompt)
    if answer == question.answer:
      score += 1
  print("You got " + str(score) + "/" + str(len(questions)) + " correct")

run_test(questions)