import random


def lotto_numbers(range_min=1, range_max=49):
    """
    Picks 6 random numbers in range 1-49
    """
    number_list = [i for i in range(range_min, range_max + 1)]
    random.shuffle(number_list)
    return sorted(number_list[:6])


print(lotto_numbers(1, 49))
