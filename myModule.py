class MyClass:
    def __init__(self, list):
        self.list = list
        
    def odds(self):
        newList = []
        for i in range(len(self.list)):
            if i%2 == 1:
                newList.append(self.list[i])
        return newList

    def oddsPlusC(self, c):
        list = MyClass.odds(self)
        for i in range(len(list)):
            list[i] = int(list[i]) + int(c)
        return list
        
