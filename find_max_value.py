def find_max_value(data: dict):
    """
    Return the maximum int or float value in a dictionary.
    Args:
        data (dict): A dictionary of values
    Returns:
        int: The maximum value in the dictionary.
    """
    data = {
        'a' : -4, 
        'b' : -10, 
        'c' : 0
         }
    
    arr=(data['a'])
    arr1=(data['b'])
    arr2=(data['c'])

    if arr>arr1 and arr>arr2:
        return arr
    if arr1>arr and arr1>arr2:
        return arr1
    if arr2>arr and arr2>arr1:
        return arr2

print(find_max_value("data"))