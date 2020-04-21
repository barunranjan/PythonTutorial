class Student:
    """
     Here whatever is under the indentation of class is know as class
     class have methods,
     On the basis of class we make object.In line 14 we have make an object
     name as "Student(123,'rahul)" and the variable which is referencing this
     object is known as reference variable. Here "s" is a reference variable
    """
    def __init__(self, rollNo, name,salery):
        self.roll_Number = rollNo
        self.name = name
        self.salery = salery

    def talk(self):
        print("my name is ",self.name)
        print("my roll number is ", self.roll_Number)
        print("my salery is ", self.salery)


s=Student(name='rahul', salery=50000, rollNo=22)
s.talk()




