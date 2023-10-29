# def findMedianSortedArrays(nums1, nums2):
#     nums3 = sorted(nums1 + nums2)
#     length = len(nums3)
#     sum = 0
#     for i in nums3:
#         sum += i
#
#     median = sum / length
#     return median
#
#
# print(findMedianSortedArrays(nums1=[1, 2], nums2=[3, 4]))
#
# # Python3 code to demonstrate working of
# # Median of list
# # Using loop + "~" operator
#
# # initializing list
# test_list = [4, 5, 8, 9, 10, 17]
#
# # printing list
# print("The original list : " + str(test_list))
#
# # Median of list
# # Using loop + "~" operator
# test_list.sort()
# mid = len(test_list) // 2
# res = (test_list[mid] + test_list[~mid]) / 2
#
# # Printing result
# print("Median of list is : " + str(res))
#
#
# # num=2
# # sum =0
# # for i in str(num):
# #     if i != num:
# #         # print(i)
# #         sum+=int(i)
# #         print(sum)
# #     else:
# #         print(i)
# # add digits of number
# class Solution(object):
#     def addDigits(self, num):
#         """
#         :type num: int
#         :rtype: int
#         """
#         while num >= 10:
#             # Split the number into its digits and add them
#             digit_sum = 0
#             while num > 0:
#                 digit_sum += num % 10
#                 num //= 10
#             num = digit_sum
#         return num
#
#
# my_instance = Solution()
# result = my_instance.addDigits(23)  # Note the correct method name and argument
# print(result)
#
# # two input lists
# list1 = [11, 21, 34, 12, 31, 26]
# list2 = [23, 25, 54, 24, 20]
#
# # empty resultant list
# result = []
#
# # choose the smaller list to iterate
# small_list = len(list1) < len(list2) and list1 or list2
#
# for i in range(0, len(small_list)):
#     result.append(list1[i] + list2[i])
#
# print("Resultant list : " + str(result))
#
#
# class Solution(object):
#     def addTwoNumbers(self, l1, l2):
#         """
#         :type l1: ListNode
#         :type l2: ListNode
#         :rtype: ListNode
#         """
#         result = []
#         small_list = len(l1) > len(l2) and l1 or l2
#         for i in range(0, len(small_list)):
#             result.append(l1[i] + l2[i])
#         return result
#
#
# my_instance = Solution()
# Result = my_instance.addTwoNumbers(l1=[1, 2, 3], l2=[4, 5, 6])
# print(Result)
#
#
# class Solution(object):
#     def intToRoman(self, num):
#         """
#         :type num: int
#         :rtype: str
#         """
#         val = [
#             1000, 900, 500, 400,
#             100, 90, 50, 40,
#             10, 9, 5, 4,
#             1
#         ]
#         syms = [
#             "M", "CM", "D", "CD",
#             "C", "XC", "L", "XL",
#             "X", "IX", "V", "IV",
#             "I"
#         ]
#
#         roman_num = ''
#         i = 0
#         while num > 0:
#             for _ in range(num // val[i]):
#                 roman_num += syms[i]
#                 num -= val[i]
#             i += 1
#
#         return roman_num
#
#
# my_instance = Solution()
# print(my_instance.intToRoman(123))
#
# #
# # def move_even_odd(nums):
# #     even_nums = []
# #     odd_nums = []
# #
# #     for num in nums:
# #         if num % 2 == 0:
# #             even_nums.append(num)
# #         else:
# #             odd_nums.append(num)
# #
# #
# #     result = even_nums + odd_nums
# #
# #     return result
# #
# #
# # nums = [3, 1, 2, 4, 6, 5, 7, 8]
# # result = move_even_odd(nums)
# # print(result)
# #
# #
# # class Solution(object):
# #     def sortArrayByParity(self, nums):
# #         """
# #         :type nums: List[int]
# #         :rtype: List[int]
# #         """
# #         even_nums = []
# #         odd_nums = []
# #
# #         for num in nums:
# #             if num % 2 == 0:
# #                 even_nums.append(num)
# #             else:
# #                 odd_nums.append(num)
# #
# #         result = even_nums + odd_nums
# #
# #         return result
# #
# #
# # nums = [3, 1, 2, 4, 6, 5, 7, 8]
# # my_instance = Solution()
# # result = my_instance.sortArrayByParity(nums)
# # print(result)


# Sample dictionary of dictionaries
data = {
    'person1': {'name': 'Alice', 'age': 30},
    'person2': {'name': 'Bob', 'age': 25},
    'person3': {'name': 'Charlie', 'age': 35}
}

# Outer loop to iterate through the top-level keys (e.g., 'person1', 'person2', 'person3')
for person_key, person_value in data.items():
    print(f"Person: {person_key}")

    # Inner loop to iterate through the nested dictionary's keys and values
    for key, value in person_value.items():
        print(f"{key}: {value}")

    # Add an empty line for separation between individuals
    print()

people = {1: {'Name': 'John', 'Age': '27', 'Sex': 'Male'},
          2: {'Name': 'Marie', 'Age': '22', 'Sex': 'Female'}}

if 1 in people:
    # person1 = people[1]

    for key, value in people[1].items():
        print(f"{key},{value}")

else:
    print("not found")
