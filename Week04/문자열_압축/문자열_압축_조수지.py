def solution(s):
    zip_len = []  # 압축한 문자열 길이 저장할 리스트 초기화

    for i in range(1, len(s) // 2 + 1):
        result = []  # 길이 i로 쪼개진 문자열 저장할 리스트 초기화

        for j in range(0, len(s), i):  # 길이 i로 문자열 쪼개기
            substring = s[j:j+i]
            result.append(substring)

        zip_result = []  # 압축한 문자열 저장할 리스트 초기화
        cnt = 1 # 연속된 동일한 문자열 개수 저장하는 변수

        for j in range(1, len(result)):
            if result[j] == result[j-1]: # 길이 i로 쪼갠 문자열의 j번째와 j-1번째가 같다면
                cnt += 1 # cnt에 1을 더해줌
                
            else: # j번째와 j-1번째가 다르고
                if cnt == 1: # cnt가 1이라면
                    zip_result.append(result[j-1]) # j-1번째 문자열을 압축한 문자열에 더해줌
                
                else: # cnt가 1을 초과한다면
                    zip_result.append(str(cnt)) # cnt를 압축한 문자열에 더해줌
                    zip_result.append(result[j-1]) # j-1번째 문자열도 더해주고
                    cnt = 1 # cnt를 다시 1로 바꿔줌
        
        # result 리스트의 마지막 요소에 대하여
        if cnt > 1:
            zip_result.append(str(cnt))
        
        zip_result.append(result[-1]) # result의 마지막 요소를 따로 zip_result 리스트에 저장해줌
        zip_len.append(len(''.join(zip_result))) # zip_result 리스트를 하나로 합친 다음, 길이를 저장

    answer = min(zip_len) # 최솟값 반환
    
    return answer