class Teacher:
    def __init__(self, name, form, courses, rank, arrival, gender):
        self.name = name
        self.form = form
        self.courses = courses
        self.rank = rank
        self.arrival = arrival
        self.gender = gender


    def is_good_teacher(self):
        if self.rank >= 70:
            return True
        else:
            return False

    def is_punctual(self):
        if self.arrival <= 8:
            print("Yes this teacher is punctual")
        else:
            print(f"{self.name} needs to improve on {self.gender} punctuality qualities")


teacher1 = Teacher("samuel", "CEET", "CSE518", 89, 9, "his")
print(teacher1.is_good_teacher())
teacher1.is_punctual()
