import numpy as np

def format_number(value):
    """
    Format a number or list of numbers for display
    """
    if isinstance(value, (list, tuple, np.ndarray)):
        
        return ', '.join([format_number(item) for item in value])
    elif isinstance(value, (int, float)):
        if value == int(value):
            return str(int(value))
        else:
            return f"{value:.8f}".rstrip('0').rstrip('.') if '.' in f"{value:.8f}" else f"{value:.8f}"
    return str(value)