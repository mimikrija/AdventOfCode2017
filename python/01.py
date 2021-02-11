# Day 1: Inverse Captcha

from santas_little_helpers import *

digits = list(map(int, get_input('inputs/01')[0]))

# add digit if it matches the next one
part_1 = sum(digit for digit, next_digit in zip(digits, digits[1:] + [digits[0]]) if digit == next_digit)

# add digit if it matches the one half way in the list 
# it is enough to compare top to bottom half of the list and multiply result by 2
part_2 = 2*sum(digit for digit, next_digit in zip(digits, digits[len(digits)//2:] + [digits[0]]) if digit == next_digit)

print_solutions(part_1, part_2)
