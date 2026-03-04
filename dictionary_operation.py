student_1 = {'maths' : 80.5, 'english' : 76.0, 'physics' : 89.0}
print(student_1)
# fetch the marks of physics
print(student_1['physics'])

# get function which does similar task
print(student_1.get('physics'))
#print(student_1['chem']) will give a error as this key is not present in the dictionary
#print(student_1.get('chem')) will not give an error but will show value as None
print(student_1.get('chem'))

emp1 = {'id' : 1001, 'name' : 'john', 'salary' : 10000}
print(emp1.get('phone',"number not provide"))

#membership > in looks for a key and not value

print(1001 in emp1)
# false

print('name' in emp1)
# True
emp1['city'] = 'New York'
print(emp1)

#update function

sem1_marks = {'maths' : 71.5, 'english' : 84, 'physics' : 87.5}
sem2_marks = {'chem' : 93, 'Biology' : 75}

sem1_marks.update(sem2_marks)
print(sem1_marks)

#update function
groceries_1 = {'milk' : 60, 'bread' : 30, 'eggs' : 80 }
groceries_2 = {'butter' : 45, 'bread' : 40,}
groceries_1.update(groceries_2)
print(groceries_1)

#pop function
groceries_1.pop('milk')
print(groceries_1)
