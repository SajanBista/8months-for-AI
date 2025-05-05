class Data:
    def __init__(self):
        self.items = []

    def ad(self, x):
        self.items.append(x)

    def rm(self, x):
        self.items.remove(x)

    def gt(self):
        return self.items

    def pr(self):
        for i in self.items:
            print(i)

    def cl(self):
        self.items = []


d = Data()
d.ad("item1")
d.ad("item2")
d.ad("item3")
d.pr()

#d.rm("item2")
print("after removing:")
d.pr()
d.cl()
print("after clearing:")
d.pr()
