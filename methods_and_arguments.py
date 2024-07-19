def example_method(mandatory_param, default_param='Default', *args, **kwargs):
    print(f'''
    mandatory_param: {mandatory_param} {type(mandatory_param)}
    default_param: {default_param} {type(default_param)}
    args: {args} {type(args)}
    kwargs: {kwargs} {type(kwargs)}
    ''')


example_method('Mandatory param')
example_method(mandatory_param='Mandatory param')
example_method('Mandatory param', 'Default param')
example_method('Mandatory param', 'Default param', 'args1', 'args2', 'args3')
example_method('Mandatory param', 'Default param', key1='value1', key2='value2')
example_method('Mandatory param', 'Default param', 'args1', 'args2', 'args3', key1='value1', key2='value2')

example_list = ['Mandatory param', 'Default param', 3, 4, 5, 6]
example_dict = {'args': 'args1', 'args2': 'args2', 'args3': 'args3'}
example_method(*example_list, **example_dict)
