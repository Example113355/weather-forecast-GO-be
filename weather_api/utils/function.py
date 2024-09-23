import random

def get_random_code():
    return ''.join([str(random.randint(0, 9)) for _ in range(6)])
