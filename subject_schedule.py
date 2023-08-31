import json


subject_list = [
    "CHINESE",
    "MALAY",
    "ENGLISH",
    "MATHS",
    "SCIENCE",
    "HISTORY",
    "PHYSICS",
    "CHEMISTRY",
    "BIOLOGY",
]

days = [["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY"]]

subject_prices = {
    "CHINESE": 120,
    "MALAY": 150,
    "ENGLISH": 90,
    "MATHS": 150,
    "SCIENCE": 120,
    "PHYSICS": 180,
    "CHEMISTRY": 180,
    "BIOLOGY": 170,
    "HISTORY": 150,
}

#Gives subject list
def give_subjectlist():
    return subject_list

#Gives the schedule of a specified subject, day and level
def give_schedule(subject: str, day: str, level: int):
    with open("Data files/SubjectSchedules.txt") as f:
        subject_schedule = json.load(f)
    return subject_schedule.get(subject, "Not valid subject").get(day, "Not valid day")[
        level - 1
    ]

#Gives the days that the tuition centre is open
def give_days():
    return ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY"]

#Gives the subject prices
def get_subject_prices():
    return subject_prices

#Gives the whole schedule
def get_whole_schedule():
    with open("Data files/SubjectSchedules.txt") as f:
        subject_schedule = json.load(f)
    return subject_schedule

#Edits the schedule
def edit_schedule(subject_schedule, subject, day, level, start_time, end_time):
    subject_schedule[subject][day][level - 1] = [level, start_time, end_time]
    return subject_schedule

#Saves the changes made to the schedule
def save_schedule(subject_schedule):
    out_file = open("Data files/SubjectSchedules.txt", "w")
    json.dump(subject_schedule, out_file, indent=8)
