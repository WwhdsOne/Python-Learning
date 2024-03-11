class BPlusTree:
    def __init__(self, order):
        self.order = order
        self.root = BPlusTreeNode(order)

    def insert(self, key, value):
        self.root.insert(key, value)

    def search(self, key):
        return self.root.search(key)


class BPlusTreeNode:
    def __init__(self, order):
        self.order = order
        self.keys = []
        self.values = []
        self.children = []

    def insert(self, key, value):
        if not self.children:
            self.keys.append(key)
            self.values.append(value)
            self.keys.sort()
        else:
            child = self._find_child(key)
            child.insert(key, value)

    def search(self, key):
        if not self.children:
            index = self._find_key_index(key)
            if index != -1:
                return self.values[index]
            else:
                return None
        else:
            child = self._find_child(key)
            return child.search(key)

    def _find_child(self, key):
        for i in range(len(self.keys)):
            if key < self.keys[i]:
                return self.children[i]
        return self.children[-1]

    def _find_key_index(self, key):
        for i in range(len(self.keys)):
            if key == self.keys[i]:
                return i
        return -1