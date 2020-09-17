'''
숫자 뒤집은 후 큰 숫자 출력

ex) 
입력 : 734 893
출력 : 437

-> 734는 437, 893은 398이 되므로 둘 중 큰 수는 437
'''

num = input().split()

A = int(num[0][::-1])
B = int(num[1][::-1])

if A>B:
  print(A)
else:
  print(B)
