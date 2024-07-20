#풀이시간: 51m 53s
from collections import deque
n = int(input())
data = list(map(int, input().split()))
data.sort()
q = deque(data)

f = q.popleft()
cnt = 1
last_f = f
group = 0
while q:
  if last_f <= cnt:
    group += 1
    cnt = 0
  else:
    last_f = q.popleft()
    cnt += 1
    
print(group)
      