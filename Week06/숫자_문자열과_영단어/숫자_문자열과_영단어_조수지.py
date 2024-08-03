# 너무 무식하게 코드를 짠 거 같은데 더 복잡하게 생각하기가 싫다...

def solution(string) :
  s = ''
  answer = ''
  
  for i in range(len(string)) :
    s += string[i]
    
    if s == '0' or s == '1' or s == '2' or s == '3' or s == '4' or s == '5' or s == '6' or s == '7' or s == '8' or s == '9' :
      answer += s
      s = ''
    
    elif s == 'zero' :
      answer += '0'
      s = ''
      
    elif s == 'one' :
      answer += '1'
      s = ''
      
    elif s == 'two' :
      answer += '2'
      s = ''
      
    elif s == 'three' :
      answer += '3'
      s = ''
      
    elif s == 'four' :
      answer += '4'
      s = ''
      
    elif s == 'five' :
      answer += '5'
      s = ''
      
    elif s == 'six' :
      answer += '6'
      s = ''
      
    elif s == 'seven' :
      answer += '7'
      s = ''
      
    elif s == 'eight' :
      answer += '8'
      s = ''
      
    elif s == 'nine' :
      answer += '9'
      s = ''
      
  return int(answer)