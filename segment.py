
'''
 	Author :- Tanay Kulkarni
	Date   :- 8-5-2021
	Time   :- 16:35:58.396367
	Name   :- solve.py
	
''' 
def debug(*a):
	print(a)
def read(typ = str):
	return typ(input())
def read_arr(typ):
	return list(map(typ,input().split()))
def leading_digit(n:int):
	x  = 0
	while(1<<x<n):
		x+=1
	return 1<<x
def gcd(a,b):
	if b  == 0:
		return a
	return gcd(b,a%b)
MOD = 1e9+7
class Segment:
	def __init__(self,arr:list):
		self.arr = arr
		self.n = leading_digit(len(self.arr))
		x = len(self.arr)
		for i in range(self.n-x):
			self.arr.append(0)
		self.tree = []
		self.build_tree(self.arr)
	def build_tree(self,arr):
		self.tree = [0 for i in range(len(arr)*2)]
		for i in range(self.n):
			self.tree[self.n+i] = (arr[i]%MOD)
		for i in range(self.n-1,0,-1):
			self.tree[i] = self.tree[i*2]+self.tree[i*2+1]		
	def update(self,i,node_low,node_high,index,new_number):
		if node_low == node_high == index:
			self.tree[i] = new_number
			return
		if node_low>index or node_high<index:
			return
		mid = (node_low+node_high)//2
		self.update(i*2,node_low,mid,index,new_number) # left node
		self.update(i*2+1,mid+1,node_high,index,new_number) # right node
		self.tree[i] = self.tree[i*2] + self.tree[i*2+1]
	def updt(self,index,new_num):
		self.update(1,0,self.n-1,index,new_num)
	def grange(self, i , node_low , node_high , qlow , qhigh):
		if qlow<=node_low and qhigh>=node_high:
			return self.tree[i]
		if node_low>qhigh or node_high<qlow:
			return 0
		mid = (node_low+node_high)//2
		p1 = self.grange(i*2,node_low,mid,qlow,qhigh)
		p2 = self.grange(i*2+1,mid+1,node_high,qlow,qhigh)
		return p1+p2
			
def solve():
	n,q = read_arr(int)
	arr = read_arr(int)
	obj = Segment(arr)
	for i in range(q):
		tp,st,ed = read_arr(int)
		if tp == 1:
			obj.updt(st-1,ed)
		else:
			print(int(obj.grange(1,0,obj.n-1,st-1,ed-1)))
		
t = 1
for i in range(1,t+1):
		#print("Case #{}:".format(i),end=' ')
		solve()

