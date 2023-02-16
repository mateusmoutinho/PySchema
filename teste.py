import PySchema



user_data = {
    'name': 3,
}


try:
    name = PySchema.treat_and_get_str(user_data, 'name')
    print(name)
except PySchema.PySchemaException as e:
    print(e.props)
    