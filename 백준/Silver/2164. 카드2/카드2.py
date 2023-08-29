import sys

n = int(sys.stdin.readline().rstrip())
q = [i + 1 for i in range(n)]
front, rear = 0, 0

for _ in range(n - 1):
    q[rear] = q[(front + 1) % n]
    rear = (rear + 1) % n
    front = (front + 2) % n

print(q[front])