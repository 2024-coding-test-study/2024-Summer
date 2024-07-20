# 35분
s = list(map(int, input()))  # 입력된 문자열을 정수 리스트로 변환

count_0 = 0  # 연속된 0의 그룹 수
count_1 = 0  # 연속된 1의 그룹 수

for i in range(len(s)):
    if i == 0:  # 첫 번째 요소 처리
        if s[i] == 0:
            count_0 += 1
        else:
            count_1 += 1
    else:
        if s[i] != s[i-1]:  # 현재 요소가 이전 요소와 다르면
            if s[i] == 0:
                count_0 += 1
            else:
                count_1 += 1

# 더 적은 그룹의 수를 출력
print(min(count_0, count_1))