n = int(input())
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

print(SUM)