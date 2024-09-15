import sys
from collections import deque
n = int(sys.stdin.readline())
q = deque(list(map(int, sys.stdin.readline().split())))


#시간초과코드
while len(q) > 1:
  e = False
  now = q.popleft()
  for i in q:
    if now < i:
      e = True
      print(i, end = " ")
      break
  if e == False:
    print(-1, end = " ")

print(-1)
  
