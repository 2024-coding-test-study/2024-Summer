def binary_search(start, end, target, count, words):
  word = target[0]
  start_idx = target[1]
  length = target[2]
  while True:
    if start > end:
      return count
      # print(count)


    mid = (start + end) // 2
   
 
    if word == str(words[mid][start_idx:start_idx+len(word)]):
        if length == len(words[mid]):
            print(start, end, mid)
            
            count += 1
            start += 1
          
            # print(words[mid][start_idx:start_idx+len(word)])
        elif length < len(words[mid]):
            end = mid - 1
        elif length > len(words[mid]):
            start = mid + 1

    elif word < str(words[mid][start_idx:start_idx+len(word)]): #두 
        # print(end)
        end = mid - 1
        

    elif word > str(words[mid][start_idx:start_idx+len(word)]):
        # print(start)
        start = mid + 1



def solution(words, queries):
  answer = []
  keyword = []
  words.sort()
  print(words)
  for i in queries:
      to_find = i.split("?")
      for k in range(len(to_find)):
          if to_find[k] != '':
              keyword.append((to_find[k], k, len(i)))

  for i in keyword:
      cnt = 0
      cnt = binary_search(0, len(words)-1, i, cnt, words)
      answer.append(cnt)

  return answer