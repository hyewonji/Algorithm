'''
1. 자연수 n을 3진법 변환
2. 3진법을 앞뒤로 뒤집는다.
3. 다시 10진법으로 변환
'''

def solution(n):
  ternary = ''
  answer = 0

  while n:
    ternary += str(n % 3)
    n = n//3

  for i,v in enumerate(ternary[::-1]):
    answer += (3**i)*int(v)

  return answer
