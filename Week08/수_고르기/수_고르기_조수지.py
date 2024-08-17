n, m = map(int, input().split())
nums = []

for _ in range(n) :
  nums.append(int(input()))
  
nums.sort() # 오름차순 정렬

start, end = 0, 0
best = 99999999999 # 가장 적은 차를 저장할 변수. 충분히 크게 설정해 둠.

while end < n and start < n :
  minus = nums[end] - nums[start] # 차를 저장함
  
  if minus >= m :
    best = min(best, minus)
    start += 1
  else :
    end += 1
    
print(best)