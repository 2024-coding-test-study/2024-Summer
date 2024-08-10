n = int(input())
#문자열로된 것은 -x[1]이런식으로 내림차순 정렬할 수 없다.
data = []
for i in range(n):
  name, k, e, m = input().split()
  data.append((name, int(k), int(e), int(m)))

data.sort(key = lambda x: (-x[1], x[2], -x[3], x[0]))

for i in data:
  print(i[0])