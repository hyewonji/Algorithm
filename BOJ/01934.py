'''
T개의 줄에 A와 B의 최소공배수를 입력받은 순서대로 한 줄에 하나씩 출력하는 프로그램을 작성하라
'''

# math모듈의 최대공약수 구해주는 gcd함수를 import한다.
from math import gcd

T = int(input())
for i in range(T):
  A, B = map(int,input().split())
  # 최소공배수 == (두 수의 곱)/(두 수의 최대공약수)
  # 정수로 나타내기 위해 '/' 대신 '//'을 사용한다.
  print(A*B//gcd(A,B))
