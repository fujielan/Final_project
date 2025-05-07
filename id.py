#import revalent modules
import numpy as np
import matplotlib.pyplot as plt

def energy_diagram(data, slope=0.5, colors=None, alpha=1, label=None, step_labels=None, font_size=6):
    """
    The following are parameter I define and gives the details of each one I have done in code
    Parameters:
      data: list or array of energies at each reaction stage.
      slope: controls the horizontal width of each state line, I have to make sure the slop is optimal for each reaction stage without blocking words on top.
      colors: list with one element to define the color of the plot lines.
      alpha: transparency for the plot lines.
      label: label for the dashed connecting lines.
      step_labels: list of custom labels for each step for example "ID + H₂(g)", "ID* + H₂(g)", etc.
      font_size: size of the font for the step labels.
    """
    # Set default color if none provided.
    if colors is not None and len(colors) > 0:
        color = colors[0]
    else:
        color = 'blue'
    
    # Prepare the energy data: each state is represented as a horizontal segment.
    y_data = np.repeat(data, 2)
    x_data = np.empty_like(y_data, dtype=float)
    # Each stage gets two x coordinates, offset by half the slope.
    x_data[0::2] = np.arange(1, len(data) + 1) - (slope / 2)
    x_data[1::2] = np.arange(1, len(data) + 1) + (slope / 2)
    
    # Draw dashed lines connecting each consecutive state.
    for i in range(len(data) - 1):
        plt.plot(x_data[i * 2:i * 2 + 4], y_data[i * 2:i * 2 + 4],
                 lw=2, linestyle='dashed', color=color, alpha=alpha, label=label)
    
    # Draw horizontal state lines for each stage.
    for i in range(0, len(data) * 2, 2):
        plt.plot(x_data[i:i + 2], y_data[i:i + 2], lw=3, color=color, alpha=alpha)
    
    # Add custom labels (or default step numbers) above each state.
    for i in range(len(data)):
        x_center = i + 1
        y_offset = 0.1  # Adjust this offset as needed.
        if step_labels is not None and i < len(step_labels):
            text_label = step_labels[i]
        else:
            text_label = f"{i+1}"
        plt.text(x_center, data[i] + y_offset, text_label, ha='center', va='bottom', 
                 fontsize=font_size, fontweight='bold',color='black')
    
    plt.xlabel('Reaction Step')
    plt.ylabel('Relative Energy (eV)')
    plt.title('Energy Diagram for ID to 8H-ID')
    plt.tight_layout()

# Example energy data.
energy_data_ID = [0, -2.844, -3.732, -3.214, -4.499, -3.370, -5.795, -3.497, -1.907]

# Define custom step labels on top of each blue stage of corresponding steps.
step_labels = [
    r'ID+H$_2$(g)+5*',   # Step 1: ID + H₂(g)
    r'ID*+H$_2$(g)+4*',  # Step 2: ID* + H₂(g)
    r'(ID+2H)*+2*',      # Step 3: (ID + 2H)*
    r'2H–ID*+4*',        # Step 4: 2H–ID* + 2
    r'(2H–ID+2H)*+2*',   # Step 5: (2H–ID + 2H)*
    r'4H–ID*+4*',        # Step 6: 4H–ID* + 2
    r'(4H–ID+4H)*+4*',   # Step 7: (4H–ID + 4H)*
    r'8H–ID*+4*',      # Step 8: 8H–ID* + 4
    r'8H–ID(g)+5*'     # Step 9: 8H–ID(g) + 4
]

plt.figure(figsize=(12, 6))
energy_diagram(energy_data_ID, colors=['blue'], label='2MID', step_labels=step_labels, font_size=6)
plt.show()
