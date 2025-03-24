def run_game(game_module):
    """
    Запускает игру, используя переданный модуль игры.
    """
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print(game_module.GAME_RULES)
    
    correct_answers = 0
    questions_count = 3
    
    for _ in range(questions_count):
        question, correct_answer = game_module.generate_question_and_answer()
        print(f"Question: {question}")
        user_answer = input("Your answer: ")
        
        if user_answer == str(correct_answer):
            print("Correct!")
            correct_answers += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
    
    if correct_answers == questions_count:
        print(f"Congratulations, {name}!")

def main():
    """
    Основная функция для выбора и запуска игры.
    """
    print("Choose a game:")
    print("1. Find the smallest common multiple (LCM)")
    print("2. Find the missing number in a geometric progression")
    
    choice = input("Enter the number of the game you want to play: ")
    
    if choice == "1":
        from games import nok
        run_game(nok)
    elif choice == "2":
        from games import geometric_progression
        run_game(geometric_progression)
    else:
        print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()