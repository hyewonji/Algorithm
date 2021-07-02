'''
분류 : 그리디(탐욕 기법)

▲ - 다음 알파벳
▼ - 이전 알파벳 (A에서 아래쪽으로 이동하면 Z로)
◀ - 커서를 왼쪽으로 이동 (첫 번째 위치에서 왼쪽으로 이동하면 마지막 문자에 커서)
▶ - 커서를 오른쪽으로 이동
조이스틱을 최소로 움직여 원하는 문자열을 만들어라
'''

def solution (name) :
    change = [min(ord(i) - ord('A'), ord('Z') - ord(i) + 1) for i in name]
    idx = 0
    answer = 0
    
    while True:
        answer += change[idx]
        change[idx] = 0
        if sum(change) == 0:
            return answer
        
        left, right = 1, 1
        while change[idx - left] == 0:
            left += 1
        while change[idx + right] == 0:
            right += 1
        
        answer += left if left < right else right
        idx += -left if left < right else right
        
