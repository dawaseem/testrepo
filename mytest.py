# fname = input("First Name: ")
# lname = input("Last Name: ")

# print(fname[::-1])


# lisst = fname.split(",")
# tuuple = tuple(lisst)

# print("List: ", lisst, "Tuple: ", tuuple)
# myf = fname.split(".")
# print(myf[1])


# color_list = ["Red", "Green", "White", "Black"]

# listlen = len(color_list)
# print(color_list[0], color_list[listlen-1])

# exam_st_date = (11, 12, 2014)
# print("The examination will start from : %i / %i / %i" % exam_st_date)

# val = 3

# print(val+val*val+val*val*val)

# a = int(input("Input an integer : "))
# n1 = int("%s" % a)
# n2 = int("%s%s" % (a, a))
# n3 = int("%s%s%s" % (a, a, a))
# print(n1 + n2 + n3)

# import calendar
# y = int(input("Input the year : "))
# m = int(input("Input the month : "))
# print(calendar.month(y, m))


# from datetime import date
# fdata = date(1998, 4, 2)
# ldate = date(2023, 1, 23)
#
# d = ldate-fdata
# print(d/30)

# def difference(n):
#     if n <= 17:
#         return 17 - n
#     else:
#         x = (17 - n) * 2
#         return abs(x)
#
#
# print(difference(25))
# print(difference(5))


# def new_s(text):
#     if len(text) >= 2 and text[:2] == "Is":
#         return text
#     return "Is " + text
#
#
# print(new_s("Array"))
# print(new_s("Empty"))


# def list_counter(nums):
#     count = 0
#     for num in range(len(nums)):
#         if nums[num] == 4:
#             count = count + 1
#     return count
#
#
# print(list_counter([1, 4, 6, 7, 4]))


# def substring_copy(text, n):
#     flen = 2
#     if flen > len(text):
#         flen = len(text)
#     substr = text[:flen]
#     print(substr)
#     result = ""
#     for i in range(n):
#         result = result + substr
#     return result
#
#
# print(substring_copy('abcdef', 2))
# print(substring_copy('p', 3))

#
# def multer(text):
#     if len(text) >= 2:
#         return text[:2] * 2
#     else:
#         return text
#

# print(multer('waseem'))


# def num_checker(mylist):
#     if 3 in mylist:
#         print("Yes in list")
#     else:
#         print("Not present")
#
#
# print(num_checker([2, 5, 7, 4, 5, 3, 1, 3]))


# def myfunc(a, b, c):
#     return a + b + c
#
#
# print(myfunc(2, 4, 10, 4))


# def argfunc(*data):
#     sum = None
#
#     for i in data:
#         sum += i
#     print(sum)
#
#
# print(argfunc())


# a = [1, 2, "Ram", 3.50, "Rahul", 6]
# b = [1, 2, "Ram", 3.50, "Rahul", 6]
#
# print(a == b)

# omlist = [1, 2, 3, 4, 5, 6, 7]
# mlist = [1, 2, 3, 4, 5, 6, 7]
# mlist[-1:] = [89, 78]
# print("Old Lis: ", omlist)
# print("New List: ", mlist)

# print(mlist*3)

# listlenth = int(input("Enter list length: "))
# mylist =[]
# for i in range(listlenth):
#     mylist.append(input('Enter digit: '))
#
#
# print(sorted(mylist))

# mylistomlist = [1, 2, 3, 4, 5, 6, 7]
#
# omlist.remove(3)
# print(omlist)

# import json
#
# data = { "name": "John", "age": 30, "city": "New York" }
# print(type(data))
#
# json_data = json.dumps(data)
# print(data)
# print(type(json_data))