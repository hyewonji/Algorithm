'''
valid-parentheses
스텍 구현

입력된 s문자열의 (),[],{}를 삭제했을때 s가 빈 문자열이 되면 true, 아니면 false를 반환한다.
'''

class Solution(object):
    def isValid(self, s ) :
        stack = []
        table = {
            ')':'(',
            '}':'{',
            ']':'['
        }
        
        for i in s:
            if len(stack) == 0:
                stack.append(i)
            elif i not in table:
                stack.append(i)
            else:
                if table[i] == stack[len(stack)-1]: 
                    stack.pop()
        
        if len(stack) == 0:
            s = ''

        return s == ''
