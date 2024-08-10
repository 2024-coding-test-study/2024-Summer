n, c = map(int, input().split())
loc = []
for _ in range(n):
    loc.append(int(input()))

loc.sort()

start, end = 1, loc[-1] - loc[0]  # 가능한 최소, 최대 거리

result = 0
mid = (start + end) // 2
while True:
     #gap이 가장 넓은 경우가 (가장 긴 gap)/2이니까 mid를 초반에 설정해 놓고, 가장 인접한 것 중 최대 값을 구하는 것이니까 gap을
    current = loc[0]
    count = 1  # 첫 번째 위치에 공유기를 설치했다고 가정

    for i in range(1, n):
        if loc[i] - current >= mid:
            count += 1
            current = loc[i]
    if c == count:
        result = mid  # 가능한 최대 거리를 업데이트
        break
       
    else:
        mid = mid - 1

print(result)