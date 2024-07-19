# 2차원 배열로 어떻게든 해결해보고 싶었지만 실패...
# wall 배열 하나로만 표현할 수가 없는데...
# 두 개 이상의 배열을 사용해야하는 거라면 어떻게 구현하는것이냐... 으앙아아ㅏ아

def solution(n, build_frame):
    wall = [[0] * (n + 1) for _ in range(n + 1)]  # 보드 초기화
    
    for i in range(len(build_frame)) :
        x, y, a, b = build_frame[i] # build_frame 리스트의 i번째 요소를 각각 지정해줌
        
        if b == 1 : # 설치하는 경우
            if a == 0 : # 기둥을 설치하는 경우
                wall[x][y] 
                ...
                
            else : # 보를 설치하는 경우
                wall[x][y]
                ...
        
        else : # 삭제하는 경우
            if a == 0 : # 기둥을 삭제하는 경우
                wall[x][y]
                ...
                
            else : # 보를 삭제하는 경우
                wall[x][y]
                ...
    
    answer = [[]]
    
    return answer