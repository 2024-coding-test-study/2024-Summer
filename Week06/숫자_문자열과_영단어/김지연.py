def solution(s):
    answer = ""
    #s 길이 50이므로 완전탐색 가능
    #영단어를 사전에 정의한 후 s에 해당 문자열을 찾아서 숫자로 반환
    #영단어 나오면 첫번째부터 하나씩 검사하다가 사전에 일치하는거 있으면 반환
    dict = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5","six":"6", "seven":"7", "eight":"8", "nine":"9"}
    
    word = ""
    for i in s:
        if 'a' <= i <= 'z':
            word += i
            if word in dict:
                answer += dict[word]
                word = ""
        else:
            answer += i
            
    return int(answer)
#two를 tow로 오타나서 테케 8,9에서 계속 오답이 뜸;; 
# s길이가 50 이하인데 성능 최적화문제는 전형 아닐거 같은데 혹시나 해서 다른 사람 코드 찾아보니까 나랑 비슷하게 풀었더라. chat gpt한테 물어보니 오타가 있다고 해서 고치고 제출하니까 바로 맞다고 뜸