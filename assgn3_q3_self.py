# a = int(input("enter a number"))
# b = int(input("enter a number"))
# c = int(input("enter a number"))

# list_1 = [a, b, c]
# print(list_1)

# list_2 = [(a,a**2), (b,b**2), (c,c**2)]
# print(list_2)


# n = int(input("enter a number: "))
# list1 = []
# list2 = []
# for i in range(1,n+1):
#     a = int(input("enter a number: "))
#     list1.append(a)
#     list1.append(a**2)
#     tuple_list1 = tuple(list1)
#     list2.append(tuple_list1)
#     list1.clear()

# print(list2)    


n= int(input("enter a number "))
my_list = []


for i in range(1,n+1):
    a = int(input("enter a number"))
    my_list.append(a)

result = [(val,val**2) for val in my_list]
print(result)


     






    




