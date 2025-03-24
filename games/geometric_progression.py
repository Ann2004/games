import random

GAME_RULES = "What number is missing in the progression?"

def generate_geometric_sequence(start, multiplier, length):
    """
    Генерирует геометрическую прогрессию.
    """
    return [start * (multiplier ** i) for i in range(length)]

def hide_element(sequence, index):
    """
    Скрывает элемент в последовательности, заменяя его на '..'.
    """
    sequence[index] = ".."
    return sequence

def generate_question_and_answer():
    """
    Генерирует вопрос и правильный ответ для игры.
    """
    start = random.randint(1, 5)
    multiplier = random.randint(2, 5)
    length = random.randint(5, 10)
    
    sequence = generate_geometric_sequence(start, multiplier, length)
    
    hidden_index = random.randint(0, length - 1)
    correct_answer = sequence[hidden_index]
    
    question_sequence = hide_element(sequence.copy(), hidden_index)
    question = " ".join(map(str, question_sequence))
    
    return question, correct_answer