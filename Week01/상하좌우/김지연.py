#L(0, -1)
#R(0, 1)
#U(-1,0)
#D(1,0)
#풀이시간: 22m 45s
#오타 + 문제 잘 읽지 않아서 처음 시작점이 0, 0인줄 알았음
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
start = [1, 1]
n = int(input())
data = list(input().split())
nx = 1
ny = 1
for i in data:
    if i == 'L':
        nx = start[0] + dx[0]
        ny = start[1] + dy[0]
    elif i == 'R':
        nx = start[0] + dx[1]
        ny = start[1] + dy[1]
    elif i == 'U':
        nx = start[0] + dx[2]
        ny = start[1] + dy[2]
    elif i == 'D':
        nx = start[0] + dx[3]
        ny = start[1] + dy[3]
    if  1 > nx or n < nx or 1 > ny or n < ny:
        continue

    start[0] = nx
    start[1] = ny

print(*start)

