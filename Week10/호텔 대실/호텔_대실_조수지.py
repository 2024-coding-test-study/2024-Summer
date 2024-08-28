# 너무너무 어렵당.......... 답을 봐도 잘 이해가 되지 않음...

# book_time 문자열을 시간으로 바꾸는 함수
def str_to_time(str_time: str) -> int :
  return int(str_time[0:2]) * 60 + int(str_time[3:]) # 분으로 치환해서 반환해줌

def solution(book_time) :
  book_times = sorted([[str_to_time(i[0]), str_to_time(i[1]) + 10] for i in book_time])
  
  rooms = []
  
  # 정수로 변환된 시간에 대하여 반복
  for book_time in book_times :
    if not rooms : # 아직 아무 예약도 받지 않았을 때
      rooms.append(book_time) # 추가해줌
      
      continue # 다음 예약으로 넘어감
    
    for idx, room in enumerate(rooms) : # enumerate는 인덱스 값을 얻을 수 있음
      if book_time[0] >= room[-1] : # 다음 예약 시작 시간이 배정된 방의 종료 시간보다 이후라면
        rooms[idx] = room + book_time # 다음 예약의 종료 시간으로 업데이트
        
        break
      
    # 이 else는 for idx, room .... 과 이어짐. break로 중단되지 않았을 경우 실행.
    else : # 겹치는 예약 시간이라면
      rooms.append(book_time) # 추가해줌
      
  return len(rooms) # 사용된 방의 개수 출력