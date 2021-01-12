'''
크레인 인형뽑기 게임
'''


def solution(board, moves):

    arry = []
    for i in moves:
      for j in range(len(board)):
        if board[j][i-1] != 0:
          arry.append(board[j][i-1])
          board[j][i-1] = 0
          break

    r = 0
    n = 1
    while n < len(arry):
        if arry[n] == arry[n-1]:
          r += 2
          del arry[n]
          del arry[n-1]
          if n != 1:
            n -= 1
        else:  
          n += 1  
    return r


'''
stack을 사용해서 푸는 방법
'''
def solution(board, moves):
    stacklist = []
    answer = 0

    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:
                stacklist.append(board[j][i-1])
                board[j][i-1] = 0

                if len(stacklist) > 1:
                    if stacklist[-1] == stacklist[-2]:
                        stacklist.pop(-1)
                        stacklist.pop(-1)
                        answer += 2     
                break

    return answer
