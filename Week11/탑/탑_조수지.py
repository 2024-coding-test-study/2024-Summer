n = int(input()) # 탑의 수
input_buildings = input()

buildings = list(map(int, input_buildings.split()))

result = [0] * n
stack = []

for i in range(n) :
    while stack and buildings[i] > buildings[stack[-1]] : # 스택이 비어있지 않고 스택의 꼭대기보다 현재 탑이 더 크다면
        stack.pop() # 없애줌

    if stack : # 스택이 비어있지 않다면
        result[i] = stack[-1] + 1
    else : # 스택이 비어있다면
        result[i] = 0 # 현재 빌딩이 처음이거나 가장 높다는 뜻이므로 수신할 수 없음

    stack.append(i)

# 스택 사용 x. 시간 초과
'''for i in range(n - 1, -1, -1) : # 역으로 순환
    idx = i - 1

    while 1 :
        if idx < 0 :
            result[i] = 0
            break

        if buildings[idx] > buildings[i] :
            result[i] = idx + 1
            break
        else :
            idx -= 1'''


for i in range(n) :
    print(result[i], end = ' ')