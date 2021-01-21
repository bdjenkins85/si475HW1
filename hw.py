import math

def sortFunc():

    x = input("Num 1:" )
    y = input("Num 2: ")
    z = input("Num 3: ")

    nums = [int(math.ceil(x)), int(math.ceil(y)), int(math.ceil(z))]

    for i in range(len(nums)):
        minindex = i
        for j in range(i+1, len(nums)):
            if (nums[minindex] > nums[j]):
                    minindex = j
        nums[i], nums[minindex] = nums[minindex], nums[i]

    print("The cielings of those numbers are: "+str(nums))

if __name__=="__main__":
    sortFunc()
