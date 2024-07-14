#find함수 만들고
#union 함수 만들고
#time: 7m 44s
def find_team(parent, i): #i 부모 찾기
  if parent[i] != i:
    parent[i] = find_team(parent, parent[i])
  return parent[i]

def union_team(parent, a, b): #a,b 합치기
  p_a = find_team(parent, a)
  p_b = find_team(parent, b)
  if p_a < p_b:
    parent[p_b] = p_a
  else:
    parent[p_a] = p_b

n, m = map(int, input().split())
parent = [0] * (n+1)
#부모 초기화
for i in range(n+1):
  parent[i] = i
  
#연산 시작
for i in range(m):
  op, a, b = map(int, input().split())
  if op == 0: #union
    union_team(parent, a, b)
  else:
    if find_team(parent, a) == find_team(parent, b):
      print("YES")
    else:
      print("NO")

