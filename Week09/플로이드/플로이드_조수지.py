import sys
input = sys.stdin.readline

n = int(input())  # 도시 개수
m = int(input())  # 버스 개수
INF = int(1e9)  # 무한대 설정
bus = [[INF] * (n + 1) for _ in range(n + 1)]  # 버스 정보 저장할 리스트

for i in range(1, n + 1):
    bus[i][i] = 0  # 자기 자신으로 가는 비용은 0

for _ in range(m):
    a, b, c = map(int, input().split())  # 시작 도시, 도착 도시, 비용
    bus[a][b] = min(c, bus[a][b])  # 더 적은 비용을 저장

# 플로이드-워셜 알고리즘을 통해 최소 비용 계산
for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            bus[i][j] = min(bus[i][j], bus[i][k] + bus[k][j])
            
for a in range(1, n + 1) :
  for b in range(1, n + 1) :
    if bus[a][b] == INF : # 갈 방법이 없다면
      print("0", end=" ") # 0 출력
    else :
      print(bus[a][b], end=" ")
  
  print()