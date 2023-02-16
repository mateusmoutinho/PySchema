
import PySchema


user_data = {
    'name': 'John',
    'age': 60.4,
    'emails': ['John@myemail.cmm', 'John2@myemail.com'],
    'address': {
        'street': 'Rua 1',
        'number': 10,
        'city': 'São Paulo',
        'state': 'SP',
    }
}

adress = PySchema.treat_and_get_dict(user_data, 'address')
print(adress)