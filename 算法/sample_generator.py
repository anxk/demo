import random


def genOneZeroMatrix(m: int, n: int) -> list:
	mtx = []
	for i in range(m):
		row = []
		for j in range(n):
			row.append(random.randint(0, 1))
		mtx.append(row)
	return mtx


def genMatrix(m: int, n: int) -> list:
	mtx = []
	for i in range(m):
		row = []
		for j in range(n):
			row.append(random.randint(0, 100))
		mtx.append(row)
	return mtx


def genXYPoints(n: int) -> list:
	l = []
	for i in range(n):
		l.append([i+1, random.randint(-100, 100)])
	return l


def genIntervals(n: int) -> list:
	l = []
	for i in range(n):
		a = random.randint(-100, 100)
		b = random.randint(-100, 100)
		if a > b:
			a, b = b, a
		if a == b:
			b = b + 1
		l.append([a, b])
	return l


def genSeries(n: int) -> list:
	l = []
	for i in range(n):
		l.append(random.randint(1, 1000))
	return l


def genDNA(n: int) -> str:
	s = ""
	for i in range(n):
		s += ['A', 'C', 'G', 'T'][random.randint(0, 3)]
	return s


def genStr(n: int) -> str:
	s = ""
	for i in range(n):
		s += "abcdefghijklmnopqrtsuvwxyz"[random.randint(0, 25)]
	return s


def genNumStr(n: int) -> str:
	s = ""
	for i in range(n):
		s += "1123456789"[random.randint(0, 9)]
	return s.upper()


def genStrSeries(n: int) -> list:
	ans = []
	for i in range(n):
		s = ""
		for i in range(random.randint(1, 7)):
			s += "abcdefghijklmnopqrtsuvwxyz"[random.randint(0, 10)]
		ans.append(f"{s}")
	return ans


if __name__ == '__main__':
	for i in range(8):
		pass
		# print(genOneZeroMatrix(8, 8))
		# print(genXYPoints(100))
		# print(genIntervals(100))
		# print(genDNA(100000))
		print(genSeries(500))
		# print(genMatrix(100, 100))
		# print(random.randint(1, 100000))
		# print('"%s"' % genStr(16))
		# print(genStrSeries(500))
		# print('"%s"' % genNumStr(90))
