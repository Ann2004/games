import math
import random


def lcm_two(a, b):  # НОК для двух чисел
    return a * b // math.gcd(a, b)


def lcm_three(a, b, c):  # НОК для трёх чисел
    return lcm_two(lcm_two(a, b), c)


def generate_numbers():  # генерация трех случайных чисел
    return [random.randint(1, 100) for _ in range(3)]


def main():
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print("Find the smallest common multiple of given numbers.")
    
    correct_answers = 0
    questions_count = 3
    
    for _ in range(questions_count):
        numbers = generate_numbers()
        correct_answer = lcm_three(*numbers)
        
        print(f"Question: {' '.join(map(str, numbers))}")
        user_answer = int(input("Your answer: "))
        
        if user_answer == correct_answer:
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