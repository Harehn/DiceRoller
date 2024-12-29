from random import randint
import re


def roll_dice(dice):
    return randint(1, int(dice))


# Output (number of dice, type of dice, modifier)
def parse(dice_string):
    if re.match('[0-9]+d[0-9]+([+-][0-9]+)', dice_string) is not None:
        a, _, b, c, d = re.split('([d+-])', dice_string)
        return a, b, c + d
    if re.match('[0-9]+d[0-9]+', dice_string) is not None:
        a, b = re.split('d', dice_string)
        return a, b, 0
    return -1, -1, -1


def evaluate(dice_string):
    num_dice, dice_type, modifier = parse(dice_string)
    if num_dice == -1:
        return 'Incorrect dice string'
    num_dice, dice_type, modifier = int(num_dice), int(dice_type), int(modifier)
    return sum([roll_dice(dice_type) for _ in range(num_dice)]) + modifier


if __name__ == '__main__':
    while True:
        value = input("Enter your dice:")
        print(value, parse(value))
        for i in range(5):
            print(evaluate(value))

