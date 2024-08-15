import sys

n, s = map(int, sys.stdin.readline().rstrip().split())

data = list(map(int, sys.stdin.readline().rstrip().split()))

start, end = 0, 0
interval = n
p = False


for start in range(n):
  total = 0
  end = start
  current_sum = data[start]


  for i in range(start, n):
    if current_sum >= s:
      
      
      p = True
      if interval > end - start + 1:
        interval = end - start + 1
        break
    elif current_sum < s:
      end += 1
      if end >= n:
        break
      current_sum += data[end]
  if interval == 1:
    break


if p:
  print(interval)
else:
  print(0)