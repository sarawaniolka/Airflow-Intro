def get_names():
    return {'first_name': 'S',
            'last_name': 'W'}
    

def greet(n1,n2):
    print(f'Hello, {n1}, {n2}.')
    

name_dict = get_names()
print(name_dict['first_name'])