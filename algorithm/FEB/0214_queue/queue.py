class Queue:
    def __init__(self, capacity=10):
        self.capacity = capacity # 큐의 크기
        self.items = [None] * capacity # 큐를 저장할 리스트를 None으로 초기화
        self.front = -1 # 맨 앞의 요소를 가리키는 포인터
        self.rear = -1 # 맨 뒤의 요소 포인터

    def is_full(self):
        return  self.rear == self.capacity - 1

    # 큐의 데이터를 삽입하는 메서드
    def enqueue(self, item):
        if self.is_full():
            raise IndexError("Queue is full")
        # rear의 다음 칸에 데이터를 삽입
        self.rear += 1
        self.items[self.rear] = item

    # 비어있는지 확인하는 메서드
    def is_empty(self):
        return self.rear == self.front

    def dequeue(self):
        if self.is_empty():
            raise IndexError("큐가 비어있습니다!")
        self.front += 1
        item = self.items[self.front]
        self.items[self.front] = None
        return item

    def peek(self):
        if self.is_empty():
            raise IndexError("큐가 비어있습니다!")
        return self.items[self.front + 1]
