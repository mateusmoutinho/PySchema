
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
try:
    PySchema.ensure_not_expected_keys_is_present(
        data=user_data,
        expected_keys=['name','age','emails','address']
    )
except PySchema.PySchemaException as e:
    print(e.props)