import random
from Question import Question

br = "\n"


def run_quiz(questions):
    score = 0
    for question in questions:
        print(question.prompt)
        choice = input(question.choices+br)
        if choice == question.answer:
            score += 1
    print(f"You got {score}/{len(questions)} correct")


def get_quiz():
    prompts = random.sample(list(open("prompts.txt", "r")), 2)
    questions = []
    for line in prompts:
        q_a_split = line.split('-')
        questions.append(
            Question(q_a_split[0], q_a_split[1], q_a_split[2].strip('\n')))

    return questions


def main():
    while True:
        # Run quiz
        questions = get_quiz()
        run_quiz(questions)

        # Promp to play again
        play_again = input("Would you like to play again? Enter yes or no"+br)
        if play_again.lower()[0] == 'y':
            continue
        else:
            break


if __name__ == "__main__":
    main()
