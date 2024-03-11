class Student():
    count = 0

    def __init__(self, id, name):
        self.id = id
        self.name = name
        Student.count += 1

    def set_id(self, id):
        self.id = id

    def get_id(self):
        return self.id

    def set_Name(self, name):
        self.name = name

    def get_Name(self):
        return self.name

    def show_Infor(self):
        print(f"ID: {self.get_id()}, ten sinh vien: {self.get_Name()}")


sv = Student("SV01", "Nguyenthanhchung")
sv1 = Student("SV01", "Nguyenthanhchung")
sv2 = Student("SV01", "Nguyenthanhchung")

# print(Student.count)
