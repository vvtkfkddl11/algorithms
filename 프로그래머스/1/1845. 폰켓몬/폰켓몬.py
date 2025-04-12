def solution(nums):
    choice = len(nums)//2
    nums = list(set(nums))
    if len(nums) >= choice:
        return choice
    return len(nums)