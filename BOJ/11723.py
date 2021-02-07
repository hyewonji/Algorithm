'''
집합


다음의 규칙을 구현하는 프로그램을 작성해라
1. add x: S에 x를 추가한다. (1 ≤ x ≤ 20) S에 x가 이미 있는 경우에는 연산을 무시한다.
2. remove x: S에서 x를 제거한다. (1 ≤ x ≤ 20) S에 x가 없는 경우에는 연산을 무시한다.
3. check x: S에 x가 있으면 1을, 없으면 0을 출력한다. (1 ≤ x ≤ 20)
4. toggle x: S에 x가 있으면 x를 제거하고, 없으면 x를 추가한다. (1 ≤ x ≤ 20)
5. all: S를 {1, 2, ..., 20} 으로 바꾼다.
6. empty: S를 공집합으로 바꾼다. 
'''

import sys

T=int(sys.stdin.readline())
S=0

for _ in range(T):
    opcodeStr=sys.stdin.readline()
 
    opcode=opcodeStr.split()[0]
    if opcode=="add":
        S |= 1<<int(opcodeStr.split()[1])
    elif opcode=="remove":
        S &= ~(1<<int(opcodeStr.split()[1]))
    elif opcode=="check":
        if S & (1<<int(opcodeStr.split()[1])):
            print(1)
        else:
            print(0)
    elif opcode=="toggle":
        S ^= (1<<int(opcodeStr.split()[1]))
    elif opcode=="all":
        S=(1<<21)-1
    elif opcode=="empty":
        S=0
