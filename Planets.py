class graph:
    def __init__(self):   # Undirected Graph
        self.graph = {}
        self.cycle = []
    def add(self,routes):
        for src,dest in routes:
            if src in self.graph :
                self.graph[src].append(dest)
            elif src not in self.graph:
                self.graph[src] = [dest]
            if dest in self.graph :
                self.graph[dest].append(src)
            elif dest not  in self.graph:
                self.graph[dest] = [src]


    def get_shortest_path(self,src,dest,path=[]):
        path = path+[src]
        if src == dest:
            return path
        elif src not in self.graph:
            return []
        shortest_path = None
        for node in self.graph[src]:
            if node not in path:
                sp = self.get_shortest_path(node,dest,path)
                if sp:
                    if shortest_path == None or len(sp)<len(shortest_path):
                        shortest_path = sp

        return shortest_path
    def dfs_helper(self,vertex,status_of_nodes,map,cycle_element=[]):
        status_of_nodes[vertex-1] = 'black'
        # print(vertex)
        if len(cycle_element)<=0:
            for i in self.graph.get(vertex):
                if status_of_nodes[i-1] == 'white':
                    map[i]=vertex
                    self.dfs_helper(i,status_of_nodes,map,cycle_element)
                    status_of_nodes[i-1]='gray'
                else:

                    if status_of_nodes[i-1] == 'black' and i != map.get(vertex) and map.get(vertex) != None:
                        temp = vertex
                        cycle_element.append(i)
                        while temp !=i:
                            if temp not in cycle_element:
                                cycle_element.append(temp)
                            temp = map.get(temp)
        return cycle_element
    def dfs(self,N,ele):
        array = ['white'] * len(self.graph)
        ans = self.dfs_helper(N,array,{},[])
        ele = ele+ans
        return ele
class case:
    def __init__(self,N,graph):
        self.N = N
        self.input_graph = graph
    def solve(self):
        ans = []
        main_graph = graph()
        main_graph.add(self.input_graph)
        cycle_graph = main_graph.dfs(1,[])
        # print(cycle_graph)
        for i in range(1,self.N+1):
            if i in  cycle_graph:
                ans.append(0)
            else:
                distance = 1000000000
                for j in cycle_graph:
                        distance = min(distance,len(main_graph.get_shortest_path(i,j)))
                ans.append(distance-1)
        return ans
# if "__name__" or "__main__":
T = int(input())
for _ in range(1,T+1):
    N = int(input())
    main = []
    for i in range(N):
        start,end = [int(i) for i in input().split()]
        main.append([start,end])
    obj = case(N,main)
    ans = obj.solve()
    print('Case #{}:'.format(_),end=' ')
    print(*ans)
''' 
4
5
3 1
4 5
5 1
5 2
2 1
5
1 2
2 3
3 4
2 4
5 3
3
1 2
3 2
1 3
5
5 4
5 3
2 3
4 3
1 2
'''
