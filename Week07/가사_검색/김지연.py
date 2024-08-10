def binary_search(start, end, target, words):
    #target이 정렬된 words 어디에 위치해야하는지 탐색

    while start < end:
        mid = (start + end) // 2

        if words[mid] < target:
            start = mid + 1
        elif words[mid] > target:
            end = mid #mid-1을 하지 않는 이유는 target이 words[mid]보다 작을경우 target은 words의 mid에 위치해야한다. 그래야 words[mid]의 값이 target뒤에 위치하게 된다.
    return start #start가 end보다 커지면 탐색을 모두 마친것이고 start의 위치가 target이 words에 위치할 인덱스가 된다.
    
            

    
def solution(words, queries):
    answer = []
    words.sort()
    words_reversed = []
    for word in words:
        words_reversed.append(word[::-1])
    words_reversed.sort()

    #길이에 따라 리스트를 따로 두어서 비교해야함!!!
    words_length = [[] for i in range(10001)]
    for word in words:
        words_length[len(word)].append(word)
    #접미사 탐색을 위한 word reverse 리스트 만들기
    
    words_reverse = [[] for i in range(10001)]
    for word in words_reversed:
        words_reverse[len(word)].append(word)
    
    #queries에서 ?를 a와 z로 바꾸고 각각 탐색
    for target in queries:
        #이렇게하는건 전치사일 경우 상관없는데 접두사일 경우는...? 접두사는 문자열 뒤집어서 탐색
        if target[0] == '?': #접미사이면
            left_target = target.replace('?', 'a')[::-1] #left = left_target이 words에서 위치한 인덱스 +1
            right_target = target.replace('?', 'z')[::-1] #right = right_tartget이 words에서 위치한 인덱스
            word_search = words_reverse[len(target)]
            # left_idx = binary_search(0, len(words_reverse[len(target)])-1, left_target[::-1], words_reverse[len(target)])
            # right_idx = binary_search(0, len(words_reverse[len(target)])-1, right_target[::-1], words_reverse[len(target)]) + 1
        else:
            left_target = target.replace('?', 'a') #left = left_target이 words에서 위치한 인덱스 +1
            right_target = target.replace('?', 'z') #right = right_tartget이 words에서 위치한 인덱스
            word_search = words_length[len(target)]
        #right - left하면 words안에 target수를 구할 수 있다.
        # left, right 각각 이진탐색 시작
        left_idx = binary_search(0, len(word_search[len(target)])-1, left_target, word_search)
        right_idx = binary_search(0, len(word_search[len(target)])-1, right_target, word_search)

        answer.append(right_idx - left_idx)
        
                
    return answer