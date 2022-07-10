
def binarySearchFunc (list, number):
    length = len(list)
    middle = int(length / 2)
    #if(list[middle] > )
    if (len(list) == 1):
        if list[0] == number:
            return "number found"
        else:
            return "number not found"
    else:
        if list[middle] > number :
            newlist = list[0:middle]
        elif list[middle] <= number:
            newlist = list[middle:length]     
             
    return binarySearchFunc(newlist, number)    

list = [11,22,24,31,35,43,46,49,50,90]
#sorted list =  [11,22,24,31,35,43,46,49,50,90,100]
list.sort()
print(list)
message = binarySearchFunc(list, 43)
print(message)

