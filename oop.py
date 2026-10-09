class Students:
    def __init__(self, name, age, gender, course):
        self.name = name
        self.age = age
        self.gender = gender
        self.course = course



    def Study(self):
        print("Student Is Studying")


    def sing(self):
        print("Student Is Singing")

student1 = Students("James", 21, "Male", "MIT")

student2 = Students("Harriet", 19, "Female", "Physiology")

student3 = Students("Michael", 20, "Male", "Medicine")

student4 = Students("Layla", 22, "Female", "Engineering")



