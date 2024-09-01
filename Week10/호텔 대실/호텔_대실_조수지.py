# 문자열을 시간으로 바꿔주는 함수
def str_to_time(str_time) :
    return int(str_time[0:2]) * 60 + int(str_time[3:])

def solution(book_time) :
    # 예약 시작 시간을 기준으로 정렬하고 예약 종료 시간에는 10분을 더해 새로운 리스트 생성.
    book_times = sorted([[str_to_time(i[0]), str_to_time(i[1]) + 10] for i in book_time])
    
    rooms = [] # 배정 중인 방을 나타내는 리스트
    
    for book_time in book_times:
        earliest_end_time = float('inf') # 종료 시간이 가장 빠른 방을 찾기
        chosen_room_index = -1 # 선택한 방의 인덱스
        
        for idx, room in enumerate(rooms): # enumerate 함수는 인덱스를 반환해줌
          # 새로 배정할 방의 시작 시간이 이미 배정된 방의 종료 시간보다 이후이고
          # 이미 배정된 방의 종료 시간이 이미 배정된 방들 중 가장 빨리 끝난다면
            if book_time[0] >= room[-1] and room[-1] < earliest_end_time:
                earliest_end_time = room[-1] # 이미 배정된 방들 중 가장 빨리 끝나는 시간 갱신
                chosen_room_index = idx # 인덱스 갱신(가장 빨리 끝나는 방)
        
        if chosen_room_index != -1 : # 방이 선택된 경우, 해당 방의 종료 시간을 갱신
            rooms[chosen_room_index] = rooms[chosen_room_index] + book_time
        else : # 배정된 모든 방들과 시간이 겹친다면
            rooms.append(book_time) # 방추가
    
    return len(rooms)