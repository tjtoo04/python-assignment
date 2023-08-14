import time as t
import subject_schedule
from dataclasses import dataclass


@dataclass
class User:
    Username: str
    Password: str
    Name: str
    IC: str
    Email: str
    Contact_number: str
    Address: str
    Level: str
    Subjects: str
    Month_of_enrollment: str

    # Reads every line of data in Admin.txt (index 0), Receptionist.txt (index 1), Tutor.txt (index 2) and AllUserData.txt (index 3)
    def line_read():
        with open("Data files\AllUserData.txt", "r+") as f:
            data = list(map(str.strip, f.readlines()))
        return data

    def login(counter=0):
        data = User.line_read()
        while counter < 3:
            username = input("Please enter your username ==> ")
            password = input("Please enter your password ==> ")
            for i, j in enumerate(data):
                try:
                    if username == j and password == data[i + 1]:
                        print("Logging in...")
                        return data[i - 1 : i + 11]
                except IndexError:
                    print("Incorrect username or password.")
                    counter += 1
                if counter == 3:
                    print("Login attempts reached.")
                    return -1

    def authenticator(data):
        if data[0] == "Admin":
            return 0
        elif data[0] == "Receptionist":
            return 1
        elif data[0] == "Tutor":
            return 2
        elif data[0] == "Student":
            return 3

    # user_type = 0 for admin info, user_type = 1 for Receptionist info, user_type= 2 for tutor info, user_type = 3 for student info
    def retrieve_info(username):
        user_info = User.line_read()
        for i, j in enumerate(user_info):
            if j == username:
                try:
                    return user_info[i - 1 : i + 11]
                except IndexError:
                    return user_info[i - 1 :]
            if i + 1 >= len(user_info):
                return -1

    def update_account(wanted_change_index, changed_info, username):
        data = User.line_read()
        with open("Data files\AllUserData.txt", "r+") as cursor:
            for i, j in enumerate(data):
                if j == username:
                    try:
                        data[i + (wanted_change_index - 2)] = changed_info
                        cursor.seek(0)
                        cursor.truncate()
                        for x in range(len(data)):
                            cursor.write(data[x])
                            if x < len(data) - 1:
                                cursor.write("\n")
                    except:
                        data[wanted_change_index - 2] = changed_info
                        cursor.seek(0)
                        cursor.truncate()
                        for x in range(len(data)):
                            cursor.write(data[x])
                            if x < len(data) - 1:
                                cursor.write("\n")


@dataclass
class Admin(User):
    def register():
        pass


@dataclass
class Receptionist(User):
    # Registers new students
    def register(data):
        with open("Data files\AllUserData.txt", "a+") as student:
            for i in range(len(data)):
                student.write("\n")
                student.write(data[i])
            student.write("\nPaid")
        student.close()

    def delete_requests(user_choice, subject_list, user_index):
        with open("Data files/StudentRequests.txt", "r+") as cursor:
            requests = list(map(str.strip, cursor.readlines()))
            cursor.seek(0)
            cursor.truncate()
            for j in requests:
                if j != user_choice and j != subject_list[user_index]:
                    cursor.writelines(f"{j}\n")

    def subject_enrollment_changer(username_list=[], subject_list=[]):
        with open("Data files/StudentRequests.txt", "r") as f:
            student_request_data = list(map(str.strip, f.readlines()))
            for i, j in enumerate(student_request_data):
                username_list.append(j) if i % 2 == 0 else subject_list.append(j)
        print(f"Total number of pending requests: {len(subject_list)}")
        print(f"Pending requests from: {', '.join(set(username_list))}")
        while True:
            user_choice = input("Enter the user to check on their requests ==> ")
            if user_choice in username_list:
                user_index = username_list.index(user_choice)
                all_student_data = User.line_read()
                user_subjects = subject_list[user_index].split(",")
                for i, j in enumerate(all_student_data):
                    if j == user_choice:
                        wanted_student_data = all_student_data[i - 1 : i + 12]
                        print(
                            f"{user_choice} would like to change their enrollment of {user_subjects[0]} to {user_subjects[1]}."
                        )
                approval = input(
                    "Do you want to approve this request? (Y/N) ==> "
                ).upper()
                if approval == "N":
                    Receptionist.delete_requests(user_choice, subject_list, user_index)
                    print("Request deleted.")
                elif approval == "Y":
                    old_student_subjects = wanted_student_data[9].split(",")
                    for index, subject in enumerate(old_student_subjects):
                        if subject == user_subjects[0]:
                            old_student_subjects[index] = user_subjects[1]
                            new_student_data = wanted_student_data[9] = ",".join(
                                old_student_subjects
                            )

                    with open("Data files/AllUserData.txt", "r+") as cursor:
                        student_lines = User.line_read()
                        for i, line in enumerate(student_lines):
                            if line == user_choice:
                                student_lines[i + 8] = new_student_data
                        cursor.seek(0)
                        cursor.truncate
                        for line in student_lines:
                            cursor.writelines(f"{line}\n")
                    Receptionist.delete_requests(user_choice, subject_list, user_index)
                    print("Request deleted.")
            else:
                print("Invalid user")

    # Deletes the desired student's info
    def delete_student(user_data):
        with open("Data files/AllUserData.txt", "r+") as cursor:
            data_lines = User.line_read()
            cursor.seek(0)
            cursor.truncate()
            data_lines.pop(data_lines.index(user_data[1])-1)
            for i in user_data[1:]:
                data_lines.pop(data_lines.index(i))
            for i in data_lines:
                cursor.write(f"{i}\n")



@dataclass
class Tutor(User):
    def check_schedules():
        pass


@dataclass
class Student(User):
    def subject_change_requests(name, wanted_change, changed_subject):
        with open("Data files/StudentRequests.txt", "a+") as f:
            f.writelines(f"{name},{wanted_change},{changed_subject}\n")



def main(running=True):
    items = [
        "User Type",
        "Username",
        "Password",
        "Name",
        "IC",
        "Email",
        "Contact number",
        "Address",
        "Level",
        "Subjects",
        "Month of enrollment",
        "Payment Status",
    ]
    subject_list = subject_schedule.give_subjectlist()
    while running:
        user_data = User.login()
        login_type = User.authenticator(user_data)
        # Admin code block
        if login_type == 0:
            print("Welcome Admin")
            t.sleep(1)

        # Receptionist code block
        elif login_type == 1:
            session = True
            username = user_data[1]
            print(f"Welcome {user_data[3]}.")
            t.sleep(1)
            while session:
                cursor = input(
                    "To register a student, type REG || To update subject enrollment of a student, type ENR || To generate receipts, type REC || To delete a student, type D || To update your profile, type U || To exit, type E || ==> "
                ).upper()
                if cursor == "REG":
                    data_lines = User.line_read()
                    temp = []
                    data = []
                    for i in items:
                        if i == "Username":
                            status = True
                            n = 0
                            while status:
                                new_username = input("Please enter a new username ==> ")

                                if new_username == data_lines[n]:
                                    n += 11
                                    if n == len(data_lines):
                                        print("Username already taken!")
                                        n = 0
                                else:
                                    data.append(new_username)
                                    status = False
                        if (
                            i == "Password"
                            or i == "Name"
                            or i == "IC"
                            or i == "Level"
                            or i == "Contact number"
                            or i == "Month of enrollment"
                        ):
                            new_info = input(f"Please enter {i} ==>")
                            data.append(new_info)
                        if i == "Email":
                            status = True
                            while status:
                                new_email = input("Please enter a valid email ==> ")
                                if "@" not in new_email or ".com" not in new_email:
                                    print("This is not a valid email. Try again")
                                else:
                                    data.append(new_email)
                                    status = False
                        if i == "Address":
                            unit_no = input("Please enter your unit number ==> ")
                            street = input("Please enter your street address ==> ")
                            city = input("Please enter your city ==> ")
                            postcode = input("Please enter your postcode ==> ")
                            state = input("Please enter your state ==> ")
                            address = f"{unit_no}, {street} {city} {postcode}, {state}"
                            data.append(address)
                        if i == "Subjects":
                            n = 1
                            print(
                                "The subjects available are " + ", ".join(subject_list)
                            )
                            while n <= 3:
                                choice = input(f"Please enter subject {n} ==> ").upper()
                                if choice not in subject_list:
                                    print("That's not a valid subject")
                                else:
                                    temp.append(choice)
                                    n += 1
                            data.append(",".join(temp))
                    print(data)
                    Receptionist.register(data)
                    print("User registered.")
                    t.sleep(0.5)
                elif cursor == "D":
                    wanted_user = input(
                        "Enter username of the profile you would like to delete ==> "
                    )
                    confirmation = input("Are you sure? (y/n) ==> ").upper()
                    if confirmation == "Y":
                        wanted_user_data = User.retrieve_info(wanted_user)
                        authentication = User.authenticator(wanted_user_data)
                        print(wanted_user_data, authentication)
                        if authentication == -1:
                            print("User not found.")
                            t.sleep(1)
                            print("Going back...")
                            t.sleep(1)
                        elif authentication < 3:
                            print("You cannot delete Admin, Receptionists and Tutors.")
                        else:
                            Receptionist.delete_student(wanted_user_data)
                            t.sleep(0.5)
                            print("User deleted!")
                            t.sleep(0.5)
                    elif confirmation == "N":
                        print("Going back...")
                        t.sleep(1)
                elif cursor == "U":
                    for i in range(len(user_data)):
                        print(f"|{i+1}| {items[i]}: {user_data[i]}")
                    t.sleep(1)
                    wanted_change_index = int(
                        input("What would you like to edit (2-11)? ==> ")
                    )
                    wanted_change = input("What would like to change it to? ==> ")
                    changer = Receptionist.update_account(
                        wanted_change_index, wanted_change, username
                    )
                    print("Account info changed.")
                    session = False
                elif cursor == "ENR":
                    request_counter = Receptionist.subject_enrollment_changer()
                elif cursor == "E":
                    print("Logging out...")
                    t.sleep(1)
                    print("Logout successfull.")
                    t.sleep(0.5)
                    session = False

        elif login_type == 2:
            session = True
            tutor_lines = Tutor.line_read()[2]
            current_sesh = Tutor.login(tutor_lines)
            user_data = current_sesh[1]
            username = current_sesh[2]
            if current_sesh == -1:
                print("Login failed")
            elif current_sesh[0] == 0:
                print(f"Welcome {user_data[2]}.")
                t.sleep(1)
        # Student code block
        elif login_type == 3:
            session = True
            username = user_data[1]
            print(f"Welcome {user_data[3]}.")
            t.sleep(1)
            while session:
                cursor = input(
                    "To update your profile, type U || To view your schedule, type V || To send a subject change request, type R || To view payment status, type P || To exit, type E ==> "
                ).upper()
                if cursor == "U":
                    for i in range(len(user_data)):
                        print(f"|{i+1}| {items[i]}: {user_data[i]}")
                    t.sleep(1)
                    wanted_change_index = input(
                        "What would you like to edit (2-11)? (Type B to go back) ==> "
                    ).upper()
                    if wanted_change_index == "B":
                        continue
                    elif int(wanted_change_index) == 7:
                        unit_no = input("Please enter your unit number ==> ")
                        street = input("Please enter your street address ==> ")
                        city = input("Please enter your city ==> ")
                        postcode = input("Please enter your postcode ==> ")
                        state = input("Please enter your state ==> ")
                        address = f"{unit_no}, {street} {city} {postcode}, {state}"
                        wanted_change = address
                        changer = Student.update_account(
                            int(wanted_change_index), wanted_change, username
                        )
                        print("Account info changed.")

                        session = False
                    elif int(wanted_change_index) == 9:
                        print(
                            "This can only be done in the 'Request subject change' page."
                        )
                    else:
                        wanted_change = input("What would like to change it to? ==> ")
                        changer = Student.update_account(
                            int(wanted_change_index), wanted_change, username
                        )
                        print("Account info changed.")

                        session = False
                elif cursor == "V":
                    subject_info = user_data[9]
                    student_level = int(user_data[8])
                    while True:
                        day = input(
                            "Please enter what day of your schedule that you would like to see ==> "
                        ).upper()
                        if day not in subject_schedule.give_days():
                            print("Invalid day")
                        else:
                            break
                    for i in subject_info.split(","):
                        print(
                            f"{i} || {','.join(subject_schedule.give_schedule(i, day, student_level)[1:])}"
                        )

                elif cursor == "R":
                    user_subject_info = user_data[9]
                    print(f"Your subjects: {user_subject_info}")
                    while True:
                        wanted_subject = input(
                            "What subject would you like to change ==> "
                        ).upper()
                        if wanted_subject not in user_subject_info:
                            print("You are not enrolled in that subject.")
                        else:
                            break
                    print(f"What subject would you like to change to?")
                    for i in subject_list:
                        print(i)
                    while True:
                        subject_change = input("Your choice ==> ").upper()
                        if subject_change in user_subject_info:
                            print("You have already enrolled in that subject.")
                        else:
                            break
                    print("Your request has been sent!")
                    Student.subject_change_requests(
                        username, wanted_subject, subject_change
                    )
                elif cursor == "E":
                    session = False

        elif login_type == "E":
            print("Exiting system...")
            t.sleep(1)
            running = False


if __name__ == "__main__":
    print("Welcome to Tuition Centre XY")
    main()
