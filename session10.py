# try:
#     file = open("test", "w")
#     file.write("hello every  body")
#     file.close()
# except FileNotFoundError:
#     print("error")
# finally:
#     print("blalalal")
# try:

#     file = open("test", "r")
#     content = file.read()
#     print(content)
#     file.close()
# except:
#     print("file not found")


# shopping_list = ["milk", "b;alalla"]

# with open("shopping.txt", "a") as file:
#     for item in shopping_list:
#         file.write(item + "\n")

file = open("test2.txt", "a")
while True:
    text = input("enter a text: ")
    file.write(text+"\n")
    if input("Do you want to quit(y n):? ") == "y":
        break
file.close()
