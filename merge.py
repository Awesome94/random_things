def merge(arr1, arr2):
    '''
    merge two arrays into 1
    '''
    c = []
    i = j  = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            c.append(arr1[i])
            i+=1
        else:
            c.append(arr2[j])
            j+=1
    while i < len(arr1):
        c.append(arr1[i])
        i+=1
    while j < len(arr2):
        c.append(arr2[j])
        j+=1
    print(c)
    return c
merge([1,3,5,6], [2,4,5,6,7,8])

    