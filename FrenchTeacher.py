from Winner import Teacher


class FrenchTeacher(Teacher):
    def is_fluent(self):
        return True


frenchteacher1 = FrenchTeacher("barbra", "GSS", "french", 56, 7, "her")
print(frenchteacher1.is_punctual())