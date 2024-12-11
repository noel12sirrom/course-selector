class CourseClss():
    def __init__(self, course_code, module_name, credits, semester, is_elective, prerequisites=None):
        self.course_code = course_code
        self.module_name = module_name
        self.credits = credits
        self.semester = semester
        self.is_elective = is_elective
        self.prerequisites = prerequisites if prerequisites else []

    def __repr__(self):
        return (f"Course Code: {self.course_code}\nModule Name: {self.module_name}\n"
                f"Credits: {self.credits}\nSemester: {self.semester}\nElecetive: {self.is_elective}\n"
                f"Prerequisites: {self.prerequisites}\n\n")
    
module_dict = {}

def parse_modules(modules):
    for module in modules:
        course_code = module[0]
        prerequisite = module[6]
        if course_code in module_dict: #checks if the last thing in the list's is id the same as current module
            if not module[7] and not module[8]:
                module_dict[course_code].prerequisites.append(module[6])
            elif module[7] and not module[8]:
                module_dict[course_code].prerequisites.append(f"{prerequisite}(Co-Requisite)")
            elif module[8] and not module[7]:
                module_dict[course_code].prerequisites.append(f"{prerequisite}(optional)")
            elif module[8] and module[7]:
                module_dict[course_code].prerequisites.append(f"{prerequisite}(optional, Co-Requisite)")
        else:
            currModule = CourseClss(
                course_code= module[0],
                module_name=module[1],
                credits=module[2],
                semester=module[3],
                is_elective="Yes" if module[4] == 1 else "No",
                prerequisites=[]
            )
            # Add the first prerequisite if applicable
            if prerequisite:
                if not module[7] and not module[8]:
                    currModule.prerequisites.append(prerequisite)
                elif module[7] and not module[8]:
                    currModule.prerequisites.append(f"{prerequisite}(Co-Requisite)")
                elif module[8] and not module[7]:
                    currModule.prerequisites.append(f"{prerequisite}(optional)")
                elif module[8] and module[7]:
                    currModule.prerequisites.append(f"{prerequisite}(optional, Co-Requisite)")

            module_dict[course_code] = currModule
    return [course for course in module_dict.values()]