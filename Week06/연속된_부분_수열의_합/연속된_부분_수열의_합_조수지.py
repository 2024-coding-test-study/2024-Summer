def solution(sequence, k) :
    start, end = 0, 0 # 현재 부분 수열의 인덱스를 저장할 변수
    total = sequence[0]
    sequence += [0]
    best_start, best_end = 1000000, 2000000 # 합이 k인 부분 수열의 인덱스를 저장할 변수

    while end < len(sequence) - 1 : # end 값이 sequence를 벗어나지 않을 동안
        if total <= k : # 부분 수열의 합이 k보다 작거나 같을 때
            if total == k and end - start < best_end - best_start : # 합이 k고 이전에 찾은 수열보다 길이가 짧다면
                best_start, best_end = start, end # 인덱스 업데이트
                
            end += 1
            total += sequence[end]
            
        else : # 부분 수열의 합이 k보다 클 때
            start += 1
            total -= sequence[start - 1]

    return [best_start, best_end]