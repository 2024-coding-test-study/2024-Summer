from collections import deque
import copy


#time: 57m
n = int(input())

graph = [[] for _ in range(n+1)]
time = [0] * (n+1) 
indegree = [0] * (n+1)
for i in range(1, n+1):
  info = list(map(int, input().split()))

  for k in info[1:-1]:
    graph[k].append(i) #graph[i].append(k)로 잘못생각함
    indegree[i] += 1
  time[i] = info[0]

total_time = 0
def topology_sort():
  queue = deque()

  # result = [0] * (n+1)
  # #시간 리스트 복사
  # for i in range(1, n+1):
  #   result[i] = time[i] #대입 연산자 문제 발생

  result = copy.deepcopy(time)
    
  #inderee없는거 큐에 삽입
  for i in range(1, n+1):
    if indegree[i] == 0:
      queue.append(i) #indegree없는 과목 번호 삽입
  while queue:
    s = queue.popleft()
    for i in graph[s]: #i는 선수 과목 s를 수강한 후 들을 수 있는 과목
      
      indegree[i] -= 1
      if indegree[i] == 0:
        #선수과목 중 동시에 수강했을 때 거리는 시간
        result[i] = max(result[s] + time[i], result[i])
        queue.append(i)
  for i in range(1, n+1):
    print(result[i])

topology_sort()
