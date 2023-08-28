import time as t
import subject_schedule as schedule_manager
from dataclasses import dataclass


# Parent Class
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
            n = 0
            username = input("Please enter your username or type 'E' to exit ==> ")
            if username.upper() == "E":
                data = -1
                return data
            password = input("Please enter your password or type 'E' to exit ==> ")
            if password.upper() == "E":
                data = -1
                return data
            for i, j in enumerate(data):
                if username == j and password == data[i + 1]:
                    print("Logging in...")
                    return data[i - 1 : i + 11]
                else:
                    n += 1
                if i == n - 1:
                    print("Incorrect Username or Password")
                    counter += 1
                    n = 0
                if counter == 3:
                    print("Login attempts reached.")
                    return -1

    def authenticator(data: list):
        if data == -1:
            return -1
        if data[0] == "Admin":
            return 0
        elif data[0] == "Receptionist":
            return 1
        elif data[0] == "Tutor":
            return 2
        elif data[0] == "Student":
            return 3

    # user_type = 0 for admin info, user_type = 1 for Receptionist info, user_type= 2 for tutor info, user_type = 3 for student info
    def retrieve_info(username: list):
        user_info = User.line_read()
        for i, j in enumerate(user_info):
            if j == username:
                try:
                    return user_info[i - 1 : i + 10]
                except IndexError:
                    return user_info[i - 1 :]
            if i + 1 >= len(user_info):
                return -1

    def update_account(wanted_change_index: int, changed_info: str, username: list):
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

    def store_payment(username, balance):
        with open("Data files/StudentPayments.txt", "r+") as f:
            f.write(f"{username},{balance}\n")

    def update_payment_status(user_data: list, status: int):
        new_price = Student.view_payment_info(user_data)
        with open("Data files/StudentPayments.txt", "r+") as f:
            data = list(
                map(str.strip, f.readlines())
            )  # Output: data = [username1, prices1, balance1, username2, prices2, balance2, .......]
            username = [
                x.split(",")[0] for x in data
            ]  # Output: username = [username1, username2 ......]
            prices = [
                int(x.split(",")[1]) for x in data
            ]  # Output: prices = [prices1, prices2 ......]
            balance = [
                int(x.split(",")[2]) for x in data
            ]  # Output: balance = [balance1, balance2 ......]
            for i, j in enumerate(username):
                if j == user_data[1] and status == 1:
                    balance[i] = new_price - prices[i]
                    prices[i] = new_price
                    joiner = [
                        f"{username[x]},{prices[x]},{balance[x]}"
                        for x in range(len(username))
                    ]  # Output: joiner = [username1, prices1, balance1, username2, prices2, balance2, .......]
                elif j == user_data[1] and status == 0:
                    balance[i] = 0
                    prices[i] = new_price
                    joiner = [
                        f"{username[x]},{prices[x]},{balance[x]}"
                        for x in range(len(username))
                    ]
            f.seek(0)
            f.truncate()
            for i in joiner:
                f.write(f"{i}\n")


@dataclass
class Admin(User):
    def register_employee(data: list, role, subjects, prices=None):
        if prices is None:
            prices = 0
        with open("Data files\AllUserData.txt", "a+") as f:
            if role == "Tutor":
                f.write(role)
                for i in range(4):
                    data.append("null")
                data[9] = ",".join(subjects)
                for i in range(len(data)):
                    f.write("\n")
                    f.write(data[i])
                f.write("\n")

            elif role == "Receptionist":
                f.write(role)
                for i in range(len(data)):
                    f.write("\n")
                    f.write(data[i])
                for i in range(4):
                    f.write("\nnull")
                f.write("\n")

    def delete_user(user_data: list):
        with open("Data files/AllUserData.txt", "r+") as cursor:
            data_lines = User.line_read()
            cursor.seek(0)
            cursor.truncate()
            data_lines.pop(data_lines.index(user_data[1]) - 1)
            for i, j in enumerate(data_lines):
                if j == user_data[1]:
                    for x in range(11):
                        data_lines.pop(i)
            for i in data_lines:
                cursor.write(f"{i}\n")

    def monthly_report_generator(price=None):
        if price is None:
            price = 0
        total_price = {}
        data = Admin.line_read()
        for i, j in enumerate(data):
            if j == "Student":
                user_data = data[i : i + 12]
                subjects = user_data[9].split(",")
                subject_prices = schedule_manager.get_subject_prices()
                for x in subjects:
                    if x not in total_price:
                        total_price[x] = subject_prices[x]
                    else:
                        total_price[x] += subject_prices[x]
                    price += subject_prices[x]
        return total_price, price


@dataclass
class Receptionist(User):
    # Registers new students
    def register(data: list, prices=None):
        if prices is None:
            prices = 0
        with open("Data files\AllUserData.txt", "a+") as student:
            student.write("Student")
            for i in range(len(data)):
                student.write("\n")
                student.write(data[i])
            student.write("\nPaid")
        subject_prices = schedule_manager.get_subject_prices()
        subjects = data[8].split(",")
        for i in subjects:
            prices += subject_prices[i]
        with open("Data files\StudentPayments.txt", "a+") as f:
            f.write(f"{data[0]},{prices},0\n")

    def delete_requests(user_choice: str, subject_list: list):
        with open("Data files/StudentRequests.txt", "r+") as cursor:
            requests = list(map(str.strip, cursor.readlines()))
            subject_change_info = f"{user_choice},{','.join(subject_list[1:])}"
            cursor.seek(0)
            cursor.truncate()
            for j in requests:
                if j != subject_change_info:
                    cursor.writelines(f"{j}\n")

    def subject_enrollment_changer(running=True, choosing=True):
        while running:
            with open("Data files/StudentRequests.txt", "r") as f:
                changing_user = []
                student_request_data = list(map(str.strip, f.readlines()))
                data = [x.split(",") for x in student_request_data]
                names = [x[0] for x in data]
                subjects = [x[1:] for x in data]
            print(f"Total number of pending requests: {len(subjects)}")
            print(f"Pending requests from: {', '.join(set(names))}")
            while choosing:
                user_choice = input(
                    "Enter the user to check on their requests (Type E to exit) ==> "
                )
                if user_choice.upper() == "E":
                    running = False
                    choosing = False
                elif user_choice in names:
                    for i in data:
                        if i[0] == user_choice:
                            changing_user.append(i)
                    wanted_student_data = User.retrieve_info(user_choice)
                    for i in range(len(changing_user)):
                        print(
                            f"{user_choice} would like to change their enrollment of {changing_user[i][1]} to {changing_user[i][2]} ({i+1})."
                        )
                    selection = (
                        int(
                            input(
                                "Select which request you would like to select (Type 0 to exit) ==> "
                            )
                        )
                        - 1
                    )
                    if selection == 0:
                        running = False
                        choosing = False

                    subject_list = changing_user[selection]
                    approval = input(
                        "Do you want to approve this request? (Y/N) ==> "
                    ).upper()
                    if approval == "N":
                        Receptionist.delete_requests(
                            user_choice,
                            subject_list,
                        )
                        print("Request deleted.")
                        changing_user = []
                    elif approval == "Y":
                        old_student_subjects = wanted_student_data[9].split(",")
                        for index, subject in enumerate(old_student_subjects):
                            if subject == subject_list[1]:
                                old_student_subjects[index] = subject_list[2]
                        wanted_student_data[9] = ",".join(old_student_subjects)
                        User.update_account(
                            10, ",".join(old_student_subjects), wanted_student_data[1]
                        )
                        print("Subject changed.")
                        Receptionist.delete_requests(user_choice, subject_list)
                        User.update_payment_status(
                            wanted_student_data, 1
                        )  # 1 for adding new balance
                        print("Request deleted.")
                        changing_user = []
                else:
                    print("Invalid user")

    # Deletes the desired student's info
    def delete_student(user_data: list):
        with open("Data files/AllUserData.txt", "r+") as cursor:
            data_lines = User.line_read()
            cursor.seek(0)
            cursor.truncate()
            data_lines.pop(data_lines.index(user_data[1]) - 1)
            for i in user_data[1:]:
                data_lines.pop(data_lines.index(i))
            for i in data_lines:
                cursor.write(f"{i}\n")

    def update_payment_status(username: str, user_info: list):
        User.update_account(12, "Paid", username)
        print("Payment received")
        Receptionist.receipt_generator(user_info)

    def receipt_generator(user_info: list):
        subject_price = schedule_manager.get_subject_prices()
        user_subjects = user_info[9].split(",")
        payment = [subject_price[x] for x in user_subjects]
        print(f"Receipt for {user_info[1]}")
        print("-------------------------------------")
        for i in range(3):
            print(f"{list(subject_price.keys())[i]}: {payment[i]}")
        print("-------------------------------------")
        print(f"Total paid amount: {sum(payment)}\n")


@dataclass
class Tutor(User):
    def check_schedules():
        pass

    def edit_schedule(subject_schedule, subject, day, level, start_time, end_time):
        edited_schedule = schedule_manager.edit_schedule(
            subject_schedule, subject, day, level, start_time, end_time
        )
        schedule_manager.save_schedule(edited_schedule)


@dataclass
class Student(User):
    def subject_change_requests(name: str, wanted_change: str, changed_subject: str):
        with open("Data files/StudentRequests.txt", "a+") as f:
            f.writelines(f"{name},{wanted_change},{changed_subject}\n")

    def view_payment_info(user_data: list, prices=None):
        if prices is None:
            prices = 0
        subject_prices = schedule_manager.get_subject_prices()
        for i in user_data[9].split(","):
            prices += int(subject_prices[i])
        return prices

    def check_payment_status(user_info: list):
        payment_status = user_info[-1]
        if payment_status == "Paid":
            print("You have already paid!")
        elif payment_status == "Unpaid":
            with open("Data files/StudentPayments.txt", "r") as f:
                data = list(map(str.strip, f.readlines()))
                username = [x.split(",")[0] for x in data]
                prices = [int(x.split(",")[1]) for x in data]
                balance = [int(x.split(",")[2]) for x in data]
                for i, j in enumerate(username):
                    if j == user_info[1]:
                        if balance[i] != 0:
                            choice = input(
                                f"Type P to pay the amount of: RM{balance[i]} or type C to cancel ==> "
                            ).upper()
                            if choice == "P":
                                print("Paying...")
                                User.update_payment_status(
                                    user_info[1], 0
                                )  # 0 for resetting balance value
                                Receptionist.update_payment_status(
                                    user_info[1], user_info
                                )
                        else:
                            balance = Student.view_payment_info(user_info)
                            choice = input(
                                f"Type P to pay the amount of: RM{balance} or type C to cancel ==> "
                            ).upper()
                            if choice == "P":
                                print("Paying...")
                                User.store_payment(user_info[1], balance)
                                Receptionist.update_payment_status(
                                    user_info[1], user_info
                                )

    def view_schedule(subject_info, student_level, running=True):
        while running:
            day = input(
                "Please enter what day of your schedule that you would like to see ==> "
            ).upper()
            if day not in schedule_manager.give_days():
                print("Invalid day")
            else:
                running = False
            for i in subject_info.split(","):
                print(
                    f"{i} || {','.join(schedule_manager.give_schedule(i, day, student_level)[1:])}"
                )


def admin(user_data: list, items: list, subject_list: list):
    session = True
    username = user_data[1]
    print("Welcome Admin")
    t.sleep(1)
    while session:
        cursor = input(
            "To update your profile, type U || To register employees, type REG || To remove employees, type D || To view monthly income report, type V || To exit, type E ==> "
        ).upper()
        if cursor == "U":
            for i in range(len(user_data)):
                print(f"|{i+1}| {items[i]}: {user_data[i]}")
            t.sleep(1)
            wanted_change_index = int(input("What would you like to edit (2-11)? ==> "))
            wanted_change = input("What would like to change it to? ==> ")
            changer = Receptionist.update_account(
                wanted_change_index, wanted_change, username
            )
            print("Account info changed.")
            session = False
        elif cursor == "REG":
            registering = input(
                "Type R to register Receptionist, type T to register Tutor ==> "
            ).upper()
            if registering == "T":
                role = "Tutor"
                data_lines = User.line_read()
                subject = []
                temp = []
                data = []
                for i in items:
                    if i == "Username":
                        status = True
                        n = 1
                        while status:
                            new_username = input("Please enter a new username ==> ")
                            for x in data_lines:
                                if x == new_username:
                                    print("Username taken")
                            if len(new_username) < 8:
                                print(
                                    "The username length must be more than 8 characters."
                                )
                            else:
                                data.append(new_username)
                                status = False
                    if (
                        i == "Password"
                        or i == "Name"
                        or i == "IC"
                        or i == "Contact number"
                    ):
                        new_info = input(f"Please enter your {i} ==>")
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
                        print("What are the subjects tutor will be teaching? ==> ")
                        print(f"Subjects: {', '.join(subject_list)}")
                        while n <= 3:
                            choice = input(f"Please enter subject {n} ==> ").upper()
                            if choice not in subject_list:
                                print("That's not a valid subject")
                            else:
                                temp.append(choice)
                                n += 1
                        subject.append(",".join(temp))
                print(data)
                Admin.register_employee(data, role, subject)
                print("User registered.")
                t.sleep(0.5)
            elif registering == "R":
                role = "Receptionist"
                data_lines = User.line_read()
                subject = []
                temp = []
                data = []
                for i in items:
                    if i == "Username":
                        status = True
                        n = 1
                        while status:
                            new_username = input("Please enter a new username ==> ")
                            for x in data_lines:
                                if x == new_username:
                                    print("Username taken")
                            if len(new_username) < 8:
                                print(
                                    "The username length must be more than 8 characters."
                                )
                            else:
                                data.append(new_username)
                                status = False
                    if (
                        i == "Password"
                        or i == "Name"
                        or i == "IC"
                        or i == "Contact number"
                    ):
                        new_info = input(f"Please enter your {i} ==>")
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
                    subject = []
                print(data)
                Admin.register_employee(data, role, subject)
                print("User registered.")
                t.sleep(0.5)

        elif cursor == "D":
            wanted_user = input(
                "Enter username of the user you would like to delete ==> "
            )
            confirmation = input("Are you sure? (y/n) ==> ").upper()
            if confirmation == "Y":
                wanted_user_data = User.retrieve_info(wanted_user)
                authentication = User.authenticator(wanted_user_data)
                if authentication == -1:
                    print("User not found.")
                    t.sleep(1)
                    print("Going back...")
                    t.sleep(1)
                else:
                    Admin.delete_user(wanted_user_data)
                    t.sleep(0.5)
                    print("User deleted!")
                    t.sleep(0.5)
            elif confirmation == "N":
                print("Going back...")
                t.sleep(1)
        elif cursor == "V":
            report = Admin.monthly_report_generator()
            print(f"Monthly income: {report[1]}")
            print("------------------------------")
            print(f"Income based on subjects: ")
            for i in report[0]:
                print(f"{i}: {report[0][i]}")

        elif cursor == "E":
            print("Logging out....")
            print("Logout successfull")
            session = False


def receptionist(user_data: list, items: list, subject_list: list):
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
                    n = 1
                    while status:
                        new_username = input("Please enter a new username ==> ")
                        for x in data_lines:
                            if x == new_username:
                                print("Username taken")
                        if len(new_username) < 8:
                            print("The username length must be more than 8 characters.")
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
                    print("The subjects available are " + ", ".join(subject_list))
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
            wanted_change_index = int(input("What would you like to edit (2-11)? ==> "))
            wanted_change = input("What would like to change it to? ==> ")
            changer = Receptionist.update_account(
                wanted_change_index, wanted_change, username
            )
            print("Account info changed.")
            session = False
        elif cursor == "ENR":
            request_counter = Receptionist.subject_enrollment_changer()
        elif cursor == "REC":
            data = User.line_read()
            for i, j in enumerate(data):
                if j == "Student" and data[i + 11] == "Paid":
                    Receptionist.receipt_generator(data[i : i + 12])
        elif cursor == "E":
            print("Logging out...")
            t.sleep(1)
            print("Logout successfull.")
            t.sleep(0.5)
            session = False


def tutor(user_data: list, items: list, subject_list: list):
    session = True
    username = user_data[1]
    print(f"Welcome {user_data[3]}.")
    t.sleep(1)
    while session:
        cursor = input("To change your current schedule, type C").upper()
        if cursor == "C":
            valid = True
            subjects = list(map(str.strip, user_data[9].split(",")))
            days = schedule_manager.give_days()
            level = list(x for x in range(1, 6))
            print(f"Subjects you are teaching:")
            for i in subjects:
                print(f"{i}")
            while valid:
                chosen_subject = input(
                    "Select which subject you would like to check ==> "
                ).upper()
                if chosen_subject not in subjects:
                    print("Invalid subject")
                else:
                    break
            while valid:
                chosen_day = input(
                    "Select which day's schedule you would like to see ==> "
                ).upper()
                if chosen_day not in days:
                    print("Invalid day")
                else:
                    break
            while valid:
                chosen_level = int(input("Enter the level of students ==> "))
                if chosen_level not in level:
                    print("Invalid level")
                else:
                    valid = False
            tutor_subjects = schedule_manager.give_schedule(
                chosen_subject, chosen_day, chosen_level
            )
            print(
                f"Subject: {chosen_subject}\nLevel: Form {tutor_subjects[0]}\nStart time: {tutor_subjects[1]}\nEnd time: {tutor_subjects[2]}"
            )


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
    subject_list = schedule_manager.give_subjectlist()
    while running:
        user_data = User.login()
        login_type = User.authenticator(user_data)
        # Admin code block
        if login_type == 0:
            admin(user_data, items, subject_list)

        # Receptionist code block
        elif login_type == 1:
            receptionist(user_data, items, subject_list)

        elif login_type == 2:
            tutor(user_data, items, subject_list)

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
                    Student.view_schedule(subject_info, student_level)

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
                elif cursor == "P":
                    Student.check_payment_status(user_data)
                elif cursor == "E":
                    session = False

        elif login_type == -1:
            print("Exiting system...")
            t.sleep(1)
            running = False


if __name__ == "__main__":
    print("Welcome to Tuition Centre XY")
    main()
