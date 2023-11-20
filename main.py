
from timetable import Timetable, SectionPackage

class Menu:
    
    def __init__(self, table):
        self.table : Timetable = table
        self.start_prompt(False)
    
    def start_prompt(self, pause):
        
        if(pause):
            input("Press Enter to Continue")
        
        prompt = '''
What do you want to do:
1. Show Available Courses
2. Add Course To Timetable
3. Display Timetable
4. Export timetable to CSV
5. Import courses from excel
6. Exit
'''
        
        print(prompt)
        selection = int(input("Your Choice: "))
        print()
        
        match selection:
            case 1:
                self.table.display_courses_in_memory_without_sections()
                self.start_prompt(True)
            case 2:
                self.add_course_to_timetable()
                self.start_prompt(True)
            case 3:
                for c in self.table.timetable_courses.keys():
                    print(f"COURSE: {c}")
                    if(self.table.timetable_courses[c].lecture != None):
                        print("Lecture Section")
                        self.table.timetable_courses[c].lecture.print_section_info()
                    if(self.table.timetable_courses[c].lab != None):
                        print("Lab Section")
                        self.table.timetable_courses[c].lab.print_section_info()
                    if(self.table.timetable_courses[c].tutorial != None):
                        print("Tutorial Section")
                        self.table.timetable_courses[c].tutorial.print_section_info()
                        
                self.start_prompt(True)
            case 4:
                self.table.export_to_csv()
                print("Timetable exported!")
                self.start_prompt(True)
            case 5:
                self.table.load_courses_into_database()
                self.table.load_courses_from_database()
                print("Courses Loaded!")
                self.start_prompt(True)
            case 6:
                print("Thanks for using!")
                exit()
            case _:
                print("Invalid input!")
                self.start_prompt(True)
                
        
    
    def add_course_to_timetable(self):
        
        id = input("Enter course ID (With spaces if any): ")
        found_course = None
        for x in self.table.all_courses:
            if(x.course_id == id):
                found_course = x
                break
        
        if(found_course == None):
            print("Invalid ID")
            return
        
        for x in self.table.timetable_courses.keys():
            if(x == id):
                print("Course is already present in timetable!")
                return

        found_course.get_all_sections_short()
        print()
        
        section_package = SectionPackage()
        self.table.timetable_courses[id] = section_package
        
        has_tutorial = False
        for section in found_course.sections:
            if(section.section_number[0] == 'T'):
                has_tutorial= True
                break
        
        if(found_course.lecture_hours > 0):
            while(True):
                chosen_section = input("Enter desired lecture section (Including letter): ")
                chosen_section_object = None
                
                if(chosen_section[0] != 'L'):
                    print("Not a lecture section!. Try again?")
                    restart = input("Y/N: ")
                    if(restart == 'Y'):
                        continue
                    else:
                        self.table.timetable_courses.pop(id)
                        return
                
                found_flag = False
                for sec in found_course.sections:
                    if(sec.section_number == chosen_section):
                        found_flag = True
                        chosen_section_object = sec
                        break
                
                if(not found_flag):
                    print("Section not found. Try again?")
                    restart = input("Y/N: ")
                    if(restart == 'Y'):
                        continue
                    else:
                        self.table.timetable_courses.pop(id)
                        return
            
                clash_result = self.table.check_clashes(chosen_section_object)
                if(clash_result != False):
                    print(f"Time clashing with {clash_result}. Try again?")
                    restart = input("Y/N: ")
                    if(restart == 'Y'):
                        continue
                    else:
                        self.table.timetable_courses.pop(id)
                        return
                
                
                section_package.lecture = chosen_section_object
                print("Lecture section for this course added!")
                break
            
        if(found_course.lab_hours > 0):
            while(True):
                chosen_section = input("Enter desired lab section (Including letter): ")
                chosen_section_object = None
                
                if(chosen_section[0] != 'P'):
                    print("Not a lab section!. Try again?")
                    restart = input("Y/N: ")
                    if(restart == 'Y'):
                        continue
                    else:
                        self.table.timetable_courses.pop(id)
                        return
                
                found_flag = False
                for sec in found_course.sections:
                    if(sec.section_number == chosen_section):
                        found_flag = True
                        chosen_section_object = sec
                        break
                
                if(not found_flag):
                    print("Section not found. Try again?")
                    restart = input("Y/N: ")
                    if(restart == 'Y'):
                        continue
                    else:
                        self.table.timetable_courses.pop(id)
                        return
            
                clash_result = self.table.check_clashes(chosen_section_object)
                if(clash_result != False):
                    print(f"Time clashing with {clash_result}. Try again?")
                    restart = input("Y/N: ")
                    if(restart == 'Y'):
                        continue
                    else:
                        self.table.timetable_courses.pop(id)
                        return
                
                #self.table.timetable_courses[id] = section_package
                section_package.lab = chosen_section_object
                print("Lab section for this course added!")
                break
            
        if(has_tutorial):
            while(True):
                chosen_section = input("Enter desired tutorial section (Including letter): ")
                chosen_section_object = None
                
                if(chosen_section[0] != 'T'):
                    print("Not a tutorial section!. Try again?")
                    restart = input("Y/N: ")
                    if(restart == 'Y'):
                        continue
                    else:
                        self.table.timetable_courses.pop(id)
                        return
                
                found_flag = False
                for sec in found_course.sections:
                    if(sec.section_number == chosen_section):
                        found_flag = True
                        chosen_section_object = sec
                        break
                
                if(not found_flag):
                    print("Section not found. Try again?")
                    restart = input("Y/N: ")
                    if(restart == 'Y'):
                        continue
                    else:
                        self.table.timetable_courses.pop(id)
                        return
            
                clash_result = self.table.check_clashes(chosen_section_object)
                if(clash_result != False):
                    print(f"Time clashing with {clash_result}. Try again?")
                    restart = input("Y/N: ")
                    if(restart == 'Y'):
                        continue
                    else:
                        self.table.timetable_courses.pop(id)
                        return
                
                #self.table.timetable_courses[id] = section_package
                section_package.tutorial = chosen_section_object
                print("Tutorial section for this course added!")
                break
                    
                
                
            
        

if __name__ == '__main__':
    table = Timetable()
    table.load_courses_from_database()
    menu = Menu(table)
    
    