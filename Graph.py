class graph:
    def __init__(self):
        self.dic = {}
    def add(self,arr):
        if arr[0] in self.dic:
            self.dic[arr[0]].append(arr[1])
        else:
            self.dic[arr[0]] = [arr[1]]
    def print_routes(self):
        print(self.dic)
N = int(input())
routes = []
for i in range(N):
    start,end = [str(i) for i in input().split()]
    routes.append((start,end))
obj = graph()
for i in routes:
    obj.add(i)
obj.print_routes()
