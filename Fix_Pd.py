# This line Initialize the ZPE accumulator
zpe_sum_meV = 0.0

# Open the OUTCAR file and this file is a output file from the ZPE calculation from the 
# computation package and this can give you a full lise the zpe lines but for this code the 
#OUTCAR can be served as a input file.
file_handle = open('OUTCAR', 'r')

# Following code will read all lines into a list from the OUTCAR file
all_lines = []
for single_line in file_handle:
    all_lines.append(single_line)


file_handle.close()

#  Loop over every line and looking out for excat f terms which in outcar means the actual frequency line which is the valid line
for idx in range(len(all_lines)):
    line = all_lines[idx]
    

    contains_marker = False
    if "f  =" in line:
        contains_marker = True
    
    # Next steo is to look for the  imaginary‑frequency marker "f/i=" and try to get rid of it, becaus this is the "trash" data
    contains_imag = False
    if "f/i=" in line:
        contains_imag = True
    
    # This code make sure that only proceed if it's a real frequency line, which means all imaginary frequency will be negelected
    if contains_marker and not contains_imag:
        
        # Split the line into parts on spaces
        raw_parts = line.split(' ')
        
        # Clean up the split so we remove empty strings
        tokens = []
        for part in raw_parts:
            if part != "":
                tokens.append(part)
        
        # Make sure we have at least 10 tokens before indexing
        if len(tokens) >= 10:
            # Extract the 10th token (index 9)
            freq_str = tokens[9]
            
            # following will convert to float 
            try:
                freq_val = float(freq_str)
                
                # Compute half of this energy , and maks sure divide by 2 and then sum up
                half_energy = freq_val * 0.5
                
                zpe_sum_meV = zpe_sum_meV + half_energy
            except Exception as e:
                # If conversion fails, just skip silently
                skip_variable = e  # dummy use so beginner code doesn't complain
        else:
            # If there aren't enough tokens, do nothing 
            not_enough = True  # another dummy variable

# Finally, print out the computed ZPE, and show the result
print("Zero-Point Energy (ZPE) in meV:", zpe_sum_meV)
