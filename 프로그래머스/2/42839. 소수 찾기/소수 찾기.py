import math
from itertools import permutations

def solution(numbers):
    answer = 0
    lst = list(numbers)
    length = len(lst)
    s = set([])
    for i in range(1, length + 1):
        for elem in permutations(lst, i):
            s.add(int("".join(elem)))
    def find_prime(n):
        if n == 0 or n == 1:
            return 0
        else:
            sqt = int(math.sqrt(n))
            for i in range(2, sqt + 1):
                if n % i == 0:
                    return 0
            return 1
    for num in s:
        answer += find_prime(num)
    
    
    return answer