import math

def sortFunc(x, y, z):
    num1 = int(math.ceil(x))
    num2 = int(math.ceil(y))
    num3 = int(math.ceil(z))
    list = [num1, num2, num3]
    for i in range(len(list)):
        min = list[i]
        mindex = i
        for k in range(len(list) -i):
            if(list[i+k] < min):
                min = list[i+k]
                mindex = i+k
        list[mindex] = list[i] 
        list[i] = min        
    return list

        
def main():
    x = input("Num 1: ")
    y = input("Num 2: ")
    z = input("Num 3: ")
    print "The ceilings of those numbers sorted are: ", sortFunc(x,y,z)

if __name__== "__main__":
    main()
