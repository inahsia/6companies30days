from collections import deque 
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        queue=deque(range(1,n+1))
        while len(queue)>1:
            for _ in range(k-1):
                variable=queue.popleft()
                queue.append(variable)
            queue.popleft()

        return queue[0]