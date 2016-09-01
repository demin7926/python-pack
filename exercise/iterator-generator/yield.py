# Program:
# 	yield & yield from语法演示
# Reference:
# 	https://docs.python.org/3/whatsnew/3.3.html#pep-380

def accumulate():
	tally = 0
	while 1:
		next = yield
		if next is None:
			return tally
		tally += next

def gather_tallies(tallies):
	while 1:
		tally = yield from accumulate()
		tallies.append(tally)


if __name__ == '__main__':
	tallies = []
	acc = gather_tallies(tallies)
	next(acc)  # Ensure the accumulator is ready to accept values
	for i in range(4):
		acc.send(i)

	acc.send(None)  # Finish the first tally
	for i in range(5):
		acc.send(i)

	acc.send(None)  # Finish the second tally
	print(tallies)
