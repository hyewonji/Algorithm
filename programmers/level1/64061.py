'''
크레인 인형뽑기 게임
'''

def solution(board, moves):

    arry = []
    for i in moves:
      for j in range(len(board)):
        s = board[j][i-1]
        if s != 0:
          arry.append(s)
          board[j][i-1] = 0
          break

    r = 0
    n = 1
    while n < len(arry):
        if arry[n] == arry[n-1]:
          r += 1
          del arry[n]
          del arry[n-1]
          if n != 1:
            n -= 1
        else:  
          n += 1  
    return r*2
