import sys
sys.setrecursionlimit(10000)
class graph:
    def __init__(self,n):   # Undirected Graph
        self.graph = {}
        self.cycle = []
        self.n = n
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

    def bfs(self, start_node, cycle, arr,status):
        counter = 0
        queue = []
        maps = [-1]*(self.n+100)
        queue.append(start_node)
        while queue:
            if queue[0] != None:
                s = queue.pop(0)
                if maps[s-1] != -1:
                    counter*=0
                    counter += maps[s-1]
                if s!= start_node:
                    arr[s - 1] = min(arr[s-1],counter)
                counter += 1
                for i in self.graph.get(s):
                    if status[i - 1] == False:
                        arr[i - 1] =min(arr[i-1],counter)
                        status[i - 1] = True
                        queue.append(i)
                        maps[i-1] = counter
            else:
                return
    def dfs_helper(self,vertex,status_of_nodes,map,cycle_element):
        status_of_nodes[vertex - 1] = True
        for i in self.graph.get(vertex):
            if status_of_nodes[i-1] == False:
                map[i]=vertex
                self.dfs_helper(i,status_of_nodes,map,cycle_element)
                status_of_nodes[i-1]='gray'
            elif status_of_nodes[i-1] == True and i != map.get(vertex) and map.get(vertex) != None:
                    temp = vertex
                    cycle_element.append(i)
                    while temp !=i:
                        if temp not in cycle_element:
                            cycle_element.append(temp)
                        temp = map.get(temp)


                        # return  cycle_element
    def dfs(self,N):
        # for i in range(1,N+1):
        ans = []
        array = [False] * (N+10)
        self.dfs_helper(1,array,{},ans)
        return ans
class case:
    def __init__(self,N,graph):
        self.N = N
        self.input_graph = graph
    def solve(self):
        ans = [N+1]*N
        main_graph = graph(self.N)
        main_graph.add(self.input_graph)
        cycle_graph = main_graph.dfs(self.N)
        status = [False] * (self.N)
        # print(cycle_graph)
        for cyclic_node in cycle_graph:
            status[cyclic_node - 1] = True
            ans[cyclic_node-1] = 0
        for i in cycle_graph:
                main_graph.bfs(i,cycle_graph,ans,status)
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

2
6
1 3
2 3
3 4
4 5
5 3
6 2
7
7 2
6 2
2 3
1 3
3 4
4 5
5 3
Case #1: 1 1 0 0 0 2
Case #2: 1 1 0 0 0 2 2

    '''
