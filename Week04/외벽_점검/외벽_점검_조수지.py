# 답을 보기 전에 리스트를 어떻게 원형으로 표현할 지 막막했었는데
# 길이의 2배를 해주면 되는거였음!
# combinations(조합)는 순서가 중요하지 않지만 permutations(순열)는 순서가 중요함!
from itertools import permutations

# n은 외벽 길이, weak는 취약 지점 위치 담긴 배열, dist는 각 친구 1시간 동안 이동 가능 거리
def solution(n, weak, dist) :
    length = len(weak)
    
    # 길이를 2배로 늘려서 원형을 일자 형태로 변형
    for i in range(length) :
        weak.append(weak[i] + n)
        
    answer = len(dist) + 1 # 투입할 친구 수의 최솟값을 찾아야 하므로 dist 길이보다 큰 값으로 초기화
    
    # 0부터 length - 1까지의 위치를 각각 시작점으로 설정
    for start in range(length) :
        # 친구를 나열하는 모든 경우 각각에 대하여 확인
        for friends in list(permutations(dist, len(dist))) :
            count = 1 # 투입할 친구의 수
            
            # 해당 친구가 점검할 수 있는 마지막 위치
            position = weak[start] + friends[count - 1]
            
            # 시작 취약점부터 모든 취약한 지점을 확인
            for index in range(start, start + length) :
                # 점검할 수 있는 위치를 벗어나는 경우
                if position < weak[index] :
                    count += 1 # 새로운 친구를 투입
                    
                    if count > len(dist) : # 더 투입이 불가능하다면 종료
                        break
                    
                    # 다음 친구가 점검 시작할 취약점 위치를 정해줌
                    position = weak[index] + friends[count - 1]
                    
            answer = min(answer, count) # 최솟값 계산
            
    if answer > len(dist) : # 투입 되는 친구의 최솟값이 친구들의 수보다 많으면
        return -1 # 모든 취약점을 점검할 수 없다는 뜻
    
    return answer