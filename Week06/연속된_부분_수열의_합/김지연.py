def solution(sequence, k):
    answer = []
    #sequence길이 100만 -> 완전탐색 가능 -> 100만 * 100만 이중 배열이므로 안됌...
    #사고과정: sequence를 idx=0부터 끝까지 idx=1부터 끝까지 ... idx끝부터 끝 까지 부분 수열 만들어서 k가 될 수 있는거 찾기
    #2차시도: 이중배열이면 시간초과나므로 .. 1개, 2개, 3개 ... len(sequence)개 씩 끊어서 k가 될 수 있는지확인 -> 1번이랑 똑같은 과정임..
    #오름차순은 인접한 두 수가 같을 수도 있는지 여부를 명확하게 알려주지 않지만 비내림차순은 같을 수도 있음을 명확히 해준 것
    #idx = 0 부터 계산하다가 k넘어가면 멈추고... idx=1 부터 계산하다가 k넘어가면 머추고... 원소가 1, k = 100만일 경우
    total = 0
    for i in range(len(sequence)):
        for j in range(i, len(sequence)):
            if i == j:
                if sequence[i] == k:
                    answer.append((0, i, j))
            elif sum(sequence[i:j+1]) == k:
                answer.append((j-i, i, j)) #j-i 수열길이도 같이 저장
    answer.sort()
    answer = answer[0][1:]
