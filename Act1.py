#Queue: FIFO (First In First Out) or LILO (Last In Last Out)

class Queue:
    def __init__(self):
        self.queue = []
    
    #enqueue - add value to queue
    def enqueue(self, item):
        self.queue.append(item) #append to add to list
    
    #dequeue - remove values from queue
    def dequeue(self):
        if len(self.queue)<1:
            return None
        return self.queue.pop(0)
    
    def display(self):
        print(self.queue)

    def size(self):
        return len(self.queue)
    
q = Queue()
q.enqueue(5)
q.enqueue(4)
q.enqueue(0)
q.enqueue(8)
q.enqueue(2)
q.display()
print(q.size())
q.dequeue()
q.display()