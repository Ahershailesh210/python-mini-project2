students = []
number_of_students = int(input("Enter the number of students: "))
for i in range(number_of_students):
    student = {
        "roll_no": int(input("Enter roll number: ")),
        "name": input("Enter name: "),
        "department": input("Enter department: "),
        "marks": {
            "maths": int(input("Enter marks in Maths: ")), 
            "physics": int(input("Enter marks in Physics: ")),
            "chemistry": int(input("Enter marks in Chemistry: ")),
            "python": int(input("Enter marks in Python: ")),
            "IDS": int(input("Enter marks in IDS: "))
        }
    }
    students.append(student)
print("\nAll Students:")

for student in students:
    print("Roll No:", student["roll_no"])
    print("Name:", student["name"])
    print("Department:", student["department"])
    print("Marks:", student["marks"])
    print()
search_roll_no = int(input("Enter roll number to search: "))
found = False
for student in students:
    if student["roll_no"] == search_roll_no:
        print("Student found:")
        print("Roll No:", student["roll_no"])
        print("Name:", student["name"])
        print("Department:", student["department"])
        print("Marks:", student["marks"])
        found = True
        break
if not found:
    print("Student not found.")
update_roll_no = int(input("Enter roll number to update marks: "))
found = False
for student in students:
    if student["roll_no"] == update_roll_no:
        new_name = input("Enter new name: ")
        student["name"] = new_name
        print("Current Marks:", student["marks"])
        student["marks"]["maths"] = int(input("Enter new marks in Maths: "))
        student["marks"]["physics"] = int(input("Enter new marks in Physics: "))
        student["marks"]["chemistry"] = int(input("Enter new marks in Chemistry: "))
        student["marks"]["python"] = int(input("Enter new marks in Python: "))
        student["marks"]["IDS"] = int(input("Enter new marks in IDS: "))
        print("Marks updated successfully.")
        break
if not found:
    print("Student not found.")
delete_roll_no = int(input("Enter roll number to delete: "))
found = False
for student in students:
    
    if student["roll_no"] == delete_roll_no:
        students.remove(student)
        print("Student deleted successfully.")
        found = True
        break
if not found:
    print("Student not found.") 
avg_marks = {}
for student in students:
    total_marks = sum(student["marks"].values())
    avg_marks[student["roll_no"]] = total_marks / len(student["marks"])
highest_avg_roll_no = max(avg_marks, key=avg_marks.get)
print("Student with highest average marks:")
for student in students:
    if student["roll_no"] == highest_avg_roll_no:
        print("Roll No:", student["roll_no"])
        print("Name:", student["name"])
        print("Department:", student["department"])
        print("Average Marks:", avg_marks[highest_avg_roll_no])
        break   
# department wise student finding
department_name = input("Enter department name to find students: ")
department_students = [student for student in students if student["department"].lower() == department_name.lower()]
if department_students:
    print(f"Students in {department_name} department:")
    for student in department_students:
        print("Roll No:", student["roll_no"])
        print("Name:", student["name"])
        print("Marks:", student["marks"])
        print()
else:
    print(f"No students found in {department_name} department.")    
count_students = len(students)
print("Total number of students:", count_students)