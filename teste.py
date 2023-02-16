
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

adress = PySchema.treat_and_get_any(
    data=user_data,
    key_or_index='address',
    expected_type=dict,
)

print(adress)