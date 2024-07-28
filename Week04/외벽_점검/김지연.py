from itertools import permutations

def solution(n ,weak, dist):
    #원형을 2배로 키워서 선형으로 만들기 -> 하는 이유: start를 다르게 해서 친구들의 순열을 하나씩 검사해보기 위함
    length = len(weak)
    for i in range(length):
        weak.append(weak[i] + n)

    # answer는 최소의 친구수를 찾는 것이므로 최대값으로 초기화
    answer = len(dist) + 1 #친구수 + 1

    #친구를 무작위로 나열하는 모든 경우의 수
    dist_n = list(permutations(dist, len(dist)))
    
    #start위치를 모두 다르게 설정해서 친구를 나열해보자. 나열하면서 중간에 친구 투입이 필요없으면 종료하고 answer에 저장
    for start in range(length):
        for friends in dist_n:
            count = 1 #먼저 친구 한명 투입

            #start를 기준으로 친구들의 모든 무작위 순열을 나열해보자
            #각 친구의 마지막 점검 위치를 기준으로 취약점의 어느 위치까지 점검할 수 있는지 확인하는 과정 필요
            position = start + friends[count-1] #마지막 점검위치
            for index in range(start, start + length): #취약점의 어느 위치까지 점검가능한가
                if position < weak[index]:
                    #마지막 점검 위치가 취약점에 도달하지 못함 -> 다음 친구 투입필요
                    #근데 투입할 사람이 더 없다면
                    if count > len(dist):
                        break
                    count += 1
                    position = weak[index] + friends[count-1] #다음 친구의 마지막 점검 위치
            answer = min(answer, count)
    if answer > len(dist): #만약에 answr가 초기 설정 값과 동일하면 투입할 친구가 없다는 뜻임
        return -1
    else:
        return answer

print(solution())