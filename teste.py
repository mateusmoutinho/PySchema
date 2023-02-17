
import PySchema

user_data = {
    'name': 'John',
    'age': 'aa',
    'emails': ['John@myemail.cmm', 'John2@myemail.com','ss'],
    'address': {
        'street': 'Rua 1',
        'number': 10,
        'city': 'São Paulo',
        'state': 'SP'
    }
}



def treat_adress(adress):
    PySchema.ensure_not_expected_keys_is_present(
        data=adress,
        expected_keys=['street','number','city','state']
    )
    street = PySchema.treat_and_get_str(data=adress,key_or_index='street')
    number = PySchema.treat_and_get_int(data=adress,key_or_index='number')
    city = PySchema.treat_and_get_str(data=adress, key_or_index='city')
    state = PySchema.treat_and_get_str(data=adress,key_or_index='state')
    return adress


def treat_user_data(user_data):
    PySchema.ensure_not_expected_keys_is_present(
        data=user_data,
        expected_keys=['name','age','emails','address']
    )
    PySchema.treat_and_get_str(data=user_data,key_or_index='name')
    PySchema.treat_and_get_int(data=user_data,key_or_index='age')
    emails =PySchema.treat_and_get_list(data=user_data,key_or_index='emails')
    PySchema.treat_and_get_all(
        data=emails,
        callable=lambda data,index: PySchema.treat_and_get_str(
            data=data,
            key_or_index=index
        )
    )
    PySchema.treat_and_get_dict(
        data=user_data,
        key_or_index='address',
        treater=treat_adress
    )
    return user_data


try:
    user_data = treat_user_data(user_data)
except PySchema.PySchemaException as e:
    print(e.props['menssage']) 