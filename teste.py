import PySchema

user_data = {
    'name': 'John',
    'age': 20,
    'single': 'aa',
}

single = PySchema.treat_and_get_bool(
    data=user_data,
    key_or_index='single',
)
print(user_data)
