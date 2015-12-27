def heapify(array):
    """ Change the current array into heapify
    Start with middle elemnt and check whether it satisfies heap property
    Continue doing it till the roor (first element of the array) """
    end=len(array)-1
    start=int(end/2) - 1
    for i in range(start, -1, -1):
        shift_down(array, i, end)


def shift_down(array, start, end):
    """ Start is the parent under consideration, check whether it is larger than childrens, if not swap them.
    Propogate this effect till the end of the array """

    root = start
    child_left = 2 * root + 1 #Indexing starts from zero

    while(child_left < end):
        child_right = child_left + 1

        swap = root
        if(array[root] < array[child_left]):
            swap = child_left
        if(array[root] < array[child_right] and array[swap] < array[child_right]): # We want to swap with child with larger value
            swap = child_right
        if(root != swap):
            array[root], array[swap] = array[swap], array[root]
            root = swap
            child_left = 2 * root + 1 #Indexing starts from zero
        else:
            return;




array = [32,46,77,4344564,7322,3,46,7,32457,7542,4,667,54]

#Turn the array into heap
heapify(array)

# Keep removing the root, and place it to end of the array
end=len(array) -1
while end >= 2:
    array[0], array[end] = array[end], array[0]
    end = end - 1
    shift_down(array, 0, end)

print ("Here is the sorted array")
print (array)
