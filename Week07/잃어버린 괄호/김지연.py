lst = input().split('-')

sum_num = 0
minus = 0
num = ''
data = []

for string in lst: 
  if '+' not in string:
    data.append(int(string))
    continue
  for j in range(len(string)):
    if string[j].isnumeric():
      num += string[j]
    if j == len(string)-1 or string[j].isnumeric() == False:
      sum_num += int(num)
      num = ''
  data.append(sum_num)
  sum_num = 0

minus = data[0]
for i in range(1, len(data)):
  minus -= data[i]
print(minus)
