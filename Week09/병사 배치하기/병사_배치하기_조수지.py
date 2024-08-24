n = int(input())
soldiers = list(map(int, input().split()))
dp = [1] * n # 내림차순이 가능한 최소 길이는 1이기에 1로 초기화

for i in range(1, n) :
  for j in range(i) :
    if soldiers[j] > soldiers[i] :
      dp[i] = max(dp[i], dp[j] + 1)
      
max_length = max(dp) # 가장 큰 값 찾기

print(n - max_length) # n에서 빼줌으로써 열외자 수 출력