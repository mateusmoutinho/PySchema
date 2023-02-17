
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
    }
}
emails = PySchema.treat_and_get_list(data=user_data,key_or_index='emails')
for email in emails:
    PySchema.check_type(email,str)