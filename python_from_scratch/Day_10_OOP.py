class Employee:
    # Class attributes
    company_name = "TCS"
    # Mandatory initialization method
    def __init__(self, name, age, designation):
        self.name = name
        self.age = age
        self.designation = designation
    # Optional description method
    def __str__(self):
        return f"Hi I am {self.name}, and I am a happy employee of this company"
    # User defined methods
    def is_present(self):
        return True
    def is_absent(self):
        if self.is_present():
            print("Not Absent")
        else:
            print("Absent")


ashish = Employee("Ashish","xx","desg1")
balaka = Employee("Balaka", "xx", "desg2")

# print(ashish.name)    # object_name.property_name OR object_name.method_name
# print(balaka.is_present())
print(ashish)
print(balaka)

