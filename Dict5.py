student={'name':['test','dd'],'age':22,'fee':17.6}
print(student)

print(student.get('name')[0],student.get('name')[1])
print(student['name'][0],student['name'][1])


student['name']='testing'
print(student)
student['address']='Bangalore'
print(student)