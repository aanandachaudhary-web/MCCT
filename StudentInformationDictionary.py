student = {
    "name": "Ram",
    "age": 19,
    "course": "BCA",
    "marks": 78
}

print("Original student information:")
print(student)

student["marks"] += 5

if student["marks"] >= 40:
    student["status"] = "Pass"
else:
    student["status"] = "Fail"

print(student)