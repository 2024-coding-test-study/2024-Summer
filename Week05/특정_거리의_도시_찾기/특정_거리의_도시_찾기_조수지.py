from collections import deque
import sys
input = sys.stdin.readline # 이걸 안하면 시간 초과 뜸

n, m, k, x = map(int, input().split()) # 도시 개수, 도로 개수, 거리 정보, 출발 도시 번호
city = [[] for _ in range(n + 1)] # 도시 정보 저장할 리스트
INF = 99999 # 무한대 설정
distance = [INF] * (n + 1) # x로부터의 최단 거리 리스트 초기화
distance[x] = 0 # x자신으로의 거리는 0

# 도로 입력 받기
for i in range(m) :
  a, b = map(int, input().split()) 
  city[a].append(b)
  
q = deque([x])

while q :
  now = q.popleft() # 현재 상태에서 가장 먼저 들어온 정보 pop
  
  for next in city[now] :
    if distance[next] == INF : # 방문한 도시가 아니라면
      distance[next] = distance[now] + 1 # 거리를 바꿔줌
      q.append(next) # 다음 도시에 방문하기 위해 큐에 넣어줌
      
check = False # 최단 거리가 k인 도시가 존재하는지 여부

for i in range(1, n + 1) :
  if distance[i] == k : # 최단 거리가 k라면 해당 도시를 출력
    print(i)
    check = True
    
if check == False :
  print(-1) # 거리가 k인 도시가 없다면 -1을 출력