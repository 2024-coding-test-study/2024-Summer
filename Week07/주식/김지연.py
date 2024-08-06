#https://www.acmicpc.net/board/view/128845 참고한 자료
import sys
t = int(sys.stdin.readline())

result = []
for _ in range(t):
  day = int(sys.stdin.readline())
  lst = list(map(int, input().split()))
  profit = 0
  lst.reverse() 
  #역순으로 하면 미래에서 현재 주가를 미리 예상할 수 있으므로 미래 주가보다 작은 주가만 사면된다.
  #역순이 아니면 8 5 4 9 10 이렇게 있다고 치면 현재 주가보다 더 큰 주가가 있는지 계속 검색해야한다. -> O(N^2)으로 시간초과 나는 이유

  k=0
  for i in range(1, len(lst)):
    next = lst[k]
    if next >= lst[i]: #다음날 주가가 이전 날보다 크다면 이전 주식 사기
      profit += next - lst[i]
    else:
      # lst = lst[i:] #슬라이싱하면 시간초과된다고 한다
      k = i
  print(profit)