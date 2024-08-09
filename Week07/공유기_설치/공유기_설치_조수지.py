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
low, high = 1, houses[-1] - houses[0]

best_dist = 0

while low <= high :
  mid = (low + high) // 2
  
  if install_ok(houses, c, mid) :
    best_dist = mid
    low = mid + 1
    
  else :
    high = mid - 1
    
print(best_dist)