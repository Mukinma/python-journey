"""
LASAGNA PREPARATION TIME CALCULATIONS
"""

EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 5

def bake_time_remaining(elapsed_bake_time):
    """
    Calculate the elapsed baking time

    :param elapsed_bake_time: int - the elapsed cooking time
    :return: int - total elapsed (in minutes) cooking time

    This function takes one ingerers representing the number of lasagna layers and
    calculates the total elapsed minutes spent cooking the lasagna
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time
    
def preparation_time_in_minutes(number_of_layers):
    """
    Calculate the preparation time

    :param number_of_layers: int - the number of layers in the lasagna.
    :return: int - total elapsed (in minutes) preparing time

    This function takes one ingerers representing the number of lasagna layers and
    calculates the total elapsed minutes spent preparing the lasagna
    """
    return number_of_layers * 2
    
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """
    Calculate the elapsed cooking time

    :param number_of_layers: int - the number of layers in the lasagna.
    :param elapsed_bake_time: int - the elapsed cooking time
    :return: int - total time elapsed (in minutes) preparing and cooking

    This function takes two ingerers representing the number of lasagna layers and the time 
    already spent baking and calculates the total elapsed minutes spent cooking the lasagna.
    """
    return (number_of_layers * 2) + elapsed_bake_time
   