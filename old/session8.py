# numbers = (1,2,3,4,5)
# for n in numbers:
#     print(n)

# print(numbers[:4])
# numbers[0] = 3 # error

# student = {
#     "name" : "sara",
#     "family" : "blalalal",
#     "age" : 24,
#     "grade" : 18
# }
# print(student["name"])
# print(student["family"])
# student["age"] = 34
# student["national_code"] = "22222222"
# del student["family"]
# print(student)
# for key, val in student.items():
#     print(key, val)
# student = {
#     "name" : "sara",
#     "family" : "blalalal",
#     "age" : 24,
#     "grade" : 18
# }
# keys = list(student.keys())
# keys_length = len(keys)
# i = 0
# while i < keys_length:
#     print(keys[i], student[keys[i]])
#     i += 1


# numbers = {1,2,3,4,5,1,2,3,4,5,16}
# print(numbers)

# # names = ["ali", "sara", "abtin", "reza", "abtin", "reza"]

# # names = list(set(names))
# # print(names)
# names ={"ali", "sara", "abtin", "reza", "abtin", "reza"}
# names.add("samira")
# names.remove("reza")
# print(names)

# if "ali" in names:
#     print("yes")


grades = {}
for i in range(3):
    name = input("enter the name: ")
    g = float(input("enter the grade: "))
    grades[name] = g


print("student's grades: ")
for name,g in grades.items():
    print(name, ":", g)