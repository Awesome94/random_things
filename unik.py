def findequil(arr):
    mid = len(arr)//2
    sum_arr = []

    while mid < len(arr):
        if sum(arr[:mid]) == sum(arr[mid+1:]):
            return mid
        elif sum(arr[:mid]) > sum(arr[mid+1:]):
            if arr[:mid] not in sum_arr or arr[mid+1:] not in sum_arr:
                sum_arr.append(arr[:mid])
                sum_arr.append(arr[mid+1:])
                mid-=1
            else:
                return -1
   
        elif sum(arr[:mid]) < sum(arr[mid+1:]):
            if arr[:mid] not in sum_arr or arr[mid+1:] not in sum_arr:
                sum_arr.append(arr[:mid])
                sum_arr.append(arr[mid+1:])
                mid+=1
            else:
                return -1

print(findequil([2, 1, 1, 1, 2, 1, 7]))
