def gen1(count):
	i = 1
	while i<=count:
		yield i
		i += 1

	return count

def get_gen(count):
	print("\nget_gen: ")
	g2 = yield from gen1(count)
	print("type of g2: ", type(g2))
	print("value of g2: ", g2)
	return g2


if __name__ == '__main__':
	print("star gen1:")
	g1 = gen1(10)
	gg = get_gen(5)

	print("\n")
	print("type of gen1: ", type(gen1))
	print("type of g1: ", type(g1))
	print("type of gg: ", type(gg))
	print("value of gg: ", gg)

	print("\niterate gg: ")
	for t in gg:
		print(t)

	# ngg = next(gg)
	# print("type of ngg: ", type(ngg))
	# print("value of ngg: ", ngg)

	print("\niterate g1: ")
	for t in g1:
		print(t)
