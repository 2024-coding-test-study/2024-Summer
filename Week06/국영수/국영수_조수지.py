n = int(input())  # 학생 수 입력받기

stu = []

for i in range(n) :
    INPUT = input().split()
    scores = list(map(int, INPUT[1:]))
    stu.append((INPUT[0], scores[0], scores[1], scores[2]))  # 튜플로 stu에 추가

# 국어 내림차, 영어 오름차, 수학 내림차, 이름 오름차순으로 정렬하는 버블 정렬
# 버블 정렬 사용 시, 시간 초과
# sys.stdin.readline이나 pypy3도 시간 초과
'''for i in range(n) :
    for j in range(n - 1 - i) :
        if (stu[j][1] < stu[j + 1][1] or # i번째의 국어 점수가 더 낮거나
            (stu[j][1] == stu[j + 1][1] and stu[j][2] > stu[j + 1][2]) or # 국어 점수는 같지만 영어 점수가 높거나
            (stu[j][1] == stu[j + 1][1] and stu[j][2] == stu[j + 1][2] and stu[j][3] < stu[j + 1][3]) or # 국어, 영어 점수는 같지만 수학 점수가 낮거나
            (stu[j][1] == stu[j + 1][1] and stu[j][2] == stu[j + 1][2] and stu[j][3] == stu[j + 1][3] and stu[j][0] > stu[j + 1][0])) : # 모든 점수가 같지만 이름이 더 빠르면
            stu[j], stu[j + 1] = stu[j + 1], stu[j]  # 값 교환'''

stu.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

for i in range(n) :
    print(stu[i][0])
