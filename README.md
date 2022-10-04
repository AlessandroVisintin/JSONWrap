# JSONWrap
> Helper functions to manage JSON/YAML files.

JSONWrap is a helper library to ease the handling of JSON and YAML files.

It contains Context, a library for enhanced handling of JSON data:
With it JSON data can be accessed using subscript operator.
```py

json[0] # Single subscript
json['id','name'] # Multi subscript
json['id',('tags',0)] # Nested multi subs 

```
It also implements the Iterator interface.
```py

tags = json.get(0,'tags')
for key,value in tags:
		[...]

```

## Installation
Clone the project inside your working directory.
You can use it right away by adding the cloned folder into sys.path.
You can also install the package locally by running pip at the root level.
```sh
pip install /path/to/root/level
```

## Usage examples
Use Context to explore JSON.
```py
from JSONWrap.Context import Context
from JSONWrap.utils import load


PATH = 'config/JSONWrap/example.json'


ctx = Context(load(PATH))
# explore subtrees using get
node = ctx.get(0)
# get values using subscript notation
print('ID', node['_id'], '\n')
# use tuple to get nested values
print('TAG', node[('tags',0),], '\n')
# JSON context implements iterator interface
print('TAGS')
for key, value in node.get('tags'):
	print(key, value)

```
Loading, printing, dumping JSON/YAML data.
```py
from JSONWrap.utils import loads
from JSONWrap.utils import is_leaf
from JSONWrap.utils import is_node
from JSONWrap.utils import prettyjson


JSON = ('{"a1":{"b1":[0,1],"b2":{"c1":"t"},"b3":0},"a2":[{"b4": "t"},0]}')

loaded = loads(JSON)
print('Loaded JSON:')
prettyjson(loaded)

print('Is leaf?', is_leaf(loaded))
print('Is node?', is_node(loaded))

```

## Meta
Alessandro Visintin - alevise.public@gmail.com

Find me: [Twitter](https://twitter.com/analog_cs) [Medium](https://medium.com/@analog_cs)

Distributed under the MIT license. See ``LICENSE.txt``.
