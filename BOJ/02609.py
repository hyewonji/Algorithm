'''
a, b를 입력받아
최대공약수와 최소공배수를 구해라
'''

from math import gcd

a, b = list(map(int,input().split()))
print(gcd(a,b))
print(a*b//gcd(a,b))
