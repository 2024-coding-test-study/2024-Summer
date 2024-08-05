a, b = map(int, input().split())
n = 0 # 연산 횟수 저장할 변수

while b > a :
  if b % 2 == 0 : # b가 짝수라면
    b = b / 2
    n += 1
    
  elif b % 10 == 1 : # b의 맨 오른쪽 자리가 1이라면
    b = b // 10
    n += 1
    
  else :
    n = -1
    break
    
if a == b : # a와 b가 같다면
  print(n + 1)
else :
  print(-1)