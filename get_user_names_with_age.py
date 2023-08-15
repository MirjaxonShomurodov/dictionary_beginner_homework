def get_user_names_with_age(data:list, age:int) -> list:
    """
    Return a list of users with a given age

    Args:
        data (dict): A dictionary of values
        age (int): The age to search for
    Returns:
        list: A list of users with the given age
    """
    names=[]
    while data:
        user = data.pop()
        user_age=user['age']
        name = user['name']
        
        if age == user_age:
            names.append(name)
        return name

data = [
            {
            'name': 'John', 
            'age': 30
            }, 
            {
            'name': 'Ann', 
            'age': 32
            }, 
            {
            'name': 'Sam', 
            'age': 27
            }, 
            {
            'name': 'Mary', 
            'age': 32
            }
        ]
print(get_user_names_with_age(data,30))

