def kwargs_length(**kwargs):
    return(len(kwargs))


dictionary_x = {'name': 'Peter', 'age': 25}
print(kwargs_length(**dictionary_x))

dictionary = {}
print(kwargs_length(**dictionary))