import sys
from collections import deque

input = sys.stdin.readline

n = int(input())  # 보드 크기
k = int(input())  # 사과 개수
board = [[0] * n for _ in range(n)]  # 보드 초기화
directions = {}  # 방향 전환 정보를 저장할 딕셔너리

# 보드에 사과 위치 표시
for _ in range(k) :
    row, col = map(int, input().split())
    board[row - 1][col - 1] = 'a'

l = int(input())  # 뱀의 방향 전환 횟수

# 시간과 방향 입력받아 딕셔너리에 저장
for _ in range(l) :
    x, c = input().split()
    directions[int(x)] = c

# 방향 정보 (동, 남, 서, 북) <- 시계 방향으로 돌아가게
dir_x = [0, 1, 0, -1]
dir_y = [1, 0, -1, 0]

# 회전 함수 구현
def turn(direction, c) :
    if c == 'L' :
        direction = (direction - 1) % 4
        
    else :  
        direction = (direction + 1) % 4
        
    return direction

x, y = 0, 0 # 뱀의 시작 좌표
board[x][y] = 1  # 뱀의 몸을 1로 표시
snake = deque([(x, y)])  # 뱀의 위치를 저장할 큐
direction = 0  # 초기 방향이 오른쪽(동쪽)이므로 0으로 초기화
time = 0  # 시간 초기화

while True :
    time += 1
    x, y = snake[-1] # 뱀의 머리 좌표 저장
    nx, ny = x + dir_x[direction], y + dir_y[direction]

    # 벽이나 자기 자신에게 부딪히면 반복문 종료
    if nx < 0 or nx >= n or ny < 0 or ny >= n or board[nx][ny] == 1 :
        break
    
    if board[nx][ny] == 'a' : # 사과를 만나면
        board[nx][ny] = 1
        snake.append((nx, ny))
        
    else : # 이동한 위치에 사과가 없으면
        board[nx][ny] = 1
        snake.append((nx, ny))
        tail_x, tail_y = snake.popleft()  # 꼬리 제거
        board[tail_x][tail_y] = 0 # 꼬리 좌표 0으로 바꿔줌

    # 방향 전환 시간인지 확인하고 방향 전환
    if time in directions :
        direction = turn(direction, directions[time])

print(time)