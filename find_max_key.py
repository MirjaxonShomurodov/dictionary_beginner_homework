def find_max_key(data: dict):
    """
    Return the maximum int or float key in a dictionary.
    Args:
        data (dict): A dictionary of values
    Returns:
        int: The maximum key in the dictionary.
    """
    return max(data.keys())
    
data = {
                    1.3 :'a', 
                    7.8 :'b', 
                    4 : 'c'
  }

print(find_max_key(data))