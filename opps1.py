class Employee:
    def __init__(self):
        print("Subclass initialized")
        self.id = 123
        self.salary = 50000
        self.designation = "SDE"
        print("Employee details initialized")

    def travel(self, destination):
        print("This travel method is called manually")
        print(f"Traveling to {destination}")


sam = Employee()
sam.travel("New York")