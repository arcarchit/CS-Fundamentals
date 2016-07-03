from collections import deque

queue = deque(["hellp", "how", "are", "you"])
queue.append("fine")
queue.append("what")
print queue
print queue.popleft()
print queue.pop()
print queue
