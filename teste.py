
import PySchema

user_data = {
    'name': 'John',
    'age': 60.4,
    'emails': ['John@myemail.cmm', 'John2@myemail.com','ss'],
    'address': {
        'street': 'Rua 1',
        'number': 10,
        'city': 'São Paulo',
        'state': 'SP',
    },
    'teste':2
}


def treat_adress(adress):
    street = PySchema.treat_and_get_str(data=adress,key_or_index='street')
    number = PySchema.treat_and_get_int(data=adress,key_or_index='number')
    city = PySchema.treat_and_get_str(data=adress, key_or_index='city')
    state = PySchema.treat_and_get_str(data=adress,key_or_index='state')
    return adress


adrress = PySchema.treat_and_get_dict(
    data=user_data,
    key_or_index='address',
    expected_type=dict,
    treater=treat_adress
)

print(user_data)