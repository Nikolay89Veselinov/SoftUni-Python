class Programmer:
    def __init__(self, name, lenguage, skills):
        self.name = name
        self.lenguage = lenguage
        self.skills = skills

    def watch_course(self, course_name, lenguage, gained_skills):
        if lenguage == self.lenguage:
            self.skills += gained_skills
            return f'{self.name} watched {course_name}'
        return f'{self.name} does not know {lenguage}'

    def change_language(self, new_lenguage, skills_neaded):
        old_lenguage = self.lenguage
        if new_lenguage != self.lenguage:
            if skills_neaded <= self.skills:
                self.lenguage = new_lenguage
                return f'{self.name} switched from {old_lenguage} to {self.lenguage}'
            return f'{self.name} needs {skills_neaded - self.skills} more skills '
        return f'{self.name} already knows {new_lenguage}'


programmer = Programmer('John', 'Java', 50)
print(programmer.watch_course('PythonMasterclass', 'Python', 84))
print(programmer.change_language('Java', 30))
print(programmer.change_language('Python', 100))
print(programmer.watch_course('Java: zero to hero', 'Java', 50))
print(programmer.change_language('Python', 100))
print(programmer.watch_course('Python Masterclass', 'Python', 84))