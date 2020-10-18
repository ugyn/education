class ExtendedStack(list):
    def sum(self):
        top1, top2 = self.pop(), self.pop()
        self.append(top1 + top2)

    def sub(self):
        top1, top2 = self.pop(), self.pop()
        self.append(top1 - top2)

    def mul(self):
        top1, top2 = self.pop(), self.pop()
        self.append(top1 * top2)

    def div(self):
        top1, top2 = self.pop(), self.pop()
        self.append(top1 // top2)