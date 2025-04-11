list1=[]
for i in range(11):
    list1.append(i)
extract=list1[0:6]
rev=extract[::-1]
print(f"Original List : {list1}")
print(f" Extract first 5 element : {extract}")
print(f" Reverse : {rev}")