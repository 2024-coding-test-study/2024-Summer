from bisect import bisect_left, bisect_right # 이진탐색 가져오기

def solution(words, queries) :
  answer = []
  
  arr = [[] for _ in range(10001)] # 단어의 최대 길이가 10000이기에 이렇게 초기화
  reverse_arr = [[] for _ in range(10001)]
  
  for word in words : # 각 단어를 길이에 따라 리스트에 저장해 줌
    arr[len(word)].append(word)
    reverse_arr[len(word)].append(word[::-1]) # 얘는 뒤집어서 저장
    
  for i in range(10001) : # 길이의 오름차순으로 정렬
    arr[i].sort()
    reverse_arr[i].sort()
    
  # 이분 탐색
  # froaa <= fro?? <= frozz
  # ????o : oaaaa <= 0???? <= ozzzz. 접두사에 와일드카드 문자가 있으므로 리버스 배열에서 수행.
  for q in queries :
    qA = q.replace('?', 'a') # 단어가 소문자로만 이루어져 있으므로 가장 작은 알파벳인 a로 ?를 치환
    qZ = q.replace('?', 'z') # 마찬가지로 가장 큰 알파벳인 z로 ?를 치환
    
    if q[0] == '?' : # '?'가 접두사 위치에 있으면
      start = bisect_left(reverse_arr[len(q)], qA[::-1])
      end = bisect_right(reverse_arr[len(q)], qZ[::-1])
      
      answer.append(end - start)
    
    else : # '?'가 접미사 위치에 있으면
      start = bisect_left(arr[len(q)], qA)
      end = bisect_right(arr[len(q)], qZ)
      
      answer.append(end - start)
      
  return answer