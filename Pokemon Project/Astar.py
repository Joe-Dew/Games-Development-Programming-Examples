class Node:
	def __init__(self, neighbours, pos):
		self.parent = None
		self.l = float("inf")
		self.g = float("inf")
		self.neighbours = neighbours
		self.pos = pos
		self.visited = False
	def heuristic(self, end):
		return (end.pos[0] - self.pos[0])**2 + (end.pos[1] - self.pos[1])**2


	def __repr__(self):
		return f"({self.pos[0]}, {self.pos[1]})"		


def astar(start, end):
	start.l = 0
	start.g = start.heuristic(end)
	openList = [start]

	while len(openList) > 0:
		openList.sort(key = lambda n: n.g)

		while len(openList) > 0 and openList[0].visited:
			openList.pop(0)

		if not openList:
			break

		else:
			current = openList[0]
			current.visited = True

			for neighbour in current.neighbours:
				if not neighbour.visited:
					openList.append(neighbour)
					if neighbour.l > 1 + current.l:
						neighbour.parent = current
						neighbour.l = 1 + current.l
						neighbour.g = neighbour.l + neighbour.heuristic(end)

	p = end
	final = None
	while p.parent != None:
		print(p)
		final = p.pos
		p = p.parent
	return p.pos



def grid(leng, hei):
	row = []
	for i in range(leng):
		col = []
		for j in range(hei):
			col.append(Node([], (i, j)))
		row.append(col)
	for i in range(leng):
		for j in range(hei):
			current = row[i][j]
			if j > 0:
				current.neighbours.append(row[i][j-1])
			if j < hei-1:
				current.neighbours.append(row[i][j+1])
			if i > 0:
				current.neighbours.append(row[i-1][j])
			if i < leng-1:
				current.neighbours.append(row[i+1][j])
	return row

g = grid(5, 5)
start = g[1][2]
end = g[4][4]

print()
for v in range(len(g[0])):
	print(g[v])
print(astar(start, end))

