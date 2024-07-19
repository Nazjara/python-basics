def method_1():
    print("Method 1")


class MyClass:

    def class_method_1(self):
        print("Class Method 1")


if __name__ == "__main__": # without this if statement, underlying code will be executed when calling methods of module1 from module2
    method_1()
    MyClass().class_method_1()
