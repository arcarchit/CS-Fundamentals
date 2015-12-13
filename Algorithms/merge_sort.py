"""
Is merge sort In Place? I guess yes

"""

def sort(array, start, end):
    if(start == end):
        return
    mid=int((start+end)/2)
    sort(array, start, mid)
    sort(array, mid+1, end)
    merge(array, start, mid + 1, end)

def merge(array, start, mid, end):
    helper=[None] * len(array)
    helper[start:end +1] = array[start:end+1]
    arrayIndex=start
    fixedMid=mid # This indicate index of first element of second array

    while(start < fixedMid and mid <= end):
        if(helper[start] <= helper[mid]):
            array[arrayIndex] = helper[start]
            arrayIndex = arrayIndex + 1
            start = start + 1
        else:
            array[arrayIndex] = helper[mid]
            arrayIndex = arrayIndex + 1
            mid = mid + 1
    while(start < fixedMid):
            array[arrayIndex] = helper[start]
            arrayIndex = arrayIndex + 1
            start = start + 1
    while(mid <= end):
            array[arrayIndex] = helper[mid]
            arrayIndex = arrayIndex + 1
            mid = mid + 1


array = [32,46,77,4344564,7322,3,46,7,32457,7542,4,667,54]
print "Array Befor Sorting"
print array
print "\n\n"
sort(array, 0, len(array)-1) #first index 0, last index len -1
print "Array After Sorting"
print array
print "\n\n"
