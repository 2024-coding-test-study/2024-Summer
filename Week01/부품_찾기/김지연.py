#손님이 문의한 M개 종류 탐색 M이 100000, n이 1000000
#순차탐색으로 진행하며m*n이 되므로 너무 오래걸림
# m개를 탐색하기 위해 n을 이진탐색해야함
#풀이시간: 8m 19s
n = int(input())
stock = list(map(int, input().split()))
m = int(input())
want = list(map(int, input().split()))

def binary(start, end, target):
  while start <= end:
    mid = (start + end) // 2
    if target == stock[mid]:
      return print("yes")
    if target < stock[mid]:
      end = mid - 1
    elif target > stock[mid]:
      start = mid + 1
  return print("no")

stock.sort()
for i in want:
  binary(0, n-1, i)