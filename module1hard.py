grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
grades[0] = sum(grades[0])/len(grades[0])
grades[1] = sum(grades[1])/len(grades[1])
grades[2] = sum(grades[2])/len(grades[2])
grades[3] = sum(grades[3])/len(grades[3])
grades[4] = sum(grades[4])/len(grades[4])

print(grades)
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
print(students)
students_list = list(students)
students_list.sort()
print(students_list)
dict = {
students_list[0]:grades[0],
students_list[1]:grades[1],
students_list[2]:grades[2],
students_list[3]:grades[3],
students_list[4]:grades[4]
        }
print(dict)
