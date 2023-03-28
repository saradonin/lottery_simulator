import random


def lotto_numbers(range_min=1, range_max=49):
    """
    Picks 6 random numbers in range 1-49
    """
    number_list = [i for i in range(range_min, range_max + 1)]
    random.shuffle(number_list)
    return sorted(number_list[:6])


def get_player_numbers():
    """
    Asks user to enter 6 unique numbers from 1 to 49 and returns sorted list of numbers.
    """
    print("Enter numbers from 1 to 49")
    player_numbers = [int(input()) for i in range(6)]  # temp generator
    return sorted(player_numbers)


print(get_player_numbers())
