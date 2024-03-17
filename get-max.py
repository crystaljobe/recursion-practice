def get_max_recursive(nums):
  if len(nums) == 1:
    return nums[0]
  else:
    if nums[0] > nums[1]:
       nums.pop(1)
       return get_max_recursive(nums)
    else:
       return get_max_recursive(nums[1:])