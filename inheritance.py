class Parent():
    def __init__(self, last_name, eye_color):
        print("Parent contructor called.")
        self.last_name = last_name
        self.eye_color = eye_color



class Child(Parent):
    def __init__(self, last_name, eye_color, number_of_toys):
        print("Child Constructor called")
        Parent.__init__(self, last_name,eye_color)
        self.number_of_toys = number_of_toys


#loma = Parent("Amol", "Black")
#print(loma)

Yatharth = Child("Wankhede", "Black", 20)

print(Yatharth.last_name)
print(Yatharth.number_of_toys)
