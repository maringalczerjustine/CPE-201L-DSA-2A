class ArrayList:
    def __init__(self):
        self.arr = []

    # Append
    def append(self, data):
        self.arr.append(data)

    # Traverse
    def traverse(self):
        for ch in self.arr:
            print(ch)

name = "Czer Justine Maringal"

array_list = ArrayList()

for ch in name:
    array_list.append(ch)

print("Characters in the array list:")
array_list.traverse()
