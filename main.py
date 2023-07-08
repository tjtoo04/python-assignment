class User:
    def __init__(
        self,
        Username: str,
        Password: str,
        Name: str,
        IC: str,
        Email: str,
        Contact_number: str,
        Address: str,
        Level: str,
        Subjects: str,
        Month_of_enrollment: str,
    ):
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

    # Reads every line of data in Admin.txt (index 0), Receptionist.txt (index 1) and Students.txt (index 2)
    def line_read():
        with open("Data files\Admin.txt", "r+") as admin:
            admin_lines = admin.readlines()
        admin.close()
        with open("Data files\Receptionist.txt", "r+") as receptionist:
            receptionist_lines = receptionist.readlines()
        receptionist.close()
        with open("Data files\Students.txt", "r+") as student:
            student_lines = student.readlines()
        student.close()
        return admin_lines, receptionist_lines, student_lines

    def login(data_lines, counter=0, userline=0, passline=1, status=False):
        data = list(map(str.strip, data_lines))
        while counter < 3:
            username = str(input("Please enter your username ==> "))
            password = str(input("Please enter your password ==> "))
            while userline / 10 < len(data) / 10:
                if username == data[userline] and password == data[passline]:
                    print("Logging in...")
                    status = True
                    try:
                        return 0, data[userline : userline + 10], username
                    except:
                        return 0, data[userline:]
                else:  # makes sure all data in Students.txt file is read
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

    # n = 0 for admin info, n = 2 for student info (for now)
    def retrieve_info(username, n):
        user_info = list(map(str.strip, User.line_read()[n]))
        for i, j in enumerate(user_info):
            if j == username:
                try:
                    return user_info[i : i + 10]
                except:
                    return user_info[i:]
            if i > len(user_info):
                return "User not found"


class Admin(User):
    def __init__(
        self,
        Username: str,
        Password: str,
        Name: str,
        IC: str,
        Email: str,
        Contact_number: str,
        Address: str,
        Level: str,
    ):
        User().__init__(
            Username, Password, Name, IC, Email, Contact_number, Address, Level
        )

    # 2 = admin, 1 = employees, 0 = students
    def login(admin_lines, counter=0):
        data = list(map(str.strip, admin_lines))
        while counter < 3:
            username = str(input("Please enter your username ==> "))
            password = str(input("Please enter your password ==> "))
            if username == data[0] and password == data[1]:
                print("Logging in...")
                return 2
            if username != data[0] or password != data[1]:
                print("Incorrect username/password.")
                counter += 1
            if counter == 3:
                print("Login attempts reached.")

    def register():
        pass


class Receptionist(User):
    def __init__(
        self,
        Username: str,
        Password: str,
        Name: str,
        IC: str,
        Email: str,
        Contact_number: str,
        Address: str,
        Level: str,
        Subjects: str,
        Month_of_enrollment: str,
    ):
        super().__init__(
            Username,
            Password,
            Name,
            IC,
            Email,
            Contact_number,
            Address,
            Level,
            Subjects,
            Month_of_enrollment,
        )

    # Registers new students
    def register(data):
        with open("Data files\Students.txt", "a+") as student:
            for i in range(len(data)):
                student.write("\n")
                student.write(data[i])
        student.close()

    def subject_change_requests():
        pass

    # Deletes the desired student's info
    def delete_student(username, user_data, n=0):
        with open("Data files\Students.txt", "r+") as student:
            student_lines = list(map(str.strip, student.readlines()))
            student.seek(0)
            student.truncate()
            for i in student_lines:
                if n < len(user_data):
                    if i != user_data[n]:
                        student.write(i + "\n")
                    else:
                        n += 1
                else:
                    student.write(i + "\n")
        student.close()


class Tutor(User):
    def __init__(
        self,
        Username: str,
        Password: str,
        Name: str,
        IC: str,
        Email: str,
        Contact_number: str,
        Address: str,
        Level: str,
        Subjects: str,
        Month_of_enrollment: str,
    ):
        super().__init__(
            Username,
            Password,
            Name,
            IC,
            Email,
            Contact_number,
            Address,
            Level,
            Subjects,
            Month_of_enrollment,
        )


class Student(User):
    def __init__(
        self,
        Username: str,
        Password: str,
        Name: str,
        IC: str,
        Email: str,
        Contact_number: str,
        Address: str,
        Level: str,
        Subjects: str,
        Month_of_enrollment: str,
    ):
        super().__init__(
            Username,
            Password,
            Name,
            IC,
            Email,
            Contact_number,
            Address,
            Level,
            Subjects,
            Month_of_enrollment,
        )

    def change_request():
        pass


def main(using=True):
    items = [
        "Username",
        "Password",
        "Name",
        "IC",
        "Email",
        "Contact_number",
        "Address",
        "Level",
        "Subjects",
        "Month_of_enrollment",
    ]
    subject_list = [
        "Chinese",
        "English",
        "Maths",
        "Science",
        "Physics",
        "Chemistry",
        "History",
        "Biology",
    ]
    login_type = str(
        input(
            "For admin, type A || For receptionists, press R || For tutors, type T || For students, type S || ==> "
        )
    ).upper()

    # Admin code block
    if login_type == "A":
        admin_lines = User.line_read()[0]
        current_sesh = Admin.login(admin_lines)
        if current_sesh == 2:
            print("Welcome Admin")

    # Receptionist code block
    elif login_type == "R":
        receptionist_lines = Receptionist.line_read()[1]
        current_sesh = Receptionist.login(receptionist_lines)
        user_profile = current_sesh[1]
        if current_sesh == -1:
            print("Login failed")
        elif current_sesh[0] == 0:
            print(f"Welcome {user_profile[2]}.")
        while using:
            cursor = str(
                input(
                    "To register a student, type REG || To update subject enrollment of a student, type U || To generate receipts, type REC || To delete a student, type D || To update your profile, type P || ==> "
                )
            ).upper()
            if cursor == "REG":
                temp = []
                data = []
                for i in items:
                    if i == "Subjects":
                        print("The subjects available are " + ", ".join(subject_list))
                        temp.append(str(input("Please enter subject 1 ==>")))
                        temp.append(str(input("Please enter subject 2 ==>")))
                        temp.append(str(input("Please enter subject 3 ==>")))
                        data.append(",".join(temp))
                    else:
                        data.append(str(input(f"Please enter your {i}")))
                Receptionist.register(data)
            elif cursor == "D":
                wanted_user = str(
                    input("Enter username of the profile you would like to delete ==> ")
                )
                confirmation = str(input("Are you sure? (y/n) ==> ")).upper()
                if confirmation == "Y":
                    wanted_user_data = Student.retrieve_info(wanted_user, 2)
                    Receptionist.delete_student(wanted_user, wanted_user_data)
                    print("User deleted!")
                    using = False
                elif confirmation == "N":
                    pass

    # Student code block
    elif login_type == "S":
        student_lines = Student.line_read()[2]
        current_sesh = Student.login(student_lines)
        user_profile = current_sesh[1]
        username = current_sesh[2]
        if current_sesh == -1:
            print("Login failed")
        elif current_sesh[0] == 0:
            print(f"Welcome {user_profile[2]}.")
        while using:
            cursor = str(
                input(
                    "To update your profile, type U || To view your schedule, type V || To send a subject change request, type R || To view payment status, type P || ==> "
                )
            ).upper()
            if cursor == "U":
                for i in range(len(user_profile)):
                    print(f"|| {items[i]}: {user_profile[i]}")
                print("What would you like to edit?")
                print(Student.retrieve_info(username, 2))
                using = False


if __name__ == "__main__":
    print("Welcome to Tuition Centre XY")
    main()
