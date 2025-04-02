"""
This module demonstrates a simple iteration over a list using the while loop.

Author: Arnold Murphy
Date: 2025-04-02
"""

i = 0


#creating lists
my_list = [1, 2, 3, 4, 5]
print(my_list)
#output: [1, 2, 3, 4, 5]

print(my_list[i])
#output: 1

print("this is a list in order")



while i < len(my_list):
    print(my_list[i])
    i += 1

# End-of-file (EOF)
