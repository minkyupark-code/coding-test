'''
초 단위로 기록된 주식가격이 담긴 배열 prices가 매개변수로 주어질 때, 가격이 떨어지지 않은 기간은 몇 초인지를 return 하도록 solution 함수를 완성하세요.
'''

def solution(prices):
    answer = [0] * len(prices)
    stack = []
    
    for i in range(len(prices)):
        while stack and prices[i] < prices[stack[-1]]:
            idx = stack.pop()
            answer[idx] = i - idx
        
        stack.append(i)
    
    while stack:
        idx = stack.pop()
        answer[idx] = len(prices) - idx - 1
    return answer