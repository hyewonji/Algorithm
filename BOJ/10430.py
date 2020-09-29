'''
(A+B)%C는 ((A%C) + (B%C))%C 
(A×B)%C는 ((A%C) × (B%C))%C 
를 구해라
'''

A, B, C = list(map(int,input().split()))
print((A+B)%C)
print(((A%C) + (B%C))%C)
print((A*B)%C)
print(((A%C) * (B%C))%C)
