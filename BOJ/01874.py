'''
스택을 사용해 주어진 수열 만들기
push : +로 출력
pop : -로 출력
불가능할 경우 : No로 출력
'''


n = int(input())

count = 1
stack = []
result = []

for i in range(1,n+1):
  data = int(input())

  while count <= data:
    stack.append(count)
    count += 1
    result.append("+")
  if stack[-1] == data:
    stack.pop()
    result.append("-")
  else:
    print("No")
    exit(0)


print('\n'.join(result))
