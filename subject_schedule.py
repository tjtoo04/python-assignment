import json

# Subject: [Day(0-4), [level, start, end], repeat]
subject_list = [
    "CHINESE",
    "MALAY",
    "ENGLISH",
    "MATHS",
    "SCIENCE",
    "PHYSICS",
    "CHEMISTRY",
    "HISTORY",
    "BIOLOGY",
]
days = [["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY"]]

"""subject_schedule = {
    "CHINESE": {
        "MONDAY": [
            [1, "1330", "1430"],
            [2, "1000", "1100"],
            [3, "1130", "1230"],
            [4, "1800", "1900"],
            [5, "1500", "1600"],
        ],
        "TUESDAY": [
            [1, "2000", "2100"],
            [2, "1600", "1700"],
            [3, "1030", "1230"],
            [4, "1730", "1930"],
            [5, "1330", "1530"],
        ],
        "WEDNESDAY": [
            [1, "1330", "1430"],
            [2, "1000", "1100"],
            [3, "1130", "1230"],
            [4, "1800", "1900"],
            [5, "1500", "1600"],
        ],
        "THURSDAY": [
            [1, "2000", "2100"],
            [2, "1600", "1700"],
            [3, "1030", "1230"],
            [4, "1730", "1930"],
            [5, "1330", "1530"],
        ],
        "FRIDAY": [
            [1, "1330", "1430"],
            [2, "1000", "1100"],
            [3, "1130", "1230"],
            [4, "1800", "1900"],
            [5, "1500", "1630"],
        ],
    },
    "MALAY": {
        "MONDAY": [
            [1, "1000", "1100"],
            [2, "1230", "1330"],
            [3, "1400", "1500"],
            [4, "1600", "1700"],
            [5, "1800", "1900"],
        ],
        "TUESDAY": [
            [1, "1030", "1130"],
            [2, "1230", "1330"],
            [3, "1430", "1530"],
            [4, "1630", "1730"],
            [5, "1830", "1930"],
        ],
        "WEDNESDAY": [
            [1, "1000", "1100"],
            [2, "1230", "1330"],
            [3, "1400", "1500"],
            [4, "1600", "1700"],
            [5, "1800", "1900"],
        ],
        "THURSDAY": [
            [1, "1030", "1130"],
            [2, "1230", "1330"],
            [3, "1430", "1530"],
            [4, "1630", "1730"],
            [5, "1830", "1930"],
        ],
        "FRIDAY": [
            [1, "1000", "1100"],
            [2, "1230", "1330"],
            [3, "1400", "1500"],
            [4, "1600", "1700"],
            [5, "1800", "1900"],
        ],
    },
    "ENGLISH": {
        "MONDAY": [
            [1, 1500, 1600],
            [2, 1000, 1100],
            [3, 1330, 1430],
            [4, 1130, 1230],
            [5, 1700, 1800],
        ],
        "TUESDAY": [
            [1, 1030, 1130],
            [2, 1200, 1300],
            [3, 1400, 1500],
            [4, 1530, 1630],
            [5, 1700, 1800],
        ],
        "WEDNESDAY": [
            [1, 1500, 1600],
            [2, 1000, 1100],
            [3, 1330, 1430],
            [4, 1130, 1230],
            [5, 1700, 1800],
        ],
        "THURSDAY": [
            ["1", 1030, 1130],
            [2, 1200, 1300],
            [3, 1400, 1500],
            [4, 1530, 1630],
            [5, 1700, 1800],
        ],
        "FRIDAY": [
            [1, 1500, 1600],
            [2, 1000, 1100],
            [3, 1330, 1430],
            [4, 1130, 1230],
            [5, 1700, 1800],
        ],
    },
    "MATHS": {
        "MONDAY": [
            [1, "1000", "1100"],
            [2, "1130", "1230"],
            [3, "1330", "1430"],
            [4, "1500", "1600"],
            [5, "1630", "1730"],
        ],
        "TUESDAY": [
            [1, "1500", "1600"],
            [2, "1430", "1530"],
            [3, "1000", "1100"],
            [4, "1130", "1230"],
            [5, "1630", "1730"],
        ],
        "WEDNESDAY": [
            [1, "1000", "1100"],
            [2, "1130", "1230"],
            [3, "1330", "1430"],
            [4, "1500", "1600"],
            [5, "1630", "1730"],
        ],
        "THURSDAY": [
            [1, "1500", "1600"],
            [2, "1430", "1530"],
            [3, "1000", "1100"],
            [4, "1130", "1230"],
            [5, "1630", "1730"],
        ],
        "FRIDAY": [
            [1, "1000", "1100"],
            [2, "1130", "1230"],
            [3, "1330", "1430"],
            [4, "1500", "1600"],
            [5, "1630", "1730"],
        ],
    },
    "SCIENCE": [[[]]],
    "PHYSICS": [[[]]],
    "CHEMISTRY": [[[]]],
    "BIOLOGY": [[[]]],
    "HISTORY": [[[]]],
}"""

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


def give_subjectlist():
    return subject_list


def give_schedule(subject: str, day: str, level: int):
    with open("Data files/SubjectSchedules.txt") as f:
        subject_schedule = json.load(f)
    return subject_schedule.get(subject, "Not valid subject").get(day, "Not valid day")[
        level - 1
    ]


def give_days():
    return ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY"]


def get_subject_prices():
    return subject_prices


def edit_schedule(subject_schedule, subject, day, level, start_time, end_time):
    subject_schedule[subject][day][level - 1] = [level, start_time, end_time]
    return subject_schedule


def save_schedule(subject_schedule):
    out_file = open("Data files/SubjectSchedules.txt", "w")
    json.dump(subject_schedule, out_file, indent=8)
