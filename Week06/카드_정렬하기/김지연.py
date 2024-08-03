import heapq
n = int(input())

heap = []

#힙은 pop할 때 가장 작은 원소를 pop한다
for _ in range(n):
  heapq.heappush(heap, int(input()))

total = 0
while len(heap) != 1:
  num1 = heapq.heappop(heap)
  num2 = heapq.heappop(heap)
  total += num1 + num2
  heapq.heappush(heap, num1+num2)
print(total)