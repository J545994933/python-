# todo 179 最大数
"""
给定一个List,让其组合成一个最大数
"""
# 排序
nums = [3,30,34,5,9]
# for x in range(len(nums)-1):
#     for y in range(x + 1, len(nums)):
#         if int(str(nums[x]) + str(nums[y])) < int(str(nums[y]) + str(nums[x])):
#             nums[y], nums[x] = nums[x], nums[y]
# print(sum(nums))
# str_nums = [str(i) for i in nums]
# print(nums)
# print(''.join(str_nums))
# sort
str_nums = [str(i) for i in nums]
len_str = len(str(max(nums))) * 2
max_nums = [(i*len_str)[:len_str] for i in str_nums]
max_nums.sort(reverse=True)
print(max_nums)
for num in str_nums:
    max_nums[max_nums.index((num*len_str)[:len_str])] = num
print(max_nums)
# print(max_nums)