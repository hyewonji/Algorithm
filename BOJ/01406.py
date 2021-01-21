'''
Stack

영어 소문자만을 기록할 수 있는 편집기이다.
 - L : 커서를 왼쪽으로 한 칸 옮김 (커서가 문장의 맨 앞이면 무시됨)
 - D : 커서를 오른쪽으로 한 칸 옮김 (커서가 문장의 맨 뒤이면 무시됨)
 - B : 커서 왼쪽에 있는 문자를 삭제함 (커서가 문장의 맨 앞이면 무시됨)
       삭제로 인해 커서는 한 칸 왼쪽으로 이동한 것처럼 나타나지만, 실제로 커서의 오른쪽에 있던 문자는 그대로임
 - P $ : $라는 문자를 커서 왼쪽에 추가함
 
 첫째 줄에는 초기에 편집기에 입력되어 있는 100,000을 넘지 않은 문자열이 주어진다. 
 둘째 줄에는 입력할 명령어의 개수를 나타내는 정수 M(1 ≤ M ≤ 500,000)이 주어진다.
 ---------------------------------------------------------------------------------------
 
 배열 2개를 이용해서 커서이동을 나타낸다.
 pop : 배열의 마지막 요소를 출력하고 제거한다.
 
 '''

import sys

stk1 = list(input())
stk2 = []
M = int(input())

for i in range(M):
  k = sys.stdin.readline().split()
  if k[0] == 'L' :
    if stk1: stk2.append(stk1.pop())
    else: continue
  elif k[0] == 'D':
      if stk2: stk1.append(stk2.pop())
      else: continue
  elif k[0] == 'B':
      if stk1: stk1.pop()
      else: continue
  elif k[0] == 'P':
      stk1.append(k[1])
print(''.join(stk1 + list(reversed(stk2))))
