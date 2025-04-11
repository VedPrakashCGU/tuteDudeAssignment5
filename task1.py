n=int(input("Enter the how much student : "))
student={}
for i in range(n):
    name=input("Enter the name of student : ")
    marks=float(input("Enter the marks : "))
    student[name]=marks
    
print(student)

name=input("Enter the name of student which want to search : ")

if name in student:
    print(student[name])
else:
    print(f"{name} is not in class")