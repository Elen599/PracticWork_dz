from view import *
from model import *
from logger import logger

degree = user_input()

result = example_us(degree)
print_for_user(result)

logger(f'{degree} = {result}')