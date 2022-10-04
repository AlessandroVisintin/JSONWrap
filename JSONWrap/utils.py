import json
import os
import yaml
from typing import Any
from numbers import Number


def loads(string:str, **kwargs) -> Any:
	"""
		
	Load a string in YAML or JSON format.
		
	Args:
		string : string to load
		**kwargs:
			indent (str, optional) : indentation character for 
				YAML format. Defaults to double space.
	
	Returns:
		loaded JSON structure.
		
	Raises:
		RuntimeError : parsing errors.
		
	"""
		
	try:
		return json.loads(string)
	except json.JSONDecodeError as e:
		error = f'{e}\n'
	try:
		indent = '  ' if not 'indent' in kwargs else kwargs['indent']
		return yaml.safe_load(string.replace(indent, '  '))
	except yaml.YAMLError as e:
		error += f'{e}\n'
	raise RuntimeError(f'Parsing errors:\n{error}')


def load(path:str, **kwargs) -> Any:
	"""
	
	Load a YAML / JSON file.
		
	Args:
		path : path to the file
		**kwargs:
			see loads() for avaiable kwargs
	
	Returns:
		loaded JSON structure.
		
	Raises:
		RuntimeError: file not found or parsing errors.
	
	"""
		
	try:
		with open(path, 'r', encoding='utf8') as f:
			return loads(f.read(), **kwargs)
	except FileNotFoundError:
		raise RuntimeError('File not found.')


def dumps(data:Any, form:str='yaml', **kwargs) -> str:
	"""
		
	Dump current JSON state to string.
		
	Args:
		data: JSON data to dump.
		form (optional) : dump format. Supported: yaml, json
			Defaults to yaml.
		**kwargs:
			indent (int, optional): indentation value (JSON).
				Defaults to 2.
			style (bool, optional): use default style (YAML).
				Defaults to False.
			sort (bool, optional): sort keys (YAML, JSON).
				Defaults to False.
		
	Returns:
		formatted string
		
	Raises:
		RuntimeError: unsupported format.
		
	"""
		
	if form == 'yaml':
		style = False if not 'style' in kwargs else kwargs['style']
		sort = False if not 'sort' in kwargs else kwargs['sort']
		return yaml.dump(data, sort_keys=sort, default_flow_style=style)
	elif form == 'json':
		indent = 2 if not 'indent' in kwargs else kwargs['indent']
		sort = False if not 'sort' in kwargs else kwargs['sort']
		return json.dumps(data, sort_keys=sort, indent=indent)
	else:
		raise RuntimeError('Unsupported format.')
	
	
def dump(data:Any, path:str, **kwargs) -> None:
	"""
	
	Dump current JSON state to file. Imply file extension from
	the path.
		
	Args:
		data: JSON data to dump.
		path: path where to dump.
		**kwargs:
			see dumps() for available kwargs.
	
	Raises:
		RuntimeError: path does not exist.
	"""
		
	try:
		_, ext = os.path.splitext(path)
		if len(ext) > 1 and ext[0] == '.':
			ext = ext[1:]
		with open(path, 'w', encoding='utf8') as f:
			f.write(dumps(data, form=ext, **kwargs))
	except FileNotFoundError:
		raise RuntimeError('Path does not exist.')


def is_leaf(value:str) -> bool:
	"""
	
	Check if 'value' is bool, number, string or None.
	
	Args:
		value: value to check.
	
	Returns:
		True if value is one of the basic data types, False otherwise.
	
	"""
	
	return (isinstance(value, bool) or isinstance(value, Number) or
		isinstance(value, str) or value is None)


def is_node(x):
	"""
	
	Check if x is dict or list.
	
	Args:
		x : value to check
	
	Returns:
		True if value is dict or list, False otherwise.
	
	"""
	
	return (isinstance(x, list) or isinstance(x, dict))



def prettyjson(data:Any, indent:int=2) -> None:
	"""
	
	Pretty print JSON data.
	
	Args:
		data : JSON structure
		indent (optional) : indentation of text. Defaults to 2.
	
	"""
	
	print(json.dumps(data, indent=indent))
