def add(num_1: float, num_2: float) -> float:
    return num_1 + num_2

def subtract(num_1: float, num_2: float) -> float:
    return num_1 - num_2 

def multiply(num_1: float, num_2: float) -> float:
    return num_1 * num_2

def divide(num_1: float, num_2: float) -> float:
    if num_2 == 0:
        raise ValueError("Cannot divide by zero.")

    return num_1 / num_2
