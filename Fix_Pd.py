# Step 1: Initialize the ZPE accumulator
zpe_sum_meV = 0.0

# Step 2: Open the OUTCAR file (we won't use a with‑block here to be more verbose)
file_handle = open('OUTCAR', 'r')

# Step 3: Read all lines into a list manually
all_lines = []
for single_line in file_handle:
    all_lines.append(single_line)

# Step 4: Close the file 
file_handle.close()

# Step 5: Loop over every line by index 
for idx in range(len(all_lines)):
    line = all_lines[idx]
    
    # Step 5 Look for the exact marker "f  =" indicating a real frequency
    contains_marker = False
    if "f  =" in line:
        contains_marker = True
    
    # Step 5 then, look for the  imaginary‑frequency marker "f/i=" and try to get rid of it
    contains_imag = False
    if "f/i=" in line:
        contains_imag = True
    
    # Step 5 Only proceed if it's a real frequency line, which means all imaginary frequency will be negelected
    if contains_marker and not contains_imag:
        
        # Step 6: Split the line into parts on spaces
        raw_parts = line.split(' ')
        
        # Step 7: Clean up the split so we remove empty strings
        tokens = []
        for part in raw_parts:
            if part != "":
                tokens.append(part)
        
        # Step 8: Make sure we have at least 10 tokens before indexing
        if len(tokens) >= 10:
            # Extract the 10th token (index 9)
            freq_str = tokens[9]
            
            # Step 9: Try converting to float 
            try:
                freq_val = float(freq_str)
                
                # Step 10: Compute half of this energy 
                half_energy = freq_val * 0.5
                
                # Step 11: Add to our running total
                zpe_sum_meV = zpe_sum_meV + half_energy
            except Exception as e:
                # If conversion fails, just skip silently
                skip_variable = e  # dummy use so beginner code doesn't complain
        else:
            # If there aren't enough tokens, do nothing 
            not_enough = True  # another dummy variable

# Step 12: Finally, print out the computed ZPE
print("Zero-Point Energy (ZPE) in meV:", zpe_sum_meV)
