# pySchema
PySchema is a Python library that provides functions to treat and validate data from dictionaries and lists.

### Instalation
To install PySchema, you can use pip:
### Instalation from github
~~~bash 

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

**data:** (dict or list) data to be treated.<br>
**key_or_index:**(int or str) key or index to be treated.<br>
**expected_value:**(str) expected value of the key or index.<br>
**inside:**(List[str]) list of values that the key or index must be inside.<br>
**not_inside:**(List[str]) list of values that the key or index must not be inside.<br>
**required:**(bool) if the key or index is required.<br>
**convert:**(bool) if the key or index must be converted to str.<br>
**default:**(str) default value if the key or index is not required.<br>
**max_len:**(int) max length of the key or index.<br>
**min_len:**(int) min length of the key or index.<br>



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

**data:**(dict or list) data to be treated.<br>
**key_or_index:**(int or str) key or index to be treated.<br>
**expected_value:**(int) expected value of the key or index.<br>
**inside:**(List[int]) list of values that the key or index must be inside.<br>
**not_inside:**(List[int]) list of values that the key or index must not be inside.<br>
**required:**(bool) if the key or index is required.<br>
**convert:**(bool) if the key or index must be converted to int.<br>
**default:**(int) default value if the key or index is not required.<br>
**max:**(int) max value of the key or index.<br>
**min:**(int) min value of the key or index.<br>


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

**data:**(dict or list) data to be treated.<br>
**key_or_index:**(int or str) key or index to be treated.<br>
**expected_value:**(float) expected value of the key or index.<br>
**inside:**(List[float]) list of values that the key or index must be inside.<br>
**not_inside:**(List[float]) list of values that the key or index must not be inside.<br>
**required:**(bool) if the key or index is required.<br>
**convert:**(bool) if the key or index must be converted to float.<br>
**default:**(int) default value if the key or index is not required.<br>
**max:**(int) max value of the key or index.<br>
**min:**(int) min value of the key or index.<br>

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
**key_or_index:**(int or str) key or index to be treated.<br>
**expected_value:**(list) expected value of the key or index.<br>
**inside:**(List[list]) list of values that the key or index must be inside.<br>
**not_inside:**(List[list]) list of values that the key or index must not be inside.<br>
**required:**(bool) if the key or index is required.<br>
**default:**(list) default value if the key or index is not required.<br>
**max_len:**(int) max length of the key or index.<br>
**min_len:**(int) min length of the key or index.<br>    

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
        'city': 'São Paulo',
        'state': 'SP',
    }
}

adress = PySchema.treat_and_get_dict(user_data, 'address')
print(adress)
~~~
##### Args:
**data:**(Union[dict,list]):The data to be treated.<br>
**key_or_index:**(int or str) key or index to be treated.<br>
**expected_value:** (dict) The expected value of the key or index.<br>
**inside:** (List[dict]) The expected values of the key or index.<br>
**not_inside:** (List[dict]) The expected values of the key or index.<br>
**required:** (bool) If the key or index is required.<br>
**default:** (dict) The default value if the key or index is not required.<br>
**max_len:** (int) The maximum length of the leys in value.<br>
**min_len:** (int) The minimum length of the keys in value.<br>

### Getting Any


### Iterating over lists