Huffman coding
from queue import Queue as Q
class Node:
	l = None
	r = None
	
	count = 0
	bit = 0
	ch = None
	def __init__(self, l = None, r = None):
		if l is not None:
						self.l = l
						self.count += l.count
		if r is not None:
						self.r = r
						self.count += r.count

	def isLeaf(self):
		return self.l == None or self.r == None


pattern = []
table = {}
def createTable(head):
	if head.isLeaf():
		table[head.ch] = "".join(map(lambda x: str(x), pattern))
		return table

	pattern.append(0)
	createTable(head.l)
	pattern.pop()

	pattern.append(1)
	createTable(head.r)
	pattern.pop()

	return table
	

def huffman(string):
	counter = [0 for _ in range(26)]
	for s in string:
		counter[ord(s) - ord('a')] += 1

	counter = map(lambda x : (chr(ord('a') + x[0]), x[1]), enumerate(counter))

	res = sorted(counter, key=lambda x: x[1], reverse=True)
	
	counter = [c for c in res if c[1] != 0]
	
	q = Q()
	l = counter.pop()
	r = counter.pop()

	if l[1] > r[1]:
		l, r = r, l

	n1 = Node()
	n1.ch = l[0]
	n1.bit = 0
	n1.count = l[1]

	n2 = Node()
	n2.ch = r[0]
	n2.bit = 1
	n2.count = r[1]

	q.put(n1)
	q.put(n2)
	while len(counter) > 0:
		small = q.get()
		large = q.get()

		# Let n1 be smaller
		n1 = Node(small, large)
		n2 = Node()

		n = counter.pop()
		n2.ch = n[0]
		n2.count = n[1]
			
		if n2.count < n1.count:
			n2, n1 = n1, n2

		n1.bit = 0
		n2.bit = 1

		q.put(n1)
		q.put(n2)

	small = q.get()
	large = q.get()

	head = Node(small, large)

	table = createTable(head)

	res = ""
	for ch in string:
		res += (table[ch])

	return table, res

content = 'abccde'
print(content)
table, res = (huffman(content))
print(table)
print(res)
