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
