def find_int_keys(data: dict) -> list:
    """
    Return a list of all keys in a dictionary that are integers.
    Args:
        data (dict): A dictionary of values
    Returns:
        list: A list of all keys in the dictionary that are integers.
    """
    find=0
    for i in data:
        if i['age']=='age':
            find+=1
    return find

data=[
    {
        'name':'John',
        'age':27
    },
    {
        'name':'Ann',
        'age':42
    },
    {
        'name':'Mary',
        'age':27
    }
  ]
data1=data,('age',27)
print(find_int_keys(data1))