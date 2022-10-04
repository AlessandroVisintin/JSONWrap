import json
from typing import Any, Union


class Context:
	"""
	
	Wrap a JSON structure for enhanced handling.
	
	JSON structure can be explored with 'get'.
	json.get(0,'tags')
	
	JSON data can be accessed using subscript operator.
	Single subscript : json[0]
	Multi subscript : json['id','name'] (returns list)
	Nested multi subs : json['id',('tags',0)]
	
	Iterator interface: JSONContext supports iterator interface
	with json.get(0,'tags') as node:
		for key,value in node:
			[...]
	
	"""
	
	def __init__(self, json_data:Any) -> None:
		"""
		
		Args:
			json_data : JSON structure.
		
		"""
		
		self.ctx = json_data


	def __str__(self) -> str:
		"""
		
		Print behaviour.
		
		"""
		
		return json.dumps(self.ctx, indent=2)
	
	
	def __contains__(self, key:Union[str,int]) -> bool:
		"""
		
		Contains 'in' operator.
		
		"""
		
		return key in self.ctx
	
	
	def __getitem__(self, name:str) -> Any:
		"""
		
		Subscript [] operator.
		
		"""
		
		if not isinstance(name, tuple):
			name = (name,)
		out = []
		for key in name:
			if isinstance(key, tuple):
				try:
					tmp = self.ctx
					for k in key:
						tmp = tmp[k]
					out.append(tmp)						
				except (KeyError,IndexError,TypeError):
					out.append(None)
			else:
				try:
					out.append(self.ctx[key])						
				except (KeyError,IndexError,TypeError):
					out.append(None)
		if len(out) == 1:
			return out[0]
		return out
	

	def __iter__(self) -> 'Context':
		"""
		
		Iterator interface.

		"""
		
		self._i = 0
		if isinstance(self.ctx, dict):
			self._k = sorted(self.ctx.keys())
		return self


	def __next__(self) -> 'Context':
		"""
		
		Iterator interface.
		
		"""
		
		try:
			if isinstance(self.ctx, dict) or isinstance(self.ctx, list):
				k = (self._k[self._i] if isinstance(self.ctx, dict)
					 else self._i)
				self._i += 1
				return k, Context(self.ctx[k])
			if self._i == 0:
				self._i += 1
				return None, Context(self.ctx)
			raise TypeError
		except (IndexError, TypeError):
			raise StopIteration


	def get(self, *args):
		"""
		
		Navigate JSON subtree with list of keys.
		
		Args:
			list of params that correspond to the keys to explore.
		
		"""

		if not isinstance(args, tuple):
			args = (args,)
		out = self.ctx
		for key in args:
			try:
				out = out[key]
			except (KeyError,IndexError,TypeError):
				out = None
				break
		return Context(out)
