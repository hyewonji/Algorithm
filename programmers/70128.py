'''
주어진 길이가 같은 배열 a, b의 내적을 구하는 프로그램을 작성하라
'''

def solution(a, b):
    r = 0
    for i in range(len(a)):
        r += a[i]*b[i]
    return r

'''
zip함수 사용해서 작성

def solution(a, b):
    return sum([x*y for x, y in zip(a,b)])
'''
