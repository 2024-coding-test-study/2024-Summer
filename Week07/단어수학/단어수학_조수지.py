import sys

n = int(input())
words = [sys.stdin.readline().strip() for _ in range(n)]
alpa_value = {} # 각 알파벳이 얼마나 중요한지 나타낼 딕셔너리

for word in words :
    x = len(word) - 1
    
    for i in word :
        if i in alpa_value : # 딕셔너리에 해당 알파벳이 존재하면 더해줌
            alpa_value[i] += 10 ** x
        else : # 딕셔너리에 해당 알파벳이 없으면 해당 값 위치에 더해줌
            alpa_value[i] = 10 ** x
        
        x -= 1 # 다음 자릿수로 넘어가기
        
weight = sorted(alpa_value.values(), reverse=True) # 가중치의 내림차순으로 정렬

result = 0
num = 9

for i in weight :
    result += i * num # 가장 가중치가 큰 알파벳부터 9, 8, 7,... 씩 지정해 결과값에 더해줌
    num -= 1
    
print(result)