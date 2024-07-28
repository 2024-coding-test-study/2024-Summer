from itertools import combinations

n, m = map(int, input().split()) # 도시의 크기와 최대 존재 치킨집 수 입력 받기
chicken, house = [], [] # 각 리스트에는 좌표가 저장될 것임

# 도시 정보를 입력받아 일반 집과 치킨 집 각각 저장하기
for r in range(n) :
    data = list(map(int, input().split()))
    
    for c in range(n) :
        if data[c] == 1 :
            house.append((r, c))
            
        elif data[c] == 2 :
            chicken.append((r, c))

# 모든 치킨 집 중에서 m개의 치킨 집을 뽑는 조합을 저장하는 리스트. 
# 치킨집이 최대 m개 존재할 수 있기에 m개의 조합을 찾음
candidates = list(combinations(chicken, m))

# 치킨 집 조합 중 하나의 조합에 대해 치킨 거리의 합을 계산하는 함수
def get_sum(candidate) :
    result = 0
    
    for hx, hy in house : # 모든 집에 대하여 가장 가까운 치킨 집을 찾기
        temp = 1e9 # 일단은 무한으로 초기화
        
        for cx, cy in candidate :
            temp = min(temp, abs(hx - cx) + abs(hy - cy))
          
        result += temp # 한 집에서 가장 가까운 치킨 집까지의 거리를 result에 더해줌
       
    return result # 한 조합에 대한 치킨 거리 반환

result = 1e9 # 일단은 무한으로 초기화

# 모든 치킨 집 조합에 대해서 가장 작은 값의 치킨 거리 찾기
for candidate in candidates :
    result = min(result, get_sum(candidate))

print(result)