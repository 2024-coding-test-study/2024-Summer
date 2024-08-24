n = int(input()) # 일 할 수 있는 날짜 입력받기
job = []

for i in range(n) :
  t, p = map(int, input().split()) # 상담 기간과 금액 입력받기
  
  job.append((t, p)) # job에 튜플 추가

dp = [0] * (n + 1)

for i in range(n - 1, -1, -1) : # job을 역순으로 확인
  t, p = job[i]
  
  if i + t <= n : # 만약 이 일을 완료할 수 있다면
    dp[i] = max(p + dp[i + t], dp[i + 1]) # 더 큰 이익을 저장
  else :
    dp[i] = dp[i + 1] # 그대로 이전 값을 저장
    
print(dp[0]) # 최종 이익 출력