import math
import random

GAME_RULES = "Find the smallest common multiple of given numbers."

def lcm_two(a, b):
    """
    Вычисляет наименьшее общее кратное (НОК) для двух чисел.
    """
    return a * b // math.gcd(a, b)

def lcm_three(a, b, c):
    """
    Вычисляет НОК для трёх чисел.
    """
    return lcm_two(lcm_two(a, b), c)

def generate_question_and_answer():
    """
    Генерирует вопрос и правильный ответ для игры.
    """
    numbers = [random.randint(1, 100) for _ in range(3)]
    question = " ".join(map(str, numbers))
    correct_answer = lcm_three(*numbers)
    return question, correct_answer