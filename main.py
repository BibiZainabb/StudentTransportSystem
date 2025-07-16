# main.py

from transport_manager import TransportManager
from student import Student
from driver import Driver
from bus import Bus

manager = TransportManager()

# Create buses
b1 = Bus("BUS-10", 2)
b2 = Bus("BUS-11", 1)

manager.add_bus(b1)
manager.add_bus(b2)

# Add drivers
d1 = Driver(101, "Mr. Ahmed", "LIC12345")
d2 = Driver(102, "Miss Aisha", "LIC98765")

manager.add_driver(d1, "BUS-10")
manager.add_driver(d2, "BUS-11")

# Add students
s1 = Student(1, "Zainab")
s2 = Student(2, "Fatima")
s3 = Student(3, "Munazzah")

manager.add_student(s1)
manager.add_student(s2)
manager.add_student(s3)

manager.show_all_buses()
