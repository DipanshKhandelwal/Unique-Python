class Parent():
    def __init__(self, last_name, eye_color):
        print("Parent constructor called")
        self.last_name = last_name
        self.eye_color = eye_color

billy_cyrus = Parent("Cyrus", "blue")
print(billy_cyrus.last_name)

