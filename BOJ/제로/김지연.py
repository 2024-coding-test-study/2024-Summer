#구현
# 재민이가 잘못된 수를 부를때마다 0외친다. -> 가장 최근에 재민이가 쓴 수를 지우게 한다.
# k번 반복하면서 0이 i번째이면 i-1수 지우기 ->0으로 만들기
k = int(input())
data = [int(input()) for _ in range(k)]

##최근에 쓴 순서로 삭제 -> 스택 (질문게시판 보고 떠올림)
lst = [] #k가 최대 100000이므로 리스트 2개 사용해도 충분함
for i in data:
  if i != 0:
    lst.append(i)
  else:
    lst.pop()
print(sum(lst))