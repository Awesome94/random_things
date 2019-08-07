# def while_arr(arr, target):
#     arr.sort()
#     N = len(arr)
#     for x in range(N):
#         i = N-1
#         k = N-2
#         m = N-3
#         while i<N and i>0 and k>0 and m>0 and x<N:
#             if arr[x] + arr[i] + arr[k] +arr[m] == target:
#                 print(arr[x], arr[i], arr[k], arr[m])
#             # i-=1
#                 k-1
#                 m-1
#             # elif arr[x] + arr[i] + arr[k] +arr[m] < target:
#             #     # i-=1
#             #     k-1
#             #     m-1
#             # else:
#             #     x+=1
#             #     i-=1
# while_arr([-3,-2, -1,0,0,1,2,3], 0)
        
      
def fourSum(nums, target):
    result = []
    nums.sort()
    length = len(nums)-1
    for i in range(length-2):
        if i > 0 and nums[i] == nums[i-1]:          # if 1st index is duplicate, continue
            continue
        for j in range(i+1, length-1):
            if j > i+1 and nums[j] == nums[j-1]:    # if 2nd index is duplicate, continue
                continue
            k = j+1
            h = length
            while k < h:                            # while 3rd index is smaller than the 4th index
                curr = nums[i] + nums[j] + nums[k] + nums[h]
                if curr == target:
                    result.append([nums[i], nums[j], nums[k], nums[h]])
                    while k < h and nums[k] == nums[k+1]:
                        k += 1
                    while k < h and nums[h] == nums[h-1]:
                        h -= 1
                    k += 1
                    h -= 1
                elif curr > target:
                    h -= 1
                else:
                    k += 1
    print(result)
    return result
fourSum([-3,-2, -1,0,0,1,2,3], 0)