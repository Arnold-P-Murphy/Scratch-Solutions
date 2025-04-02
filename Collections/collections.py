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

print('Pacific:', tectonic_plates['Pacific'])


stars_dict = {
    'Sol': 0,
    'Alpha Centauri': 4.34,
    'Barnard': 3.25,
    'Wolf 359': 1.69,
}
# List of stars and their distances from Earth
stars_list = [
    ['Sol', 0],
    ['Alpha Centauri', 4.34],
    ['Barnard', 3.25],
    ['Wolf 359', 1.69],
]

print('Sol:', stars_dict['Sol'])
print(stars_list[3])
# Dictionary of stars and their distances from Earth
#End-of-file (EOF)(\n)
