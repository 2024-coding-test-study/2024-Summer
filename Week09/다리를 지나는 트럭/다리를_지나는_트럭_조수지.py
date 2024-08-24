from collections import deque

def solution(bridge_length, weight, truck_weights):
  truck_weights = deque(truck_weights) # 대기 트럭
  moving = deque([0] * bridge_length) # 다리를 건너는 중인 트럭
  time = 0 # 경과 시간
  current_weight = 0 # 현재 다리 위 트럭들의 무게
    
  # 대기 중인 트럭이 존재하거나 건너는 트럭이 있는 동안 반복
  while truck_weights or current_weight > 0 :
    time += 1
    current_weight -= moving.popleft() # 1초가 지났으므로 건넘 처리
      
    if truck_weights and current_weight + truck_weights[0] <= weight : # 대기 트럭이 있고 새로 건너게 해도 무게를 넘지 않는다면
      new_truck = truck_weights.popleft()
      moving.append(new_truck)
      current_weight += new_truck
      
    else : # 대기 중인 트럭이 없거나 새로 건너게 할 수 없다면(무게를 초과해서)
      moving.append(0) # 빈공간 만들어주기
      
  return time