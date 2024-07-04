# 48분 소요
# 프로그래머스에서 효율성 0점..
def solution(food_times, k):
    answer = 0
    time = 0 
    index = 0 # food_times리스트의 index를 나타내는 변수
    
    # k초 이전에 다 먹으면 -1을 반환
    if sum(food_times) <= k :
            return -1
    
    while 1 :
          if food_times[index] == 0 : # index+1번째 음식을 먹어야 하는 시간이 0이면 
            index = (index + 1) % len(food_times) # 다음번 음식으로 넘어감
            continue
          
          if time == k : # 네트워크 오류가 발생하면
            answer = index + 1 # index+1을 answer에 저장. 
            break
            
          food_times[index] = food_times[index] - 1 # 냠냠
          time += 1
          index = (index + 1) % len(food_times) # 다음 음식으로 넘어감
            
    return answer
          
        