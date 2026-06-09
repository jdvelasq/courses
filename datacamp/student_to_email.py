with open("datacamp/students.txt", encoding="utf-8") as file:
    students = file.read().splitlines()

emails = [student.split(" <")[1] for student in students]
with open("datacamp/emails.txt", "w", encoding="utf-8") as file:
    file.write("\n".join(emails))
