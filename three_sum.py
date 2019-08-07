def three_sum(nums):
    nums.sort()
    N = len(nums)
    result = []
    for x in range(N):
        if nums[x] == nums[x-1]:
            continue
        s = x+1
        e = N-1
        target = nums[x]*-1
        
        while s<e:
            sum_  = nums[s] + nums[e]
            if sum_ == target:
                result.append([nums[s], nums[e], nums[x]])
                s+=1
                while s<e and nums[s] == nums[s-1]:
                    s+=1
            elif sum_ < target:
                s+=1
            else:
                e-=1
    print(result)
    return result

three_sum([-2,-1,0,1,2,3])

