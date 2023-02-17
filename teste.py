import PySchema 
from PySchema.exceptions import PySchemaException
values= {
    'emails':['email1','email2','email3',10]
}

emails = PySchema.treat_and_get_list(values,'emails')
for email in emails:
    PySchema.check_type(email,str)
    print(email)