#시간초과...
import sys
t = int(sys.stdin.readline())

result = []
for _ in range(t):
  day = int(sys.stdin.readline())
  lst = list(map(int, sys.stdin.readline().split()))
  profit = 0
  while lst:
    max_idx = lst.index(max(lst))
    
    for i in range(max_idx):
      profit += lst[max_idx] - lst[i]
    if max_idx == len(lst)-1:
      break
    lst = lst[max_idx+1:]
  result.append(profit)

for i in result:
  print(i)