# Calc media of students with list
student = []
students = []
  
while True:
    name = str(input("Student name: ")).strip()
    note1 = float(input("Note 1º: "))
    note2 = float(input("Note 2º: ")) 

    student.append(name)
    student.append(note1)
    student.append(note2)
    students.append(student[:])
    student.clear()

    keep = str(input("Continue? [Y/N] ")).strip().upper()

    if keep == "N":
        break
print("=-"*12)
print(f"{'N':<3} {'Name':10} {'Media':>10}")    
for key, student in enumerate(students):
    print(f"{(key):<3} {student[0]:10} {((student[1] + student[2]) / 2):>10}")

while True:
    n_student = int(input("Shows note which student's grade? [999 for quit] "))

    if n_student == 999:
        break

    print(f"Student: {students[n_student][0]}")
    print(f"Grade: {students[n_student][1]} - {students[n_student][2]}")
    
print("End program..")
    
        





