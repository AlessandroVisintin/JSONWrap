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
