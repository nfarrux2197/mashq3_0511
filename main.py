class Student:
    def __init__(self, score):
        self.score = score

    @property
    def grade(self):
        if self.score >= 90:
            return "A"
        elif self.score >= 80:
            return "B"
        elif self.score >= 70:
            return "C"
        elif self.score >= 60:
            return "D"
        else:
            return "F"

    @grade.setter
    def grade(self, letter):
        grades = {"A": 95, "B": 85, "C": 75, "D": 65, "F": 50}
        if letter in grades:
            self.score = grades[letter]
        else:
            raise ValueError("Noto‘g‘ri baho harfi kiritildi!")


s = Student(82)
print(f"Talaba bali: {s.score}, bahosi: {s.grade}")
s.grade = "A"
print(f"Yangi baho: {s.grade}, yangi ball: {s.score}")
print("-" * 40)
