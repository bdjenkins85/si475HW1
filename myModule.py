class MyClass:
    def __init__(self, list):

        self.modList = list

    def odds(self):
        
        oddNums = []
        for i in range(len(self.modList)):
            if i%2 == 1:
                oddNums.append(self.modList[i])

        print(oddNums)


    def oddsPlusC(self, c):
        oddNums = []
        for i in range(len(self.modList)):
            if i%2 == 1:
                oddNums.append(self.modList[i]+c)


        print(oddNums)

if __name__=="__main__":
    myC = MyClass([1,2,3,4])
    myC.odds()
    myC.oddsPlusC(3)
    myC.odds()
