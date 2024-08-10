# dist의 거리로 공유기 c개 설치 가능한지 보는 함수
def install_ok(houses, c, dist) :
  count = 1
  last_position = houses[0] # 일단 제일 첫 집에 설치
  
  for i in range(1, len(houses)) :
    if houses[i] - last_position >= dist :
      count += 1
      last_position = houses[i]
      
      if count == c :
        return True
  
  return False

n, c = map(int, input().split())
houses = []

for _ in range(n) :
  houses.append(int(input()))
  
houses.sort() # 오름차순 정렬
low, high = 1, houses[-1] - houses[0] # 두 집이 최소로 떨어질 수 있는 거리는 1이므로 1로 초기화

best_dist = 0

while low <= high :
  mid = (low + high) // 2 # 이진 탐색을 위해 mid 값 지정
  
  if install_ok(houses, c, mid) :
    best_dist = mid # 최소 거리를 업데이트 하고
    low = mid + 1 # 더 넓게 띄울 수 있는지 확인
    
  else : # 더 짧은 거리로 띄울 수 있는지 확인
    high = mid - 1
    
print(best_dist)