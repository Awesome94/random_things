def fourSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    nums.sort()
    N = len(nums)-1
    result = []

    for i in range(N-2):
        if i > 0 and nums[i] == nums[i-1]:
            continue

        for x in range(i+1, N-1):
            if x > i+1 and nums[x] == nums[x-1]:
                continue
            j = x+1
            e = N

            while j < e:
                if nums[x]+nums[j]+nums[i]+nums[e] == target:
                    result.append([nums[x], nums[j], nums[i], nums[e]])
                    j+=1
                    e-=1
                    while j < e and nums[j]==nums[j-1]:
                        j+=1
                    while j < e and nums[e] == nums[e+1]:
                        e-=1
                elif nums[x]+nums[j]+nums[i]+nums[e] > target:
                    e-=1
                else:
                    j+=1
    print(result)
    return result


fourSum([1,0,-1,0,-2,2], 0)

-2, -1, 0, 0, 1, 2

"""

-3

[-3,-2, -1,0,0,1,2,3]
[-3,-1,0,2,4,5],
0
[-4, -1, -1, 0, 1, 2]

[1,0,-1,0,-2,2]
0
[-2,-1, 0, 0, 1, 2]
-2, -1, 0, 2

[[-3,-2,2,3],[-3,-1,1,3],[-3,0,0,3],[-3,0,1,2],[-2,-1,0,3],[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

[[-3,-2,3,2],[-3,-1,3,1],[-3,0,3,0],[-3,1,2,0],[-2,-1,3,0],[-2,0,2,0],[-1,0,1,0]]

-2,-1,1,2
"""

"""
sort the array.

"""