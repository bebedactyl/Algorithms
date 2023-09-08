class MyHashtable(object):
    def __init__(self, size):  # Creates an empty hashtable
        self.size = size
        self.table = []
        self.tableStatus = []
        for i in range(self.size):
            self.table.append(None)
            self.tableStatus.append('empty')

    def __str__(self):  # for print
        return str(self.table) + str(self.tableStatus)

    def insert(self, elem):  # Adds an element into the hashtable
        hash = ord(elem[0]) % self.size
        i = hash
        while self.tableStatus[i] == 'filled':
            i = (i + 1) % self.size
            if i == hash:
                raise Exception('Table is full')
        self.table[i] = elem
        self.tableStatus[i] = 'filled'

    def member(self, elem):  # Returns if element exists in hashtable
        hash = ord(elem[0]) % self.size
        i = hash
        while (self.tableStatus[i] == 'filled' and self.table[i] != elem) or self.tableStatus[i] == 'deleted':
            i = (i + 1) % self.size
            if i == hash:
                return False
        if self.tableStatus[i] == 'filled':
            return True
        else:
            return False

    def delete(self, elem):  # Removes an element from the hashtable
        hash = ord(elem[0]) % self.size
        i = hash
        while (self.tableStatus[i] == 'filled' and self.table[i] != elem) or self.tableStatus[i] == 'deleted':
            i = (i + 1) % self.size
            if i == hash:
                return
        if self.tableStatus[i] == 'filled':
            self.table[i] = None
            self.tableStatus[i] = 'deleted'
        else:
            return

# Code Testing
s = MyHashtable(10)
print(s)
s.insert("amy")                     # 97
s.insert("chase")                   # 99
s.insert("chris")                   # 99
print(s)
print(s.member("amy"))
print(s.member("chris"))
print(s.member("alyssa"))
s.delete("chase")
print(s.member("chris"))
print(s)
