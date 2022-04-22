class Link:
    def __init__(self, left, right):
        self.l = []
        self.r = []

        self.l.append(left)
        self.r.append(right)

    def __getitem__(self, name):
        for i in range(len(self.l)):
            if self.l[i] == name:
                return self.r[i]

        for i in range(len(self.r)):
            if self.r[i] == name:
                return self.l[i]

        return None

    def __setitem__(self, name, value):
        for i in range(len(self.l)):
            if self.l[i] == name:
                self.r[i] = value
                return
        
        for i in range(len(self.r)):
            if self.r[i] == name:
                self.r[i] = value
                return

        print("Appending to list")
        self.l.append(name)
        self.r.append(value)
        
    def recurse(self, what=None):
        to_return = ""
        for i in range(len(what.l)):
            left = what.l[i]
            right = what.r[i]
            if isinstance(left, Link):
                self.recurse(what=left)
            if isinstance(right, Link):
                self.recurse(what=right) 

            to_return += f"{left} <-> {right}, "

        return to_return

    def __str__(self):
        ret = self.recurse(what=self)
        return ret
