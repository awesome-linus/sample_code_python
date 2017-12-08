class MyIterator(object):
    def __init__(self, step):
        self.step = step

    def next(self):
        """Returns the next element."""
        if self.step == 0:
            raise StopIteration
        self.step -= 1
        return self.step

    __next__ = next  # for python3

    def __iter__(self):
        """Returns the iterator itself."""
        return self


for el in MyIterator(5):
    print(el)
