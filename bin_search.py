def bin_search(nums, target):
    l = -1
    r = len(nums)
    while(l<=r):
        m = (r+l)//2
        if nums[m] == target:
            return m
        elif(target > nums[m]):
            l = m+1
        else:
            r = m-1    
    return -1

#nums = [5]
#target = -5
#print(bin_search(nums, target))
    
