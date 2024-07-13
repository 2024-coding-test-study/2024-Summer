n, m = map(int, input().split()) # 집과 길 개수 입력 받기
p = [0] * (n + 1)
edges = []
result = 0

for i in range(1, n + 1) :
  p[i] = i
  
# 속한 마을을 확인하는 함수
def find_p(p, x) :
  if p[x] != x :
    p[x] = find_p(p, p[x])
  return p[x]

# 마을을 합치는 함수
def union(p, a, b) :
  a = find_p(p, a) # 각 집이 속한 마을 찾기
  b = find_p(p, b)
  
  if a < b :
    p[b] = a
  else :
    p[a] = b
    
for _ in range(m) :
  a, b, cost = map(int, input().split())
  edges.append((cost, a, b))
  
# 유지비의 오름차순으로 정렬
edges.sort()
max = 0 # 가장 큰 유지비를 저장할 변수

for edge in edges :
  cost, a, b = edge
  
  if find_p(p, a) != find_p(p, b) :
    union(p, a, b)
    result += cost
    
    if cost > max :
      max = cost

print(result - max) # 결과에서 가장 큰 길을 빼주면 최소 유지비의 길로 이뤄진 마을 2개를 얻을 수 있음