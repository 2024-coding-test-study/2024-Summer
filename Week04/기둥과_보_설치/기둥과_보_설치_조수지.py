# 현재 설치된 구조물이 '가능한' 구조물인지 확인하는 함수
def possible(wall) :
    for x, y, a in wall :
        
        if a == 0: # 설치된 것이 '기둥'인 경우
            # '바닥 위' 혹은 '보의 한쪽 끝 부분 위' 혹은 '다른 기둥 위'라면 정상
            if y == 0 or [x - 1, y, 1] in wall or [x, y, 1] in wall or [x, y - 1, 0] in wall:
                continue
            
            return False # 설치될 수 없는 구조물이 설치되었다면 거짓을 반환
        
        elif a == 1 : # 설치된 것이 '보'인 경우
            # '한쪽 끝부분이 기둥 위' 혹은 '양쪽 끝부분이 다른 보와 동시에 연결'이라면 정상
            if [x, y - 1, 0] in wall or [x + 1, y - 1, 0] in wall or ([x - 1, y, 1] in wall and [x + 1, y, 1] in wall):
                continue
            
            return False # 설치될 수 없는 구조물이 설치되었다면 거짓을 반환
        
    return True

def solution(n, build_frame) :
    wall = [] # 현재 벽 상태를 나타낼 2차원 배열
    
    for i in range(len(build_frame)) :
        x, y, a, b = build_frame[i]
        
        if b == 1 : # 설치하는 경우
            wall.append([x, y, a]) # 일단 설치
            
            if not possible(wall) : # 가능한 구조물인지 확인
                wall.remove([x, y, a]) # 가능한 구조물이 아니라면 다시 제거
        
        if b == 0 : # 삭제하는 경우
            wall.remove([x, y, a]) # 일단 삭제
            
            if not possible(wall) : # 가능한 구조물인지 확인
                wall.append([x, y, a]) # 가능한 구조물이 아니라면 다시 설치
                
                
    return sorted(wall) # 정렬된 결과를 반환