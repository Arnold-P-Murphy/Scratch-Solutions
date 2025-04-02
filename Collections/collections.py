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

stars = {
    'Sol': 0,
    'Alpha Centauri': 4.34,
    'Barnard': 3.25,
    'Wolf 359': 1.69,
}
# List of stars and their distances from Earth

stars = [
    {'name': 'Sol', 'distance': 0},
    {'name': 'Alpha Centauri', 'distance': 4.34},
    {'name': 'Barnard', 'distance': 3.25},
    {'name': 'Wolf 359', 'distance': 1.69},
]

print(stars[3]['name'])
# Output: Wolf 359

tectonic_plates_list = [
    {'name0': 'African', 'highest_peak': AFRICAN},
    {'name1': 'Antarctic', 'highest_peak': ANTARCTIC},
    {'name2': 'Australian', 'highest_peak': AUSTRALIAN},
    {'name3': 'Eurasian', 'highest_peak': EURASIAN},
    {'name4': 'North American', 'highest_peak': NORTH_AMERICAN},
    {'name5': 'Pacific', 'highest_peak': PACIFIC},
    {'name6': 'South American', 'highest_peak': SOUTH_AMERICAN}
]

print(tectonic_plates_list[5]['name'])
# Output: Pacific
#List of stars and their distances from Earth

#End-of-file (EOF)(\n)
