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
    def get_routes(self,start,end,path=[]):
        path = path+[start]
        if start==end:
            return [path]
        if start not in self.dic:
            return []
        paths = []
        for i in self.dic.get(start):
            if i not in path:
                new_path = self.get_routes(i,end,path)
                for j in new_path:
                    paths.append(j)
        return paths
    def get_shortest_route(self,start,end,path=[]):
        path = path+[start]
        if start == end:
            return path
        if self.dic.get(start) == None :
            return None
        short_path = None
        for i in self.dic[start]:
            if i not in path:
                sp = self.get_shortest_route(i,end,path)
                if sp:
                    if short_path == None or len(sp)<len(short_path):
                        short_path = sp
        return short_path
    def dfs_helper(self,vertex,status_of_nodes,map,cycle_element=[]):
        status_of_nodes[vertex-1] = 'black'
        # print(vertex)
        for i in self.graph.get(vertex):
            if status_of_nodes[i-1] == 'white':
                if map.get(i)==None:
                    map[i]=vertex
                self.dfs_helper(i,status_of_nodes,map)
                status_of_nodes[i-1]='gray'
    def dfs(self,N):
        ans = 0
        for i in range(1,N+1):
            array = ['white'] * len(self.graph)
            ans = self.dfs_helper(i,array,{})
        return ans    
# N = int(input())
routes = [
    ['Mumbai','Paris'],
    ['Mumbai','Dubai'],
    ['Paris','Dubai'],
    ['Paris','New york'],
    ['Dubai','New york'],
    ['New york','Toronto'],
    ['Mumbai','Toronto'],
]
obj = graph()
for i in routes:
    obj.add(i)
print(obj.get_routes('Mumbai','Toronto'))
