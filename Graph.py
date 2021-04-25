def read(typ)->int:
	return typ(input())
def read_arr(typ)->list:
	return list(map(typ,input().split()))
class graph:
	def __init__(self):
		self.gp = dict()
	def create(self,paths = list()):
		for start,end in paths:
			if not self.gp.get(start):
				self.gp[start] = list()
			if  not self.gp.get(end):
				self.gp[end] = list()
			self.gp[start].append(end)
			self.gp[end].append(start)		
	def bfs(self,current:int):
		n = len(self.gp)
		visited = [False for i in range(n+1)]
		queue = [current]
		while queue:
			tmp = queue.pop()
			if not visited[tmp]:
				print(tmp,end = ' ')
			visited[tmp] = True
			for i in self.gp.get(tmp):
				if not visited[i] :
					queue.append(i)
def dfs_helper(self,visited:list,current:int):
		print(current,end=' ')
		visited[current] = True
		for i in self.gp.get(current):
			if visited[i] == False:
				self.dfs_helper(visited,i)
def dfs(self,start:int):
		n = len(self.gp)
		visited = [False for i in range(n+1)]
		self.dfs_helper(visited,start)
n = read(int)
paths = list()
for i in range(n):
	tmp = read_arr(int)
	paths.append(tmp)
obj = graph()
obj.create(paths)
obj.bfs(4)
print()
