class case:
    def __init__(self,palindrome_array,question):
        self.main_array = palindrome_array
        self.question = question
    def solve(self):
        counter = 0
        for i in self.question:
            temp = self.main_array[i[0]-1:i[1]]
            chk = self.palindrome(list(temp))
            if chk>0:
                counter+=1
        return counter
    def palindrome(self,main_arr):
        if len(main_arr) == 1:
            return True
        arr = main_arr
        result = True;
        for i in range(len(arr)):
            corresponding_index = len(arr) - i - 1
            if i >= corresponding_index:
                return result
            if arr[i] != arr[corresponding_index]:
                for j in range(i + 1, len(arr) - i):
                    if (arr[i] == arr[j]) or (j+1<len(arr) and arr[i] != arr[j] == arr[j + 1]):
                        temp = arr[j]
                        arr[j] = arr[corresponding_index]
                        arr[corresponding_index] = temp
                        result = True
                    else:
                        result = False
            else:
                result = True
T = int(input())
for _ in range(1,T+1):
    N,Q = [int(i) for i in input().split()]
    String = str(input())
    questions = []
    for i in range(Q):
        start,end = [int(i) for i in input().split()]
        questions.append([start,end])
    obj = case(String,questions)
    ans = obj.solve()
    print('Case #{}: {}'.format(_,ans))
