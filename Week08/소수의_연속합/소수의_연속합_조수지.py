# 에라토스테네스의 체(n까지의 수열 중 소수 구하기)
def prime_list(n) :
  prime_nums = [True] * (n + 1)
  m = int(n ** 0.5) # n의 최대 약수가 sqrt(n) 이하이므로 sqrt(n)값으로 초기화
  
  for i in range(2, m + 1) : # 소수의 시작은 2부터라서 2부터 반복 시작
    if prime_nums[i] == True : # i가 소수라면
      for j in range(i * i, n + 1, i) : # i의 배수를 찾아서
        prime_nums[j] = False # False로 바꿔줌
        
  # 소수 목록 산출
  return [i for i in range(2, n + 1) if prime_nums[i] == True]


n = int(input())

num_list = prime_list(n)
start, end = 0, 0
sum = 0
find = 0

while end <= len(num_list) : # end가 범위를 벗어나지 않을 동안 반복
  if sum < n : # 만약 합이 n보다 작으면
    if end == len(num_list) : # end가 마지막까지 갔다면 반복문 종료
      break
    
    sum += num_list[end] # 합에 더해주고
    end += 1
    
  elif sum > n : # 만약 합이 n보다 크다면
    sum -= num_list[start] # 합에서 빼주고
    start += 1 
      
  else : # 만약 합이 n과 같다면
    find += 1 # find에 1을 더해줌 
    sum -= num_list[start] # 합이 n인 다른 수열이 있을 수 있으므로 합에서 빼줌
    start += 1
    
print(find)