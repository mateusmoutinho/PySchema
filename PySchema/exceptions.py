from typing import Any

class PySchemaException(Exception):
    def __init__(self,props:dict):
        data = None
        if 'data' in props.keys():
            data = props['data']
        
        if isinstance(data,dict):
            props['menssage'] = props['menssage'].replace('#key#','key').replace('#data#','dict')
            props['key'] = props['key_or_index']
            del props['key_or_index']
        
        elif isinstance(data,list):
            props['index'] = props['key_or_index']
            props['menssage'] = props['menssage'].replace('#key#','index').replace('#data#','list')
            del props['key_or_index']

        
        self.props = props
        super().__init__(props['menssage'])

