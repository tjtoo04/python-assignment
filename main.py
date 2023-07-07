class User:
    def __init__(self, Username: str, Password: str, Name: str, IC: str, Email: str, Contact_number: str, Address: str, Level: str, Subjects: str, Month_of_enrollment: str):
        self.Username = Username
        self.Password = Password
        self.Name = Name
        self.IC = IC
        self.Email = Email
        self.Contact_number = Contact_number
        self.Address = Address
        self.Level = Level
        self.Subjects = Subjects
        self.Month_of_enrollment = Month_of_enrollment

    def line_read():
        with open("Data files\Admin.txt", "r+") as admin:
            admin_lines = admin.readlines()
        admin.close()
        with open("Data files\Students.txt", "r+") as student:
            student_lines = student.readlines()
        student.close()

        return admin_lines, student_lines


class Admin(User):
    def __init__(self, Username: str, Password: str, Name: str, IC: str, Email: str, Contact_number: str, Address: str, Level: str):
        User().__init__(Username, Password, Name, IC, Email, Contact_number, Address, Level)

    # 2 = admin, 1 = employees, 0 = students
    def login(admin_lines, counter=0):
        while counter < 3:
            username = str(input("Please enter your username: "))
            password = str(input("Please enter your password: "))
            if username == admin_lines[0][:-1] and password == admin_lines[1]:
                print("Logging in...")
                return 2
            if username != admin_lines[0][:-1] or password != admin_lines[1]:
                print("Incorrect username/password.")
                counter += 1
            if counter == 3:
                print("Login attempts reached.")

    def register():
        pass


class Receptionist(User):
    def __init__(self, Username: str, Password: str, Name: str, IC: str, Email: str, Contact_number: str, Address: str, Level: str):
        User().__init__(Username, Password, Name, IC, Email, Contact_number, Address, Level)

    def login():
        pass


class Tutor(User):
    def __init__(self, Username: str, Password: str, Name: str, IC: str, Email: str, Contact_number: str, Address: str, Level: str):
        User().__init__(Username, Password, Name, IC, Email, Contact_number, Address, Level)

    pass


class Student(User):
    def __init__(self, Username: str, Password: str, Name: str, IC: int, Email: str, Contact_number: int, Address: str, Level: int, Subjects: str, Month_of_enrollment: str):
        User().__init__(Username, Password, Name, IC, Email, Contact_number, Address, Level, Subjects, Month_of_enrollment)
        

    def login(student_lines, counter=0, userline=0, passline=1, status=False):
        while counter < 3:
            username = str(input("Please enter your username: "))
            password = str(input("Please enter your password: "))
            while userline / 10 < len(student_lines) / 10:
                if (
                    username == student_lines[userline][:-1]
                    and password == student_lines[passline][:-1]
                ):
                    print("Logging in...")
                    status = True
                    return 0, student_lines[userline:]
                else:
                    userline += 10
                    passline += 10
            if status == False:
                print("Incorrect username or password.")
                counter += 1
                userline = 0
                passline = 1
            if counter == 3:
                print("Login attempts reached.")
                return -1
    
    def retrieve_info():
        user_info = User.line_read()[1]
        for i, j in enumerate(user_info):
            if j[:-1] == "ssss":
                return user_info[i:]


        pass

def main(editing = True):
    items = ['Username', 'Password', 'Name', 'IC', 'Email', 'Contact_number', 'Address', 'Level', 'Subjects', 'Month_of_enrollment']
    login_type = str(
        input(
            "For admin, type A || For receptionists, press R || For tutors, type T || For students, type S || "
        )
    ).upper()
    if login_type == "A":  # Admin block
        admin_lines = User.line_read()[0]
        current_sesh = Admin.login(admin_lines)
        if current_sesh == 2:
            print("Welcome Admin")
    elif login_type == "S":  # Student block
        student_lines = User.line_read()[1]
        current_sesh = Student.login(student_lines)
        user_profile = current_sesh[1]
        if current_sesh == -1:
            print("Login failed")
        elif current_sesh[0] == 0:
            print(f"Welcome {current_sesh[1][2][:-1]}.")
        cursor = str(
            input(
                "To update your profile, type U || To view your schedule, type V || To send a subject change request, type R || To view payment status, type P ||"
            )
        ).upper()
        while editing == True:
            if cursor == "U":
                for i in range(len(user_profile)):
                    print(
                        f"|| {items[i]}: {user_profile[i][:-1]}"
                    )
                print("What would you like to edit?")
                print(Student.retrieve_info())
                editing = False


# student_lines = User.line_read()[1]


print("Welcome to Tuition Centre XY")
main()
