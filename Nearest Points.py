class case:
    def __init__(self, coords,k):
        self.list_of_coordinates = coords
        self.k = k
    def squareRoot(self,n):
        x = n
        y = 1
        e = 0.000001
        while (x - y > e):
            x = (x + y) / 2
            y = n / x
        return x
    def find_distance(self,x,y):
        distance = self.squareRoot((x*x)+(y*y))
        return distance
    def top_points(self,arr):
        final = [];keys = sorted(arr.keys())
        for i in range(self.k):
            final.append(arr.get(keys[i]))
        return final
    def solve(self):
        list_of_distance = {}
        for i in range( len(self.list_of_coordinates)):
            distance  = self.find_distance(self.list_of_coordinates[i][0],self.list_of_coordinates[i][1])
            list_of_distance[distance] = i+1
        ans_array = self.top_points(list_of_distance)
        return ans_array
T = int(input())
for i in range(1,T+1):
    No_of_points,K = [int(i) for i in  input().split()]
    List_of_coordinates = []
    for j in range(0,No_of_points):
        X,Y = [int(i) for i  in input().split()]
        List_of_coordinates.append([X,Y])
    obj = case(List_of_coordinates,K)
    ans = obj.solve()
    print('Case #{}: {}'.format(i,ans))
