
class Solor(object):

	def __init__(self):
		self.planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn']
		self._index = 0

	def push(self, name):
		self.planets.append(name)

	def print_all(self):
		print("Solor.print_all:")
		for p in self.planets:
			print(p)
		print("================")


	def __iter__(self):
		return self

	def next(self):
		"""
		Python 2
		"""
		print(">>>>> next():")
		if self._index >= len(self.planets):
			raise StopIteration

		item = self.planets[self._index]
		self._index += 1
		return item

	def __next__(self):
		"""
		Python 3
		"""
		print(">>>>> __next__():")
		if self._index >= len(self.planets):
			raise StopIteration

		item = self.planets[self._index]
		self._index += 1
		return item


if __name__ == '__main__':
	s = Solor()
	s.print_all()  # OK, print all planets in the Solor

	# only when s, which is a Solor object is iterable
	for p in s:
		print (p)
