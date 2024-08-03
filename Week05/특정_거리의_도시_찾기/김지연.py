#dfs 거리가 다 1이므로 dfs로 최단경로 찾을 수 잇음
n, m, k, x = map(int, input().split())
#dfs 수행할 graph 초기화
graph = [[] for i in range(n + 1)]
for i in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
INF = int(1e9)
visited = [INF] * (n + 1)
visited[x] = 0  #자기자신의 거리는 0

result = []


def dfs(start, cnt):
  if start <= 0 or start > n or cnt == k:
    return
  for now in graph[start]:
    if visited[now] == INF:
      visited[now] = visited[start] + 1
      dfs(now, cnt)
    else:  #이미 방문해도 최소거리가 아닌 경우
      if visited[now] > visited[start] + 1:
        visited[now] = visited[start] + 1


dfs(x, 0)

if k not in visited:
  print(-1)
else:
  for i in range(1, n + 1):
    if visited[i] == k:
      print(i)
