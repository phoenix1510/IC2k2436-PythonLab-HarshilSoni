students = {
    101: {
        "name": "Asha",
        "marks": {
            "Math": 88,
            "Physics": 76,
            "Chem": 92
        }
    },
    102: {
        "name": "Ravi",
        "marks": {
            "Math": 35,
            "Physics": 58,
            "Chem": 64
        }
    },
    103: {
        "name": "Meena",
        "marks": {
            "Math": 72,
            "Physics": 81,
            "Chem": 69
        }
    }
}

def add_student():
    roll = int(input("Enter roll number: "))

    if roll in students:
        print("Student already exists!")
        return

    name = input("Enter name: ")
    marks = {}

    n = int(input("Enter number of subjects: "))

    for i in range(n):
        subject = input("Enter subject: ")
        score = float(input("Enter marks: "))

        if 0 <= score <= 100:
            marks[subject] = score
        else:
            print("Invalid marks!")
            return

    students[roll] = {
        "name": name,
        "marks": marks
    }

    print("Student added successfully!")

def update_marks():
    roll = int(input("Enter roll number: "))

    if roll not in students:
        print("Student not found!")
        return

    subject = input("Enter subject: ")
    score = float(input("Enter new marks: "))

    if 0 <= score <= 100:
        students[roll]["marks"][subject] = score
        print("Marks updated!")
    else:
        print("Invalid marks!")

def delete_student():
    roll = int(input("Enter roll number: "))

    if roll in students:
        del students[roll]
        print("Student deleted!")
    else:
        print("Student not found!")

def show_student():
    roll = int(input("Enter roll number: "))

    if roll in students:
        print(students[roll])
    else:
        print("Student not found!")


def Report():

    averages = {
        roll: round(sum(data["marks"].values()) / len(data["marks"]), 2)
        for roll, data in students.items()
        if data["marks"]
    }

    print("\n--- Student Reports ---")
    print("Averages:", averages)

    if averages:
        topper = max(averages, key=averages.get)
        print("Topper:", students[topper]["name"])
    else:
        print("No marks available!")

    subjects = {}

    for roll, data in students.items():
        for subject, marks in data["marks"].items():

            if subject not in subjects or marks > subjects[subject][1]:
                subjects[subject] = (data["name"], marks)

    print("Highest scorer per subject:", subjects)

    failed = {
        data["name"]: {
            subject: marks
            for subject, marks in data["marks"].items()
            if marks < 40
        }
        for data in students.values()
        if any(marks < 40 for marks in data["marks"].values())
    }

    print("Below 40:", failed)

    grades = {
        "A": [],
        "B": [],
        "C": [],
        "D": [],
        "F": []
    }

    for roll, avg in averages.items():

        name = students[roll]["name"]

        if avg >= 90:
            grades["A"].append(name)
        elif avg >= 75:
            grades["B"].append(name)
        elif avg >= 60:
            grades["C"].append(name)
        elif avg >= 40:
            grades["D"].append(name)
        else:
            grades["F"].append(name)

    print("Grades:", grades)


while True:
    print("\nStudent Database Menu:")
    print("1. Add Student")
    print("2. Update Marks")
    print("3. Delete Student")
    print("4. Show Student")
    print("5. Report")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_student()
    elif choice == '2':
        update_marks()
    elif choice == '3':
        delete_student()
    elif choice == '4':
        show_student()
    elif choice == '5':
        Report()
    elif choice == '6':
        break
    else:
        print("Invalid choice! Please try again.")