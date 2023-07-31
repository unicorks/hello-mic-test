def rotate(nums, n):
    return (nums[-(n):]) + nums[:(len(nums) - n)] if n < len(nums) else (nums[-(n%len(nums)):]) + nums[:(len(nums) - n%len(nums))]
    
print(rotate([1,2,3,4,5,6,7], 11))
