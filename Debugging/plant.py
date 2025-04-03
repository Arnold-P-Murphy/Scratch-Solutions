"""
This module demonstrates a simple iteration over a list of fruits using the for loop.

Author: Arnold Murphy
Date: 2025-04-02
"""
def plant_recommendation(care):
    """
    Recommends a plant based on the level of care required.

    Args:
        care (str): The level of care ('low', 'medium', 'high').

    Returns:
        None
    """
    if care == 'low':
        print('aloe')
    elif care == 'medium':
        print('pothos')
    elif care == 'high':
        print('orchid')

plant_recommendation('low')
plant_recommendation('medium')
plant_recommendation('high')

# End-of-file (EOF)
