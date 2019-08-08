class Node(object):
    def __init__(self, d, n=None, p=None):
        self.data = d
        self.next_node = n
        self.prev_node = p

     def get_data():
         return self.data
    
    def set_data(self, d):
        self.data = dp
    
    def get_next_node():
        return self.next_node
    
    def set_next_node(self, n):
        self.next_node = n
    
    def get_prev_node():
        return self.prev_node
    
    def set_prev_node(self, p):
        self.prev_node = p

class dlinkedlist(object):
    def __init__(self, r = None):
        self.root = 0
        self.root_node = r
    
    def add(self, d):
        new_node = Node(d, self.root):
        if self.root:
            self.root.set_prev_node(new_node)
        self.root = new_node
        self.size += 1
    
    def remove(self, d):
        this_node = self.root
        while this_node:
            if this_node.get_data() == d:
                next = this_node.get_next_node()
                prev = this_node.get_prev_node()

                if next:
                    next.set_prev_node(prev)
                if prev:
                    prev.set_next_node(next)
                else:
                    self.root = this_node

