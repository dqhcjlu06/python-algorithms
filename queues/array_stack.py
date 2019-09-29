from mybase.exceptions import EmptyError
class ArrayStack:
    """LIFO Stack"""

    def __init__(self):
        self._data = []
    
    def __len__(self):
        return len(self._data)
    
    def is_empty(self):
        return len(self._data) == 0
    
    def push(self, e):
        self._data.append(e)
    
    def top(self):
        if self.is_empty():
            raise EmptyError('Stack is empty')
        return self._data[-1]
    
    def pop(self):
        if self.is_empty():
            raise EmptyError('Stack is empty')
        return self._data.pop()

if __name__ == '__main__':
    S = ArrayStack()
    S.push(5)
    S.push(3)
    print(len(S))
    print(S.pop())
    print(S.is_empty())
    print(S.pop())
    print(S.is_empty())
    S.push(7)
    print(len(S))
