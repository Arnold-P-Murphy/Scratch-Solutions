
"""
This module demonstrates working with input and output.

Author: Arnold Murphy
Date: 2025-04-02
"""

# Open the input and output files
infile = open(r'C:\Users\ArnoldMurphy\OneDrive - PQA\Development\Python Pre-requisite course 02\Ex_Files_Programming_Foundations_2023\Ex_Files_Programming_Foundations_2023\Scratch Solutions\Intro_input_and_output\values.txt', 'rt')
outfile = open(r'C:\Users\ArnoldMurphy\OneDrive - PQA\Development\Python Pre-requisite course 02\Ex_Files_Programming_Foundations_2023\Ex_Files_Programming_Foundations_2023\Scratch Solutions\Intro_input_and_output\values_totaled.txt', 'wt')

print('Processing input')
sum = 0

# Process each line in the input file
for line in infile:
    line = line.strip()  # Remove leading and trailing whitespace
    if line:  # Check if the line is not empty
        sum += int(line)
        print(line, file=outfile)

# Write the total to the output file
print('\nTotal: ' + str(sum), file=outfile)

# Close the output file
outfile.close()
print('Output complete')

# End-of-file (EOF)

