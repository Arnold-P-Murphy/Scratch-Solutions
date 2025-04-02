"""
This module provides basic collections dictionary operations.
"""
# Nearest stars to Earth
STAR_1 = 'Sol'
STAR_2 = 'Alpha Centauri'
STAR_3 = 'Barnard'
STAR_4 = 'Wolf 359'

# Highest peak on each tectonic plate
AFRICAN = 'Kilimanjaro'
ANTARCTIC = 'Vinson'
AUSTRALIAN = 'Puncak Jaya'
EURASIAN = 'Everest'
NORTH_AMERICAN = 'Denali'
PACIFIC = 'Mauna Kea'
SOUTH_AMERICAN = 'Aconcagua'

# Dictionary of tectonic plates and their respective highest peaks


tectonic_plates = {
    'African': AFRICAN,
    'Antarctic': ANTARCTIC,
    'Australian': AUSTRALIAN,
    'Eurasian': EURASIAN,
    'North American': NORTH_AMERICAN,
    'Pacific': PACIFIC,
    'South American': SOUTH_AMERICAN
}
# Dictionary of stars and their distances from Earth

stars_dict = {
    'Sol': 0,
    'Alpha Centauri': 4.34,
    'Barnard': 3.25,
    'Wolf 359': 1.69,
}
# List of stars and their distances from Earth

stars = [
    {'name0': 'Sol', 'distance': 0},
    {'name1': 'Alpha Centauri', 'distance': 4.34},
    {'name2': 'Barnard', 'distance': 3.25},
    {'name3': 'Wolf 359', 'distance': 1.69},
]

print(stars[3]['name3'])
print(stars_dict['name3']['distance'])
# Output: 1.69
# Output: Wolf 359

print(tectonic_plates['Pacific'])

# Output: Pacific
#List of stars and their distances from Earth

#End-of-file (EOF)(\n)
