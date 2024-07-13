n = int(input())
time = [0] * (n + 1) # 각 작업의 기본 시간 저장할 리스트
complete_time = [0] * (n + 1)  # 각 작업의 총 완료 시간을 저장할 리스트

for i in range(1, n + 1):
    n_class = list(map(int, input().split())) # 입력받은 각 줄을 리스트에 저장
    time[i] = n_class[0] # 각 줄의 첫번째 수는 소요 시간이기에 시간 리스트에 저장
    
    for j in range(1, len(n_class)):
        if n_class[j] == -1:
            continue
        else:
            complete_time[i] = max(complete_time[i], time[i] + complete_time[n_class[j]])
    
    complete_time[i] = max(complete_time[i], time[i])  # 자신만의 시간만 있는 경우
    
    print(complete_time[i])