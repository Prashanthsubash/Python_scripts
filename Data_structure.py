alist= [100, 200, 300, 400, 500]
alist.reverse()
print(alist)

list1 = ["M", "na", "i", "Ke"] 
list2 = ["y", "me", "s", "lly"]

result= [i + j for i,j in zip(list1,list2)]
print(result)

list_2 = [1, 2, 3, 4, 5, 6, 7]
squared_list=[x**2 for x in (list_2)]
print(squared_list)

list3 = ["Hello ", "take "]
list4 = ["Dear", "Sir"]
result_3 = [l+k for l in list3 for k in list4 ]
print(result_3)

list5 = [10, 20, 30, 40]
list6 = [100, 200, 300, 400]
for a,s in zip(list5,list6 [::-1]):
    print(a,s)

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
Dic = dict(zip(keys,values))
print(Dic)

dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
com_dic = dict1.copy()
com_dic.update(dict2)
print(com_dic)

sampleSet = {"Yellow", "Orange", "Black"}
sampleList = ["Blue", "Green", "Red"]
sampleSet.update(sampleList)
print(sampleSet)


set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
identical = set1 & set2
print(identical)

set4 = {10, 20, 30, 40, 50}
set5 = {30, 40, 50, 60, 70}
combine= set4 | set5
print (combine)

aTuple = (10, 20, 30, 40, 50)
reverse_tuple = aTuple[::-1]
print(reverse_tuple)

New_Tuple = ("Orange", [10, 20, 30], (5, 15, 25))
orange = New_Tuple [1][1]
print(orange)

tuple1 = (11, 22)
tuple2 = (99, 88)

tuple1, tuple2 = tuple2 , tuple1

print(tuple1)
print(tuple2)