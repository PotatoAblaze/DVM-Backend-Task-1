
from datetime import time, timedelta, date, datetime
from enum import Enum

class DayOfTheWeek(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7

class Timeslot:
    
    def __init__(self, day, start_time, duration):
        self.day_of_the_week = day
        self.start_time = start_time
        self.end_time = (datetime.combine(date.today(), self.start_time) + timedelta(hours=self.duration)).time()

class Section:
    
    def __init__(self):
        self.section_number = None
        self.instructors = None
        self.room_no = None
        self.days = []
        self.start_time = None
        self.duration = None
        
    def print_short_section_info(self):
        print(f"Section Number: {self.section_number}")
        print("Instructors: ")
        for name in self.instructors:
            print(name)
        print()
        
        
    def print_section_info(self):
        print(f"Section Number: {self.section_number}")
        print(f"Room Number: {self.room_no}")
        
        print("Instructors: ")
        for name in self.instructors:
            print(name)
        
        # Have to convert to datetime with combine() in order to add with timedelta object, using strftime in order to remove seconds from printing
        print(f"Time: {self.start_time.strftime('%H:%M')} to {(datetime.combine(date.today(), self.start_time) + timedelta(hours=self.duration)).time().strftime('%H:%M')}")
        print("Days: ")
        for day in self.days:
            print(DayOfTheWeek(day).name)
            
        print()