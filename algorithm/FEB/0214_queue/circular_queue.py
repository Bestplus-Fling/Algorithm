class CircularQueue:
    def __init__(self, capacity=10):
        self.capacity = capacity + 1    # 설정한 용량보다 1칸 더 크게 설정한다
        self.items = [None] * self.capacity
        self.front = 0  # 큐의 맨 앞 요소 포인터
        self.rear = 0   # 큐의 맨 뒤 요소 포인더

    def is_full(self):
        # rear 다음이 front면 꽉 찬거다
        return (self.rear + 1) % self.capacity == self.front

    def enqueue(self, item):
        if self.is_full():
            raise IndexError("큐가 가득 찼습니다.")
        self.rear = (self.rear + 1) % self.capacity
        self.items[self.rear] = item

    def is_empty(self):
        return self.rear == self.front

    def dequeue(self):
        if self.is_empty():
            raise IndexError("큐가 비어있습니다.")

        self.front = (self.front + 1) % self.capacity
        item = self.items[self.front]
        self.items[self.front] = None
        return item

    def peek(self):
        if self.is_empty():
            raise IndexError("큐가 비어있습니다.")

        return self.items[(self.front + 1) % self.capacity]