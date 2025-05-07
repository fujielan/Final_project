import sys
import numpy as np
from ase import Atoms
from ase.io import read
#import the revalent module, ase is a python based software for atomic simulation environment

def main(atom_index):
    # Load the initial slab from a VASP POSCAR file
    slab = read('POSCAR_0')

    # Extract structural data from ASE atomic index in order to pick the target atom
    positions = slab.get_positions()              # this is cartesian coords of each atom
    symbols = slab.get_chemical_symbols()         # this is a list of element symbols
    cell = slab.get_cell()                        
    constraints = slab.constraints            

    # Define the new element H  and its height above the chosen atom
    new_element = 'H'
    height_offset = 1.0                            # Distance (Å) above the atom in z-direction

    # Copy the position of the selected atom and raise it by height_offset
    base_pos = positions[atom_index].copy()
    base_pos[2] += height_offset

    # Combine old and new data together
    all_symbols = symbols + [new_element]
    all_positions = np.vstack([positions, base_pos])

    # Create new slab with the extra atom, and keeps cell and constraints
    new_slab = Atoms(
        symbols=all_symbols,
        positions=all_positions,
        cell=cell,
        pbc=True,
        constraints=constraints
    )

    # Save to a new POSCAR
    new_slab.write('POSCAR')


if __name__ == '__main__':
    # Read atom index from command-line argument and run
    idx = int(sys.argv[1])
    main(idx)
