class User:
    def __init__(self, ID: str, Password: str, Name: str, Age: int):
        self.ID = ID
        self.Password = Password
        self.Name = Name
        self.Age = Age

    def line_read():
        with open("Data files\Admin.txt", "r+") as admin:
            admin_lines = admin.readlines()
        admin.close()
        with open("Data files\Students.txt", "r+") as student:
            student_lines = student.readlines()
        student.close()

        return admin_lines, student_lines


class Admin(User):
    def __init__(self, ID, Password, Name, Age):
        User.__init__(ID, Password, Name, Age)

    # 2 = admin, 1 = employees, 0 = students
    def login(ID, Password, admin_lines, student_lines):
        if ID == admin_lines[0][:-1] and Password == admin_lines[1]:
            print("Logging in...")
            return 2

        if ID != admin_lines[0][:-1] or Password != admin_lines[1]:
            print("Incorrect username/password. Try again.")
            main()

    def register():
        pass

    pass


class Receptionist(User):
    def __init__(self, ID, Password, Name, Age):
        User.__init__(ID, Password, Name, Age)

    pass


class Tutor(User):
    def __init__(self, ID, Password, Name, Age):
        User.__init__(ID, Password, Name, Age)

    pass


class Student(User):
    def __init__(self, ID, Password, Name, Age):
        User.__init__(ID, Password, Name, Age)

    pass


def main():
    login_type = str(input("For admin, type A || For receptionists, press R || For tutors, type T || For students, type S || "))
    username = str(input("Please enter your username: "))
    password = str(input("Please enter your password: "))
    admin_lines = User.line_read()[0]
    student_lines = User.line_read()[1]
    current_sesh = Admin.login(username, password, admin_lines, student_lines)
    if current_sesh == 2:
        print("Welcome Admin")


print("Welcome to Tuition Centre XY")
main()
