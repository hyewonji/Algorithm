'''
deque 구현
1. push_front X: 정수 X를 덱의 앞에 넣는다.
2. push_back X: 정수 X를 덱의 뒤에 넣는다.
3. pop_front: 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
4. pop_back: 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
5. size: 덱에 들어있는 정수의 개수를 출력한다.
6. empty: 덱이 비어있으면 1을, 아니면 0을 출력한다.
7. front: 덱의 가장 앞에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
8. back: 덱의 가장 뒤에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
'''


import sys

N = int(sys.stdin.readline().rstrip())
deq = []

def push_front(x):
    deq.insert(0,x)

def push_back(x):
    deq.append(x)    

def pop_front():
    if(not deq):
        return -1
    else:
        return deq.pop(0)

def pop_back():
    if(not deq):
        return -1
    else:
        return deq.pop()

def size():
    return len(deq)

def empty():
    return 0 if deq else 1

def front():
    return deq[0] if deq else -1

def back():
    return deq[-1] if deq else -1


for _ in range(N):
    input_split = sys.stdin.readline().rstrip().split()

    order = input_split[0]

    if order == "push_front":
        push_front(input_split[1])
    elif order == "push_back":
        push_back(input_split[1])
    elif order == "pop_front":
        print(pop_front())
    elif order == "pop_back":
        print(pop_back())
    elif order == "size":
        print(size())
    elif order == "empty":
        print(empty())
    elif order == "front":
        print(front())
    elif order == "back":
        print(back())
