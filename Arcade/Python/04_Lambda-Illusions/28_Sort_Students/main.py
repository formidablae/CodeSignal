def solution(students):
    students.sort(key=lambda student: (student.split(" ")[-1]))
    return students
