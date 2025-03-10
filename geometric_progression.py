import random


def generate_geometric_sequence(start, multiplier, length):
    return [start * (multiplier ** i) for i in range(length)]


def hide_element(sequence, index):  # Скрывает элемент в последовательности, заменяя его на '..'
    sequence[index] = ".."
    return sequence


def main():
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print("What number is missing in the progression?")
    
    correct_answers = 0
    questions_count = 3
    
    for _ in range(questions_count):
        start = random.randint(1, 5)
        multiplier = random.randint(2, 5)
        length = random.randint(5, 10)
        
        sequence = generate_geometric_sequence(start, multiplier, length)
        
        hidden_index = random.randint(0, length - 1)  # Выбор случайного элемента для скрытия
        correct_answer = sequence[hidden_index]
        
        question_sequence = hide_element(sequence.copy(), hidden_index)  # Выбор случайного элемента для скрытия
        
        print("Question:", " ".join(map(str, question_sequence)))
        user_answer = input("Your answer: ")
        
        if user_answer.isdigit() and int(user_answer) == correct_answer:  # Проверка ответа
            print("Correct!")
            correct_answers += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
    
    if correct_answers == questions_count:
        print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()