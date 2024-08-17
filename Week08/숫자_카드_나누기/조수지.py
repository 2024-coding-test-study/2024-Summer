# all_no_div 함수에서 all을 쓰지 않고 for문을 써서 했더니 시간초과.
# 최대공약수를 for문으로 구하면 시간 초과.

import math
from functools import reduce

# 배열의 모든 수가 i로 나눠 떨어지지 않는지 확인하는 함수
def all_no_div(i, nums):
    return all(num % i != 0 for num in nums)   
  
# 최대공약수 구하기
def GCD(arr) :
    return reduce(math.gcd, arr) # reduce를 쓰면 배열에 대한 최대공약수를 구할 수 있음
        
def solution(arrayA, arrayB):
    Anum = GCD(arrayA) # arrayA의 최대공약수
    Bnum = GCD(arrayB) # arrayB의 최대공약수
    
    # 각 배열의 최소공약수가 존재하고 이 수가 다른 배열의 모든 수를 나눌 수 없을 때
    if (Anum != 1 and all_no_div(Anum, arrayB)) and (Bnum != 1 and all_no_div(Bnum, arrayA)) :
      return(max(Anum, Bnum)) # 둘 중에 더 큰 수를 출력
    
    elif Anum != 1 and all_no_div(Anum, arrayB) : # 만약 배열A의 최대공약수가 존재하고 이 수가 배열B의 모든 수를 나누지 못한다면
        return Anum
        
    elif Bnum != 1 and all_no_div(Bnum, arrayA) : # 만약 배열B의 최대공약수가 존재하고 이 수가 배열A의 모든 수를 나누지 못한다면
        return Bnum
    
    else :
        return 0
      
# 유클리드 호제법 이용한 코드
'''
import math

# 배열의 모든 수가 i로 나눠 떨어지지 않는지 확인하는 함수
def all_no_div(i, nums):
    return all(num % i != 0 for num in nums)   

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def gcd_of_array(arr):
    result = arr[0]
    
    for num in arr[1:]:
        result = gcd(result, num)
        
    return result
        
def solution(arrayA, arrayB):
    Anum = gcd_of_array(arrayA) # arrayA의 최대공약수
    Bnum = gcd_of_array(arrayB) # arrayB의 최대공약수
    
    # 각 배열의 최소공약수가 존재하고 이 수가 다른 배열의 모든 수를 나눌 수 없을 때
    if (Anum != 1 and all_no_div(Anum, arrayB)) and (Bnum != 1 and all_no_div(Bnum, arrayA)) :
      return(max(Anum, Bnum)) # 둘 중에 더 큰 수를 출력
    
    elif Anum != 1 and all_no_div(Anum, arrayB) : # 만약 배열A의 최대공약수가 존재하고 이 수가 배열B의 모든 수를 나누지 못한다면
        return Anum
        
    elif Bnum != 1 and all_no_div(Bnum, arrayA) : # 만약 배열B의 최대공약수가 존재하고 이 수가 배열A의 모든 수를 나누지 못한다면
        return Bnum
    
    else :
        return 0
'''  