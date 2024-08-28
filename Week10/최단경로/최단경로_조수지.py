# 문제에서 정점 개수 v, 간선 개수 e를 입력받고
# (u, v, w) 형태의 간선이 주어진다고 해서
# 주어진대로 변수명을 했더니 런타임 에러나고....
# 내가 잘못한게 아니었다... 한참 코드만 바라봤네...

import sys
import heapq

input = sys.stdin.readline

v, e = map(int, input().split()) # 노드와 간선 개수 입력받기
k = int(input()) # 시작 노드의 번호

graph = [[] for _ in range(v + 1)]

# 인접 리스트 형태로 간선 입력받기
for _ in range(e) :
    a, b, c = map(int, input().split()) # a에서 b로 가는 가중치 c인 간선
    graph[a].append((b, c))

dist = [float('inf')] * (v + 1)
dist[k] = 0 # 시작점 자신은 0

def dijkstra(start) :
    q = []
    heapq.heappush(q, (0, start)) # 큐에 (가중치, 노드) 를 넣어줌
    
    # 큐가 빌 때까지 반복
    while q :
        current_dist, u = heapq.heappop(q) # pop하여 가중치와 노드를 추출
        
        if dist[u] < current_dist : # 현재 가중치보다 작은 가중치가 이미 있다면
            continue # 무시
        
        for v, weight in graph[u] : # 현재 노드의 인접 노드를 검사
            distance = current_dist + weight
            
            if distance < dist[v] : # 현재 노드가 더 적은 가중치라면
                dist[v] = distance # 갱신
                heapq.heappush(q, (distance, v)) # 큐에 넣어줌

dijkstra(k)

# 각 노드의 최단 거리 출력
for i in range(1, v + 1) :
    if dist[i] == float('inf'):
        print('INF')
         
    else :
        print(dist[i])