# 왜 안돼???????
'''n = int(input())
nums = []

for _ in range(n):
  nums.append(int(input()))

nums.sort(reverse=True) # 내림차순 정렬

SUM = 0
idx = 0

while idx < len(nums): # idx가 리스트를 벗어나지 않을 동안 반복
  # idx + 1도 리스트를 벗어나지 않고 1보다 큰 원소가 나란히 2개일 때나 -1보다 작은 원소가 나란히 2개일 때 곱해줌
  if idx + 1 < len(nums) and ((nums[idx] > 1 and nums[idx + 1] > 1) or (nums[idx] < -1 and nums[idx + 1] < -1)):
    SUM += nums[idx] * nums[idx + 1]
    idx += 2
        
  elif nums[idx] == 0 :
    if (len(nums) - idx - 1) % 2 == 0 : # 남은 음수의 개수가 짝수개라면
      idx += 1 # 0을 더해봤자 똑같으므로 idx만 1 추가해줌
      
    else : # 남은 음수의 개수가 홀수개라면
      # 0과 다음 수를 곱해도 0이므로 idx에 2 더해줌
      idx += 2
     
  # 이외의 경우는 그냥 더해줌 
  else:
    SUM += nums[idx]
    idx += 1

print(SUM)'''

n = int(input())
plus = [] # 1보다 큰 수를 저장할 리스트
minus = [] # 0보다 작은 수를 저장할 리스트
result = 0 # 합을 나타낼 변수 0으로 초기화
zero_count = 0 # 0이 있는지 확인할 변수

for i in range(n) :
  INPUT = int(input())
  
  if INPUT > 1 :
    plus.append(INPUT)
  elif INPUT < 0 :
    minus.append(INPUT)
  elif INPUT == 0 :
    zero_count += 1
  else : # 1을 만나면
    result += INPUT
    
plus.sort(reverse=True) # 내림차순 정렬
minus.sort() # 오름차순 정렬

idx = 0

while idx < len(plus) :
  if idx + 1 < len(plus) :
    result += plus[idx] * plus[idx + 1]
    idx += 2
  else : # 마지막 남은 하나를 더해줌
    result += plus[idx]
    idx += 1
    
idx = 0

while idx < len(minus) :
  if idx + 1 < len(minus) :
    result += minus[idx] * minus[idx + 1]
    idx += 2
  else : # 음수의 개수가 홀수개라면
    if zero_count == 0 :
      result += minus[idx]
    idx += 1

print(result)