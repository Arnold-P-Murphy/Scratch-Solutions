"""
This module demonstrates a working with strings to find values.

Author: Arnold Murphy
Date: 2025-04-02
"""

miles = input("Enter the number of miles: ")
# Convert miles to kilometers

print(miles + " miles is equal to " + str(float(miles) * 1.60934) + " kilometers.")
# Convert miles to kilometers



kilometers = float(miles) * 1.60934 # 1.60934
# Print the result
print(miles + " miles is equal to " + str(kilometers) + " kilometers.")
# Print the result

kilometers = input("Enter the number of kilometers: ")
# Convert kilometers to miles
print(kilometers + " kilometers is equal to " + str(float(kilometers) / 1.60934) + " miles.")
# Convert kilometers to miles


miles_float = float(miles)
# Convert miles to kilometers
kilometers = miles_float * 1.60934
print("that value in kilometers is: ")
print(kilometers)

# Print the result


# End-of-file (EOF)
