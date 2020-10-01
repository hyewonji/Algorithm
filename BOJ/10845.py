'''
queue 구현
1. push X: 정수 X를 큐에 넣는 연산이다.
2. pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
3. size: 큐에 들어있는 정수의 개수를 출력한다.
4. empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
5. front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
6. back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
'''


import sys

N = int(sys.stdin.readline().rstrip())
stack = []

def push(x):
    stack.append(x)

def pop():
    if(not stack):
        return -1
    else:
        return stack.pop(0)
        

def size():
    return len(stack)

def empty():
    return 0 if stack else 1

def front():
    return stack[0] if stack else -1

def back():
    return stack[-1] if stack else -1


for _ in range(N):
    input_split = sys.stdin.readline().rstrip().split()

    order = input_split[0]

    if order == "push":
        push(input_split[1])
    elif order == "pop":
        print(pop())
    elif order == "size":
        print(size())
    elif order == "empty":
        print(empty())
    elif order == "front":
        print(front())
    elif order == "back":
        print(back())
