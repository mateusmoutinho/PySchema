import PySchema

user_data = {
    'name': 'John',
    'age': 20,
    'single': 'ss',
}

single = PySchema.treat_and_get_bool(
    data=user_data,
    key_or_index='single',
    convert=False
)
print(single)
