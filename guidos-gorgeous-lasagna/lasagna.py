# TODO: define the 'EXPECTED_BAKE_TIME' constant
EXPECTED_BAKE_TIME=40

PREPARATION_TIME=2

# TODO: define the 'bake_time_remaining()' function
def bake_time_remaining(baketime):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int baking time already elapsed.
    :return: int remaining bake time derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.

    """
    remaining_bake_time=EXPECTED_BAKE_TIME-baketime
    return remaining_bake_time

# TODO: define the 'preparation_time_in_minutes()' function
def preparation_time_in_minutes(layers):
    """Gives the preparation time"""
    return layers*PREPARATION_TIME

# TODO: define the 'elapsed_time_in_minutes()' function
def elapsed_time_in_minutes(layers,time):
    """Gives the time taken"""
    return (layers * PREPARATION_TIME)+time
    
