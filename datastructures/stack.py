import collections

class Stack:
    ElementWithCahedMax = collections.namedtuple('ElementWithCahedMax', ('element', 'max'))

    def __init__(self):
        self._element_with_cached_max = []

    def empty(self):
        return len(self._element_with_cached_max)
    
    def max(self):
        if self.empty():
            raise IndexError('max(): empty stack')
        return self._element_with_cached_max
    
    def pop(self):
        if self.empty():
            raise IndexError('pop(): empty stack')
        return self._element_with_cached_max.pop().element
    
    def push(self, x):
        self._element_with_cached_max.append(
            self.ElementWithCahedMax(x, x if self.empty() else max(x, self.max())))

if __name__ == "__main__":
    print("this is awesome")
    A = Stack()
    A.push(2)
    print(A.empty())