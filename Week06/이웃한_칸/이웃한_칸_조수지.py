# 문제에서 제시한 방법과 같음

def solution(board, h, w):
    answer = 0
    dh = [0, 1, -1, 0]
    dw = [1, 0, 0, -1]
    
    
    for i in range(4) :
      h_check, w_check = h + dh[i], w + dw[i]
      
      if 0 <= h_check < len(board) and 0 <= w_check < len(board) :
        if board[h][w] == board[h_check][w_check] :
          answer += 1
      
    return answer