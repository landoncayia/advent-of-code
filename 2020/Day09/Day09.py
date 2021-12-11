def part1(nums, low, high):
    current_val = 0
    while current_val == 0:
        current_val = check_sums(nums, low, high)
        low += 1
        high += 1
    return current_val


def part2(nums, invalid):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            iter_values = [k for k in nums[i:j+1]]
            iter_sum = sum(iter_values)
            if iter_sum == invalid:
                return min(iter_values) + max(iter_values)


def check_sums(nums, low, high):
    for i in nums[low:high]:
        for j in [k for k in nums[low:high] if k != i]:
            if i + j == nums[high]:
                return 0
    return nums[high]


with open('input.txt') as f:
    data = f.readlines()


number_list = [int(num) for num in data]
low_idx = 0
high_idx = 25
invalid_num = part1(number_list, low_idx, high_idx)
print(invalid_num)
encrypt_break = part2(number_list, invalid_num)
print(encrypt_break)
