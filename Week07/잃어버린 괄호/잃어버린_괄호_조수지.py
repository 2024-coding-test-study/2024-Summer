expression = input() # 식 입력받기

parts = expression.split('-') # -를 기준으로 식을 나눠서 저장

SUM = sum(map(int, parts[0].split('+'))) # 나눠진 식의 맨 첫부분은 모두 +연산자만 있을거니까 다 더해줌

for part in parts[1:] : # 나눈 식의 두번째 부분부터 끝까지 반복
  SUM -= sum(map(int, part.split("+")))
  
print(SUM)