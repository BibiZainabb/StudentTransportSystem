# transport_manager.py

from bus import Bus
from student import Student
from driver import Driver

class TransportManager:
    def __init__(self):
        self.buses = []
        self.students = []
        self.drivers = []

    def add_bus(self, bus):
        self.buses.append(bus)

    def add_student(self, student):
        self.students.append(student)
        assigned = False
        for bus in self.buses:
            if len(bus.students) < bus.capacity:
                bus.add_student(student)
                assigned = True
                print(f"Assigned {student.name} to Bus {bus.bus_number}")
                break
        if not assigned:
            print(f"No available bus for student {student.name}")

    def add_driver(self, driver, bus_number):
        for bus in self.buses:
            if bus.bus_number == bus_number:
                bus.assign_driver(driver)
                self.drivers.append(driver)
                print(f"Assigned Driver {driver.name} to Bus {bus_number}")
                return
        print(f"Bus {bus_number} not found")

    def show_all_buses(self):
        for bus in self.buses:
            print(bus)
