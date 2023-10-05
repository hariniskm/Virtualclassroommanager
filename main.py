class Classroom:
    def __init__(self, name):
        self.name = name
        self.students = {}
        self.assignments = {}

    def add_student(self, student):
        self.students[student.get_id()] = student

    def schedule_assignment(self, assignment_name, details):
        self.assignments[assignment_name] = Assignment(assignment_name, details)

    def list_students(self):
        print(f"Students in Classroom {self.name}:")
        for student_id in self.students.keys():
            print(f"Student ID: {student_id}")

    def list_assignments(self):
        print(f"Assignments in Classroom {self.name}:")
        for assignment_name, assignment in self.assignments.items():
            print(f"Assignment Name: {assignment_name}")
            print(f"Assignment Details: {assignment.get_details()}")

    def get_name(self):
        return self.name


class Student:
    def __init__(self, student_id, classroom):
        self.student_id = student_id
        self.classroom = classroom

    def get_id(self):
        return self.student_id

    def get_classroom(self):
        return self.classroom


class Assignment:
    def __init__(self, name, details):
        self.name = name
        self.details = details

    def get_name(self):
        return self.name

    def get_details(self):
        return self.details


class VirtualClassroomManager:
    classrooms = {}
    students = {}

    @staticmethod
    def main():
        print("Virtual Classroom Manager is running...")

        while True:
            user_input = input("Enter a command: ")
            command = user_input.split()

            if len(command) < 2:
                print("Invalid command. Please provide more details.")
                continue

            action = command[0].lower()
            class_name = command[1]

            if action == "add_classroom":
                VirtualClassroomManager.add_classroom(class_name)
            elif action == "add_student":
                if len(command) < 3:
                    print("Invalid command. Please provide student ID.")
                    continue
                student_id = command[2]
                VirtualClassroomManager.add_student(class_name, student_id)
            elif action == "schedule_assignment":
                if len(command) < 3:
                    print("Invalid command. Please provide assignment details.")
                    continue
                assignment_details = " ".join(command[2:])
                VirtualClassroomManager.schedule_assignment(class_name, assignment_details)
            elif action == "submit_assignment":
                if len(command) < 3:
                    print("Invalid command. Please provide student ID.")
                    continue
                student_id = command[2]
                VirtualClassroomManager.submit_assignment(class_name, student_id)
            elif action == "list_students":
                VirtualClassroomManager.list_students(class_name)
            elif action == "list_assignments":
                list_assignments(class_name)
            elif action == "remove_classroom":  # Added command to remove a classroom
                VirtualClassroomManager.remove_classroom(class_name)
            else:
                print("Invalid command.")

    @staticmethod
    def add_classroom(class_name):
        if class_name not in VirtualClassroomManager.classrooms:
            VirtualClassroomManager.classrooms[class_name] = Classroom(class_name)
            print(f"Classroom {class_name} has been created.")
        else:
            print(f"Classroom {class_name} already exists.")

    @staticmethod
    def add_student(class_name, student_id):
        if class_name in VirtualClassroomManager.classrooms:
            classroom = VirtualClassroomManager.classrooms[class_name]
            if student_id not in VirtualClassroomManager.students:
                student = Student(student_id, classroom)
                VirtualClassroomManager.students[student_id] = student
                classroom.add_student(student)
                print(f"Student {student_id} has been enrolled in {class_name}.")
            else:
                print(f"Student {student_id} is already enrolled in a classroom.")
        else:
            print(f"Classroom {class_name} not found.")

    @staticmethod
    def schedule_assignment(class_name, assignment_details):
        if class_name in VirtualClassroomManager.classrooms:
            classroom = VirtualClassroomManager.classrooms[class_name]
            assignment_name = f"Assignment {len(classroom.assignments) + 1}"
            classroom.schedule_assignment(assignment_name, assignment_details)
            print(f"Assignment for {class_name} has been scheduled.")
        else:
            print(f"Classroom {class_name} not found.")

    @staticmethod
    def remove_classroom(class_name):
        if class_name in VirtualClassroomManager.classrooms:
            del VirtualClassroomManager.classrooms[class_name]
            print(f"Classroom {class_name} has been removed.")
        else:
            print(f"Classroom {class_name} not found.")

    @staticmethod
    def submit_assignment(class_name, student_id):
        if class_name in VirtualClassroomManager.classrooms and student_id in VirtualClassroomManager.students:
            classroom = VirtualClassroomManager.classrooms[class_name]
            print(f"Assignment submitted by Student {student_id} in {class_name}.")
        else:
            print(f"Classroom {class_name} or Student with ID {student_id} not found.")

    @staticmethod
    def list_students(class_name):
        if class_name in VirtualClassroomManager.classrooms:
            VirtualClassroomManager.classrooms[class_name].list_students()
        else:
            print(f"Classroom {class_name} not found.")


def list_assignments(class_name):
    if class_name in VirtualClassroomManager.classrooms:
        VirtualClassroomManager.classrooms[class_name].list_assignments()
    else:
        print(f"Classroom {class_name} not found.")


if __name__ == "__main__":
    VirtualClassroomManager.main()
