n = int(input())
nums = list(map(int, input().split()))
result = [-1] * n
stack = []

for i in range(n) :
    while stack and nums[i] > nums[stack[-1]] : # 스택이 비어있지 않고 현재 수가 스택 가장 위에 있는 수보다 크면
        result[stack.pop()] = nums[i]

    stack.append(i) # 인덱스를 넣어줘야함. 인덱스가 아닌 그냥 수를 넣으면 오류

for num in result :
    print(num, end=' ')