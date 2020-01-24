""" 
Given an int array nums and an int target, find how many unique pairs in the array such that their sum is equal to target. Return the number of pairs.
Input: nums = [1, 1, 2, 45, 46, 46], target = 47
Output: 2
Explanation:
1 + 46 = 47
2 + 45 = 47 
"""

numbers = [1, 1, 2, 45, 46, 46]

def two_sum(nums, target):
    seen = set()
    answers = set()
    # The idea for this loop is to find out if the difference of the target and the number is in our seen collection
    # If it is, then we know that the compare and the num sum to the target.
    # We hold this in the answers set so we don't have duplicates.
    for num in nums:
        compare = target-num
        if compare in seen:
            pair = (compare, num)
            print(pair)
            answers.add(pair)
        else:
            seen.add(num)
    return len(answers)

print(two_sum(numbers,47))