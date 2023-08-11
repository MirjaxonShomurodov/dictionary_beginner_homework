def get_min_age_user_name(data:list) -> str:
    """
    Return the name of the user with the minimum age in a dictionary.

    Args:
        data (dict): A dictionary of values
    Returns:
        str: The name of the user with the minimum age in the dictionary
    """
    min=data[0]['age']
    a=data[0]['name']
    for i in range(1,len(data)):
        if min > data[i]['age']:
            min=data[i]['age']
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
    },
    {
        'name': 'John', 
        'age': 32
    }, 
    {
        'name': 'Mary', 
        'age': 18
    }, 
    {
        'name': 'Ann', 
        'age': 20
    },
    {
        'name': 'Ban', 
        'age': 29
  }
  ]
print(get_min_age_user_name(data))
