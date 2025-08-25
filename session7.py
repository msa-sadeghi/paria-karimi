# names = ["artin","abtin", "nikan", "sara"]
# print(names)
# print(names[0])
# print(names[-1])
# print(names[:2])

# new_name = input("enter a name: ")
# names.remove(new_name)
# del names[0]
# names.pop(1)
# print(names)


# numbers = []
# for i in range(3):
#     new_number =  int(input("enter a number: "))
#     numbers.append(new_number)
# print(numbers)
# print(sum(numbers))



names = []

while True:
    n = input("enter a name: ")
    if n[0] == "a" or n[0] ==  "A":
        names.append(n)
    if input("Do you want to quit (y or n): ") == "y":
        break

print(names)