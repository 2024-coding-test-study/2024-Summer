n, m = map(int, input().split()) # 학생의 번호와 연산의 개수 입력받기
p = [0] * (n + 1) # 초기화

for i in range(1, n + 1) :
  p[i] = i
# 속한 팀을 확인하는 함수
def find_p(p, x) :
  if p[x] != x :
    p[x] = find_p(p, p[x])
  return p[x]

# 팀을 합치는 함수
def union(p, a, b) :
  a = find_p(p, a) # 각 학생이 속한 팀 찾기
  b = find_p(p, b)
  
  if a < b :
    p[b] = a
  else :
    p[a] = b
    
# 입력받은 연산 개수만큼 반복
for i in range(m) :
  num, a, b = map(int, input().split())
  
  if num == 0 :
    union(p, a, b)
  else :
    if find_p(p, a) == find_p(p, b) :
      print("YES")
    else :
      print("NO")