import time


class ListQueue:
    def __init__(self):
        self.items = []
        self.size = 0

    def enqueue(self, data):
        self.items.insert(0, data)
        self.size += 1

    def dequeue(self):
        data = self.items.pop()
        self.size -= 1
        return data

    def size(self):
        return self.size




def main():
    list_queue = ListQueue()
    start_time = time.time()
    for i in range(100000):
        list_queue.enqueue(i)
    for i in range(100000):
        list_queue.dequeue()
    print("----- %s seconds ----" % (time.time() - start_time))

if __name__ == "__main__":
    main()
