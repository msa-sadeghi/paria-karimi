# def greet(name):
#     print(f"hello {name}")
#     print("how are you?")

# greet("sara")

# def add(a, b, c):
#     return a + b + c
# x = add(13,2,3)

# if x > 10:
#     print(f"{x} is greater than 10")


# def greet(name="sara"):
#     print(f"hello {name}")
#     print("how are you?")

# greet()
# greet("armin")


# def outer():
#     print("outer...")
#     def inner():
#         print("inner")
#     inner()

# outer()

# x = 10
# def func():
#     x = 4
#     print(x)

# func()
# print(x)

# count = 0
# def login(username, password):
#     global count
#     count += 1
#     if username == "admin" and password == "1234":
#         return "success"
#     return "not success"

# while count < 3:
#     username = input("enter the username: ")
#     password = input("enter the password: ")
#     if login(username, password) == "success":
#         print("admin welcome to my site")
#     else:
#         print("username or password is not correct")
    

# def average(numbers):
#     return sum(numbers) / len(numbers)

# print(average([10, 20, 30]))

# def validate_national_code(code):
#     return len(code) == 10 and code.isdigit()

# print(validate_national_code("1234567891"))
# print(validate_national_code("12345678"))
# print(validate_national_code("12345678sd4"))


# def maximum(numbers):
#     max_ = numbers[0]
#     for n in numbers:
#         if n > max_:
#             max_ = n
#     return max_

# print(maximum([2,4,8,5,1]))

def calc_len(string):
    l = 0
    for s in string:
        l += 1
    return l
print(calc_len("hello how are you"))