def get_max_age_user_name(data:list) -> str:
    """
    Return the name of the user with the maximum age in a dictionary.

    Args:
        data (dict): A dictionary of values
    Returns:
        str: The name of the user with the maximum age in the dictionary
    """
    max=data[0]['age']
    a=data[0]['name']
    for i in range(1,len(data)):
        if max < data[i]['age']:
            max=data[i]['age']
            a=data[i]['name']
        return a
data = [
   {
        'name': 'John', 
         'age': 27
    }, 
    {
         'name': 'Mary', 
         'age': 42
    }
  ]
print(get_max_age_user_name(data))
