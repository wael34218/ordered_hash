import math


class Entry:
    def __init__(self, key, value):
        self.value = value
        self.key = key
        self.next_entry = None


class OrderedHash:
    def __init__(self, data=[]):
        self.a = 11
        self.w = 16
        self.r = int(math.ceil(math.log(2 * len(data) + 1, 2)))
        self.keys = []
        self.length = 0
        self.store = [None] * 2**self.r
        for k, v in data:
            self.insert(k, v)

    def insert(self, k, v):
        hkey = self.__hash(k)
        entry = self.store[hkey]
        parent = None
        if entry is None:
            self.store[hkey] = Entry(k, v)
        while entry is not None:
            if entry.key == k:
                entry.value = v
                return
            parent = entry
            entry = entry.next_entry
        if parent is not None:
            parent.next_entry = Entry(k, v)
        self.keys.append(k)
        self.length += 1

        if self.length > (2**self.r):
            self.__resize(self.r + 1)

    def delete(self, k):
        hkey = self.__hash(k)
        entry = self.store[hkey]
        parent = None
        found = False

        while entry is not None:
            if entry.key == k:
                found = True
                if parent is None:
                    self.store[hkey] = entry.next_entry
                else:
                    parent.next_entry = entry.next_entry
                del entry
                break
            parent = entry
            entry = entry.next_entry

        if found:
            self.keys.remove(k)
            self.length -= 1
        else:
            raise KeyError('key '+str(k)+' is not found in OrderedHash')

        if self.length < (2**self.r) / 4:
            self.__resize(self.r - 1)

    def get(self, k):
        obj = self.__get(k)
        if obj is None:
            raise KeyError('key '+str(k)+' is not found in OrderedHash')
        else:
            return obj.value

    def __resize(self, new_r):
        print("resizing into "+str(new_r))
        if new_r < 1:
            return
        dstore = [None] * 2**(new_r)
        for k in self.keys:
            v = self.get(k)
            hkey = self.__hash(k, new_r)
            entry = dstore[hkey]
            parent = None
            if entry is None:
                dstore[hkey] = Entry(k, v)
            while entry is not None:
                if entry.key == k:
                    entry.value = v
                    return
                parent = entry
                entry = entry.next_entry
            if parent is not None:
                parent.next_entry = Entry(k, v)

        self.r = new_r
        self.store = dstore

    def __get(self, k):
        hkey = self.__hash(k)
        if self.store[hkey] is None:
            return None
        else:
            entry = self.store[hkey]
            while entry is not None:
                if entry.key == k:
                    return entry
                entry = entry.next_entry
            return None

    def __hash(self, key, r=None):
        if r is None:
            r = self.r
        value = sum([ord(x)*(2**i) for i, x in enumerate(str(key))])
        key = ((value * self.a) % 2**self.w) >> (self.w - r)
        return key

    def __str__(self):
        output = []
        for k in self.keys:
            output.append(str(k) + ":" + str(self.get(k)))
        return "{" + ", ".join(output) + "}"

    def __iter__(self):
        for key in self.keys:
            yield (key, self.get(key))
        return

    def __len__(self):
        return self.length

    def __getitem__(self, k):
        return self.get(k)

    def __setitem__(self, k, v):
        return self.insert(k, v)
