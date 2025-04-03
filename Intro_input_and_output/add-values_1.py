"""
This module demonstrates working with input and output.

Author: Arnold Murphy
Date: 2025-04-02
"""

# Open the input and output files using 'with' and specify encoding
print('Processing input')
TOTAL_SUM = 0

try:
    with open(r'C:\Users\ArnoldMurphy\OneDrive - PQA\Development\Python Pre-requisite course 02\Ex_Files_Programming_Foundations_2023\Ex_Files_Programming_Foundations_2023\Scratch Solutions\Intro_input_and_output\values.txt', 'rt', encoding='utf-8') as infile, \
         open(r'C:\Users\ArnoldMurphy\OneDrive - PQA\Development\Python Pre-requisite course 02\Ex_Files_Programming_Foundations_2023\Ex_Files_Programming_Foundations_2023\Scratch Solutions\Intro_input_and_output\values_totaled.txt', 'wt', encoding='utf-8') as outfile:

        # Process each line in the input file
        for line in infile:
            line = line.strip()  # Remove leading and trailing whitespace
            if line:  # Check if the line is not empty
                TOTAL_SUM += int(line)
                print(line, file=outfile)

        # Write the total to the output file
        print('\nTotal: ' + str(TOTAL_SUM), file=outfile)
except FileNotFoundError as e:
    print(f"Error: {e}")

print('Output complete')




# End-of-file (EOF)



