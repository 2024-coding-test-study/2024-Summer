# dp 코드 이해하느라 미칠뻔 ㅠㅠ

t = int(input()) # 테스트 케이스 개수 입력받기

for _ in range(t):  # 테스트 케이스만큼 반복
    n, m = map(int, input().split())
    arr = [[0] * m for _ in range(n)]  # n*m 크기의 2차원 배열 초기화
    gold = list(map(int, input().split()))
    a = 0
    
    # 배열에 금 크기를 넣어줌
    for i in range(n):
        for j in range(m):
            arr[i][j] = gold[a]
            a += 1
    
    # 다이나믹 프로그래밍 진행
    for j in range(1, m):
        for i in range(n):
            # 왼쪽 위에서 오는 경우
            if i == 0: # 현재 칸이 가장 위이므로 더 위는 범위를 벗어남
                left_up = 0
            else:
                left_up = arr[i - 1][j - 1]
                
            # 왼쪽 아래에서 오는 경우
            if i == n - 1: # 현재 칸이 가장 아래이므로 더 아래는 범위를 벗어남
                left_down = 0
            else:
                left_down = arr[i + 1][j - 1]
                
            # 왼쪽에서 오는 경우
            left = arr[i][j - 1]
            arr[i][j] = arr[i][j] + max(left_up, left_down, left) # 현재 값에 가장 큰 값을 더해줌
    
    # 마지막 열에서 최댓값 찾기
    result = 0
    
    for i in range(n):
        result = max(result, arr[i][m - 1])
    
    print(result)
