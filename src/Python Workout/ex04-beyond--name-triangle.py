def name_triangle():
    name = input("Enter your name: ")
    for i in range(len(name) + 1):
        print(name[:i])


name_triangle()
