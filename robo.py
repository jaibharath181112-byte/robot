class Robot:
    status = "Active"
    def __init__(self, name):
        self.name = name
    def introduction(self):
        print("System Diagnosis: Connection established.")
    def details(self):
        print(f"Hi Harsh! My name is {self.name}.")
        print(f"My current operational status is: {self.status}.\n")
robot1 = Robot("Tom")
robot2 = Robot("Jerry")
robot1.introduction()
robot1.details()
robot2.introduction()
robot2.details()
