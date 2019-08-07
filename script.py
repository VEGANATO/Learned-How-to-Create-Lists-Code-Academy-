# I am a student trying to organize subjects and grades using Python. I am organizing the subjects and scores.
print("This Year's Subjects and Grades: ")
subjects = ["physics", "calculus", "poetry", "history"]
grades = [98, 97, 85, 88]

subjects.append("computer science")
grades.append(100)

gradebook = list(zip(grades, subjects))

gradebook.append(("visual arts", 93))
print(gradebook)

last_semester_gradebook = [("politics", 80), ("latin", 96), ("dance", 97), ("architecture", 65)]

full_gradebook = gradebook + last_semester_gradebook
print("Last Year's Subjects and Grades: ")
print(full_gradebook)
