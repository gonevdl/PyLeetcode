# for i in range(1, 21):
#     print(i)

# nums = [i for i in range(1, 1000001)]
# # for num in nums:
# #     print(num)
# print(sum(nums))
# nums1 = [1, 2, 3, 4, 5, 6, 7, 8]
# nums2 = [10000]
# print(nums2)
# nums2 = nums1[:]
# print(nums2)
# nums3 = [1, 2, 3]
# # nums2 = nums3[:]
# nums2[:] = nums3
# print(nums1)
# print(nums2)
# oth = [1, 2, 3, 4, "hello", 0]
# print(oth)
# oth[2] += 1000
# print(oth)
# student = {1: "name", 2: "age", 3: [12, 3, 4, 5, 6, 7], 0: 5}
# print(student)

class People(object):
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name


me = People("小明", "18")
me.name = "小李"
print(me.name)