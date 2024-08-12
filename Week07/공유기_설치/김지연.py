n, c = map(int, input().split())
loc = []
for _ in range(n):
    loc.append(int(input()))

loc.sort()

start, end = 1, loc[-1] - loc[0]  # 가능한 최소, 최대 거리

result = 0

while start <= end:
    mid = (start + end) // 2 
    #가장 작은 gap과 가장 큰 gap에서 가장 인전한 gap중에서 가장 큰 gap은 (가장 작은 gap + 가장 큰 gap) // 2 일 수 밖에 없음
    current = loc[0]
    count = 1  # 첫 번째 위치에 공유기를 설치했다고 가정

    for i in range(1, n):
        if loc[i] - current >= mid:
            count += 1
            current = loc[i]

    if count >= c:
        result = mid  # 가능한 최대 거리를 업데이트
        start = mid + 1
    else:
        end = mid - 1

print(result)
