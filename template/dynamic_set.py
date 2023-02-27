""""""


class DynamicSet:
    def search(self, k):
        pass

    def insert(self, x):
        pass

    def delete(self, k):
        pass

    def minimum(self):
        pass

    def maximum(self):
        pass

    def successor(self, x):
        pass

    def predecessor(self, x):
        pass


class EmptySetException(Exception):
    pass


class Stack(DynamicSet):
    def __init__(self):
        super(Stack, self).__init__()
        self._data = []
        self._top = 0

    def is_empty(self):
        return self._top == 0

    def push(self, x):
        self._top += 1
        self._data[self._top] = x

    def pop(self):
        if self.is_empty():
            raise EmptySetException()

        self._top -= 1
        return self._data[self._top + 1]


class Queue(DynamicSet):
    def __init__(self) -> None:
        super(Queue, self).__init__()

    def en_queue(self, x):
        pass

    def de_queue(self):
        pass


def main():
    print("hello, world")


if __name__ == "__main__":
    main()
