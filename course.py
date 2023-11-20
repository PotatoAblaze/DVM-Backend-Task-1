from section import Section
from datetime import time, date

class Course:
    
    def __init__(self):
        self.course_id = None
        self.course_name = None
        self.sections = []
        self.units = None
        self.lecture_hours = None
        self.lab_hours = None
        self.midsem_date = None
        self.compre_date = None
        
    def get_all_sections(self):
        
        for section in self.sections:
            section.print_section_info()
    
    def get_all_sections_short(self):
        for section in self.sections:
            section.print_short_section_info()
            
    def __str__(self):
        
        line1 = f"Course ID: {self.course_id}"
        line2 = f"Course Name: {self.course_name}"
        line3 = f"Units: {self.units}"
        
        return '\n'.join([line1, line2, line3])
    
    def populate_section(self):
        new_section = Section()
        new_section.section_number = input("Enter section number: ")
        new_section.room_no = input("Enter room number: ")
        
        instructor_names = input("Enter names of instructors separated by comma: ").strip().split()
        instructor_names = [name.strip() for name in instructor_names]
        new_section.instructors = instructor_names
        
        start_time = int(input("Enter starting hour in 24-hours format (for example, a class starting at 1pm, enter 13)"))
        new_section.start_time = time(hour=start_time, minute=0, second=0)
        
        new_section.duration = int(input("Enter duration of class in hours: "))
        
        class_days = input("Enter days of a week as a continuous string separated by spaces (Eg: 'T Th S' for Tuesday Thursday Saturday): ").strip().split()
        
        for day in class_days:
            day_int = 0
            match day:
                case 'M':
                    day_int = 1
                case 'T':
                    day_int = 2
                case 'W':
                    day_int = 3
                case 'Th':
                    day_int = 4
                case 'F':
                    day_int = 5
                case 'S':
                    day_int = 6
                case 'Su':
                    day_int = 7
            
            if(day_int != 0):
                new_section.days.append(day_int)
                    