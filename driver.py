# bus.py

class Bus:
    def __init__(self, bus_number, capacity):
        self.bus_number = bus_number
        self.capacity = capacity
        self.students = []
        self.driver = None

    def assign_driver(self, driver):
        self.driver = driver

    def add_student(self, student):
        if len(self.students) < self.capacity:
            self.students.append(student)
        else:
            print(f"Bus {self.bus_number} is full!")

    def __str__(self):
        return f"Bus {self.bus_number} | Driver: {self.driver.name if self.driver else 'None'} | Students: {len(self.students)}/{self.capacity}"
