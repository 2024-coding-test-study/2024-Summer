from collections import deque

n = int(input()) # 카드 개수 입력받기

nums = deque()

for i in range(1, n + 1) :
  nums.append(i)
  
while len(nums) > 1 : # 마지막 하나가 남을 때 까지 반복
  nums.popleft() # 제일 위의 카드 버리기
  nums.append(nums.popleft()) # 제일 위의 카드를 제일 아래로 옮기기
  
print(nums[0])