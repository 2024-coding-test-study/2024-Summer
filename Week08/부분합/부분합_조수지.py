n, s = map(int, input().split()) # 길이와 부분합 입력받기
nums = list(map(int, input().split()))
min_len = 999999 # 충분히 크게 잡아줌
start, end = 0, 00
cur_sum = 0

while end < n : # 범위를 벗어나지 않을 동안 반복
  cur_sum += nums[end]

  while cur_sum >= s : # 합이 부분합보다 커졌을 때
    min_len = min(min_len, end - start + 1) # 최소 길이 갱신
    cur_sum -= nums[start]
    start += 1
    
  end += 1
  
  
if min_len == 999999 :
  print(0)
else :
  print(min_len)




# 이중 for문을 쓰면 시간 초과 O(n^2)
'''for i in range(n) :
  sum = 0
  cur_len = 0
  
  for j in range(i, n) :
    if sum < s : # s보다 현재 합이 작으면
      sum += nums[j] # 더해주고
      cur_len += 1 # 길이도 늘려줌

      if sum >= s : # 부분합보다 합이 커졌다면
        if cur_len < min_len : # 지금까지 가장 짧은 길이와 비교
          min_len = cur_len # 만약 현재 부분합의 길이가 더 작다면 갱신
        break # 현재 시점에서 가장 짧은 길이를 찾았으므로 반복 필요 없음'''
