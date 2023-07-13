import time as t


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
        with open("Data files\Tutor.txt", "r+") as tutor:
            tutor_lines = tutor.readlines()
        tutor.close()
        with open("Data files\Students.txt", "r+") as student:
            student_lines = student.readlines()
        student.close()
        return admin_lines, receptionist_lines, tutor_lines, student_lines

    def login(data_lines, counter=0, userline=0, passline=1, status=False):
        data = list(map(str.strip, data_lines))
        while counter < 3:
            username = str(input("Please enter your username ==> "))
            password = str(input("Please enter your password ==> "))
            while userline / 11 < len(data) / 11:
                if username == data[userline] and password == data[passline]:
                    print("Logging in...")
                    t.sleep(1)
                    status = True
                    try:
                        return 0, data[userline : userline + 11], username
                    except:
                        return 0, data[userline:]
                else:  # makes sure all data in Students.txt file is read
                    userline += 11
                    passline += 11
            if status == False:
                print("Incorrect username or password.")
                t.sleep(1)
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
                    return user_info[i : i + 11]
                except:
                    return user_info[i:]
            if i + 1 >= len(user_info):
                return -1

    def update_account():
        pass


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
                t.sleep(1)
                return 2
            if username != data[0] or password != data[1]:
                print("Incorrect username/password.")
                t.sleep(1)
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
            student.write("\nPaid")
        student.close()

    def pending_requests():
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

    def subject_change_request():
        pass


def main(running=True):
    with open("Data files\SubjectSchedules.txt", "r+") as f:
            subject_info = list(map(str.strip, f.readlines()))
    f.close()
    subject_schedule = {'Chinese': [['Monday', 1330, 1530],['Tuesday', 1900, 2100],['Wednesday', 1400, 1500],['Thursday', 1500, 1600], ['Friday', 1200, 1300]],
                        'Malay': [[]]}
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
        "Payment Status"
    ]
    subject_list = [
        "CHINESE",
        "MALAY",
        "ENGLISH",
        "MATHS",
        "SCIENCE",
        "PYHSICS",
        "CHEMISTRY",
        "HISTORY",
        "BIOLOGY",
    ]
    while running:
        login_type = str(
            input(
                "For admin, type A || For receptionists, press R || For tutors, type T || For students, type S || To exit, type E || ==> "
            )
        ).upper()

        # Admin code block
        if login_type == "A":
            admin_lines = User.line_read()[0]
            current_sesh = Admin.login(admin_lines)
            if current_sesh == 2:
                print("Welcome Admin")
                t.sleep(1)

        # Receptionist code block
        elif login_type == "R":
            session = True
            receptionist_lines = Receptionist.line_read()[1]
            current_sesh = Receptionist.login(receptionist_lines)
            user_profile = current_sesh[1]
            if current_sesh == -1:
                print("Login failed")
            elif current_sesh[0] == 0:
                print(f"Welcome {user_profile[2]}.")
                t.sleep(1)
            while session:
                cursor = str(
                    input(
                        "To register a student, type REG || To update subject enrollment of a student, type U || To generate receipts, type REC || To delete a student, type D || To update your profile, type P || To exit, type E || ==> "
                    )
                ).upper()
                if cursor == "REG":
                    student_lines = list(map(str.strip, Student.line_read()[2]))
                    temp = []
                    data = []
                    for i in items:
                        if i == "Username":
                            status = True
                            n = 0
                            while status:
                                new_username = str(input("Please enter username"))
                                if new_username == student_lines[n]:
                                    n += 11
                                    if n == len(student_lines):
                                        print("Username already taken!")
                                        n = 0
                                else:
                                    data.append(new_username)
                                    status = False
                        if i == "Email":
                            pass

                        if i == "Subjects":
                            n = 1
                            print(
                                "The subjects available are " + ", ".join(subject_list)
                            )
                            while n <= 3:
                                choice = str(
                                    input(f"Please enter subject {n} ==> ")
                                ).upper()
                                if choice not in subject_list:
                                    print("That's not a valid subject")
                                else:
                                    temp.append(choice)
                                    n += 1
                            data.append(",".join(temp))
                        else:
                            print(data)
                            data.append(str(input(f"Please enter {i} ==> ")))
                    Receptionist.register(data)
                    print("User registered.")
                    t.sleep(0.5)
                elif cursor == "D":
                    wanted_user = str(
                        input(
                            "Enter username of the profile you would like to delete ==> "
                        )
                    )
                    confirmation = str(input("Are you sure? (y/n) ==> ")).upper()
                    if confirmation == "Y":
                        wanted_user_data = Student.retrieve_info(wanted_user, 2)
                        if wanted_user_data == -1:
                            print("User not found.")
                            t.sleep(1)
                            print("Going back...")
                            t.sleep(1)
                        else:
                            Receptionist.delete_student(wanted_user, wanted_user_data)
                            t.sleep(0.5)
                            print("User deleted!")
                            t.sleep(0.5)
                    elif confirmation == "N":
                        print("Going back...")
                        t.sleep(1)
                elif cursor == "E":
                    print("Logging out...")
                    t.sleep(1)
                    print("Logout successfull.")
                    t.sleep(0.5)
                    session = False

        elif login_type == "T":
            session = True
            tutor_lines = Tutor.line_read()[2]
        # Student code block
        elif login_type == "S":
            session = True
            student_lines = Student.line_read()[3]
            current_sesh = Student.login(student_lines)
            user_profile = current_sesh[1]
            username = current_sesh[2]
            if current_sesh == -1:
                print("Login failed")
            elif current_sesh[0] == 0:
                print(f"Welcome {user_profile[2]}.")
                t.sleep(1)
            while session:
                cursor = str(
                    input(
                        "To update your profile, type U || To view your schedule, type V || To send a subject change request, type R || To view payment status, type P || ==> "
                    )
                ).upper()
                if cursor == "U":
                    for i in range(len(user_profile)):
                        print(f"|{i+1}| {items[i]}: {user_profile[i]}")
                    t.sleep(1)
                    print("What would you like to edit?")
                    print(Student.retrieve_info(username, 2))
                    session = False

        elif login_type == "E":
            print("Exiting system...")
            t.sleep(1)
            running = False


if __name__ == "__main__":
    print("Welcome to Tuition Centre XY")
    main()
