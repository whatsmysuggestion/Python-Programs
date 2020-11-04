name=input("enter your name")
age=int(input("enter your age"))
fee=float(input("enter your fee"))
student={'name':name,'age':age,'fee':fee}

print(student.keys())
print(student.values())
print(student.get('age'))
