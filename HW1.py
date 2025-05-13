from collections import deque

queue = deque([1,4,2,7,9])
print("Original Queue:  ", list(queue))

def rev(queue):
    stack = []

    #Dequeue all elements from the queue and push them onto the stack
    while queue:
        stack.append(queue.popleft())

    #Pop all elements from the stack and enqueue them back to the queue
    while stack:
        queue.append(stack.pop())
    
    return queue

reve = rev(queue)
print("Reversed Queue", list(reve))