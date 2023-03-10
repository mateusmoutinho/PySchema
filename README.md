# pySchema
PySchema is a Python library that provides functions to treat and validate data from dictionaries and lists.

### Instalation
To install PySchema, you can use pip:
#### Instalation from github
~~~bash 
pip install git+https://github.com/mateusmoutinho/PySchema
~~~


### Basic Usage 
#### Getting Values 
you can get values using the funcions from PySchema for these:
~~~python
import PySchema
user_data = {
    'name': 'John',
}
name = PySchema.treat_and_get_str(user_data, 'name')
print(name)
~~~
#### Dealing with Errors 
You can get any part of the error with the following comand 

~~~python
import PySchema



user_data = {
    'name': 3,
}


try:
    name = PySchema.treat_and_get_str(user_data, 'name')
    print(name)
except PySchema.PySchemaException as e:
    print(e.props)
~~~
The Output gonna be:
~~~python
{   'type': 'TypeError', 
    'data': {'name': 3},
    'expected_type': <class 'str'>,
    'menssage': "Value: '3' of key: 'name'  is not a 'str' on dict '{'name': 3}'",
    'key': 'name'
}
~~~

#### Validating a full document 
these is a full example of how you can validate a full document
~~~python


import PySchema




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

user_data = {
    'name': 'John',
    'age': 24,
    'emails': ['John@myemail.cmm', 'John2@myemail.com','ss'],
    'address': {
        'street': 'Rua 1',
        'number': 10,
        'city': 'S??o Paulo',
        'state': 'SP'
    }
}

try:
    user_data = treat_user_data(user_data)
except PySchema.PySchemaException as e:
    print(e.props['menssage']) 
~~~



### Getting Values
#### Getting Strings
for getting strings with pyschema you can call the **treat_and_get_str** function
~~~python
import PySchema
user_data = {
    'name': 'John',
}
name = PySchema.treat_and_get_str(user_data, 'name')
print(name)
~~~
##### Getting Args:

**data:** The dict or list to be treated.<br>
**key_or_index:**(Union[int,str]): The key or index to be treated.<br>
**expected_value:**(str, optional): The expected value of the str. Defaults to None.<br>
**inside:**(List[str], optional): The expected values of the str. Defaults to None.<br>
**not_inside:**(List[str], optional): The not expected values of the str. Defaults to None.<br>
**required:**(bool, optional): If the str is required. Defaults to True.<br>
**convert:**(bool, optional): If the str must be converted. Defaults to False.<br>
**default:**(str, optional): The default value if the str is not required. Defaults to None.<br>
**treater (Callable, optional):** A function to treat the value. Defaults to None.<br>
**max_len:**(int, optional): The max length of the str. Defaults to None.<br>
**min_len:**(int, optional): The min length of the str. Defaults to None.<br>



#### Getting Integers

for getting integers with pyschema you can call the **treat_and_get_int** function

~~~python

import PySchema

user_data = {
    'name': 'John',
    'age': 20
}

age = PySchema.treat_and_get_int(data=user_data,key_or_index='age')
print(age)
~~~
##### Args:

**data:**(Union[dict,list]): The dict or list to be treated.<br>
**key_or_index:**(Union[int,str]): The key or index to be treated.<br>
**expected_value:**(int, optional): The expected value of the int. Defaults to None.<br>
**inside:**(List[int], optional): The expected values of the int. Defaults to None.<br>
**not_inside:**(List[int], optional): The not expected values of the int. Defaults to None.<br>
**required:**(bool, optional): If the int is required. Defaults to True.<br>
**convert:**(bool, optional): If the int must be converted. Defaults to True.<br>
**default:**(int, optional): The default value if the int is not required. Defaults to None.<br>
**treater (Callable, optional):** A function to treat the value. Defaults to None.<br>
**max:**(int, optional): The max value of the int. Defaults to None.<br>
**min:**(int, optional): The min value of the int. Defaults to None. <br>

#### Getting Boolean
for getting booleans with pyschema you can call the **treat_and_get_bool** function
~~~python
import PySchema
user_data = {
    'name': 'John',
    'age': 20,
    'single': True,
}

single = PySchema.treat_and_get_bool(
    data=user_data,
    key_or_index='single',
)
print(single)
~~~
##### Args:
**data (Union[dict,list]):** The dict or list to be treated.<br>
**key_or_index (Union[int,str]):** The key or index to be treated.<br>
**expected_value (bool, optional):** The expected value of the bool. Defaults to None.<br>
**required (bool, optional):** If the bool is required. Defaults to True.<br>
**convert (bool, optional):** If the bool must be converted. Defaults to True.<br>
**default (bool, optional):** The default value if the bool is not required. Defaults to None.<br>
**treater (Callable, optional):** A function to treat the value. Defaults to None.<br>



#### Getting Floats
for getting floats with pyschema you can call the **treat_and_get_float** function

~~~python 
import PySchema

user_data = {
    'name': 'John',
    'age': 60
}

age = PySchema.treat_and_get_float(
    data=user_data,
    key_or_index='age'
)
print(age)
~~~
##### Args:

**data:**(Union[dict,list]): The dict or list to be treated.<br>
**key_or_index:**(Union[int,str]): The key or index to be treated.<br>
**expected_value:**(float, optional): The expected value of the float. Defaults to None.<br>
**inside:**(List[float], optional): The expected values of the float. Defaults to None.<br>
**not_inside:**(List[float], optional): The not expected values of the float. Defaults to None<br>
**required:**(bool, optional): If the float is required. Defaults to True.<br>
**convert:** (bool, optional): If the float must be converted. Defaults to True.<br>
**default:**(float, optional): The default value if the float is not required. Defaults to None<br>
**treater (Callable, optional):** A function to treat the value. Defaults to None.<br>
**max:**(float, optional): The max value of the float. Defaults to None.<br>
**min:**(float, optional): The min value of the float. Defaults to None.<br>



### Getting List 

for getting lists with pyschema you can call the **treat_and_get_list** function

~~~python

import PySchema

user_data = {
    'name': 'John',
    'age': 60.4,
    'emails': ['John@myemail.cmm', 'John2@myemail.com']
}

emails = PySchema.treat_and_get_list(user_data, 'emails')
print(emails)
~~~
##### Args:

**data:**(dict or list) data to be treated.<br>
**key_or_index:** (Union[int,str]): The key or index to be treated.<br>
**expected_value:**(list, optional): The expected value of the list. Defaults to None.<br>
**inside:**(List[list], optional): The expected values of the list. Defaults to None.<br>
**not_inside:**(List[list], optional): The not expected values of the list. Defaults to None.<br>
**required:**(bool, optional): If the list is required. Defaults to True.<br>
**default:** (list, optional): The default value if the list is not required. Defaults to None<br>
**treater (Callable, optional):** A function to treat the value. Defaults to None.<br>
**max_len:**(int, optional): The max length of the list. Defaults to None.<br>
**min_len:**(int, optional): The min length of the list. Defaults to None.<br>    

### Getting Dicts

for getting dicts with pyschema you can call the **treat_and_get_dict** function

~~~python

import PySchema


user_data = {
    'name': 'John',
    'age': 60.4,
    'emails': ['John@myemail.cmm', 'John2@myemail.com'],
    'address': {
        'street': 'Rua 1',
        'number': 10,
        'city': 'S??o Paulo',
        'state': 'SP',
    }
}

adress = PySchema.treat_and_get_dict(user_data, 'address')
print(adress)
~~~
##### Args:
**data:** (Union[dict,list]): The dict or list to be treated.<br>
**key_or_index:**(Union[int,str]): The key or index to be treated.<br>
**expected_value:**(dict, optional): The expected value of the dict. Defaults to None.<br>
**inside:**(List[dict], optional): The expected values of the dict. Defaults to None.<br>
**not_inside:**(List[dict], optional): The not expected values of the dict. Defaults to None.<br>
**required:**(dict, optional): If the dict is required. Defaults to True.<br>
**default:**(dict, optional): The default value if the dict is not required. Defaults to None.<br>
**treater (Callable, optional):** A function to treat the value. Defaults to None.<br>
**max_len:** (int, optional): The max length of the dict. Defaults to None.<br>
**min_len:** (int, optional): The min length of the dict. Defaults to None.<br>

### Getting Any

You can get any type with **treat_and_get_any** function

~~~python 

import PySchema


user_data = {
    'name': 'John',
    'age': 60.4,
    'emails': ['John@myemail.cmm', 'John2@myemail.com'],
    'address': {
        'street': 'Rua 1',
        'number': 10,
        'city': 'S??o Paulo',
        'state': 'SP',
    }
}

adress = PySchema.treat_and_get_any(
    data=user_data,
    key_or_index='address',
    expected_type=dict,
)

print(adress)
~~~
### Args:
**data** (Union[dict,list]): The dict or list to be treated.<br>
**key_or_index** (Union[int,str]): The key or index to be treated.<br>
**expected_type** (type, optional): The expected type of the value. Defaults to None.<br>
**in_types** (List[Any], optional): The expected types of the value. Defaults to None.<br>
**expected_value** (Any, optional): The expected value of the value. Defaults to None.<br>
**inside** (list, optional): The expected values of the value. Defaults to None.<br>
**not_inside** (list, optional): The not expected values of the value. Defaults to None.<br>
**required** (bool, optional): If the value is required. Defaults to True.<br>
**convert** (bool, optional): If the value can be converted. Defaults to False.<br>
**default** (Any, optional): The default value if the value is not required. Defaults to None.<br>
**treater (Callable, optional):** A function to treat the value. Defaults to None.<br>

### Iterating over lists

You can iterate over list ,by using the **enumerate** build in method

~~~python

import PySchema
user_data = {
    'name': 'John',
    'age': 60.4,
    'emails': ['John@myemail.cmm', 'John2@myemail.com'],
    'address': {
        'street': 'Rua 1',
        'number': 10,
        'city': 'S??o Paulo',
        'state': 'SP',
    }
}
emails = PySchema.treat_and_get_list(data=user_data,key_or_index='emails')
for index in range(len(emails)):
    current_email = PySchema.treat_and_get_str(data=emails,key_or_index=index)
    print(current_email)
~~~

if you prefer an Function aproach you can make like these:
~~~python
import PySchema
user_data = {
    'name': 'John',
    'age': 60.4,
    'emails': ['John@myemail.cmm', 'John2@myemail.com'],
    'address': {
        'street': 'Rua 1',
        'number': 10,
        'city': 'S??o Paulo',
        'state': 'SP',
    }
}
emails = PySchema.treat_and_get_list(data=user_data,key_or_index='emails')
PySchema.treat_and_get_all(
    data=emails,
    callable=lambda data,index: PySchema.treat_and_get_str(
        data=data,
        key_or_index=index,
        min_len=10
    )
)
~~~
or if you need an procedural aproach , you can make like these:

~~~python

import PySchema
user_data = {
    'name': 'John',
    'age': 60.4,
    'emails': ['John@myemail.cmm', 'John2@myemail.com','ss'],
    'address': {
        'street': 'Rua 1',
        'number': 10,
        'city': 'S??o Paulo',
        'state': 'SP',
    }
}
emails = PySchema.treat_and_get_list(data=user_data,key_or_index='emails')
for email in emails:
    PySchema.check_type(email,str)
~~~


