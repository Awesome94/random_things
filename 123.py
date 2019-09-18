def is123Array(arr):
    if len(arr)%3:
        return 0
    y = 0

    for x in range(len(arr)-3):
        if x+3 <= len(arr)-1:
            y = x+3
            print("this is Y", y, x)
        print(arr[x], arr[y])
        if arr[x] != arr[y]:
            print(x , y)
            return 0
        else:
            x+=1
    return 1


print(is123Array([2, 2, 3]))


