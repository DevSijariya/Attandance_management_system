import datetime

class AttendanceManagementSystem:
    def __init__(college):
        college.users = {
            "Sanskar": "sanskar1234"
        }
        college.students = {}
        college.attendance = {}

    def login(college):
        while True:
            username = input("Username: ")
            password = input("Password: ")
            if username in college.users and college.users[username] == password:
                print("Login successful.")
                break
            else:
                print("Invalid credentials. Please try again.")
    
    def add_student(college, student_id, student_name):
        college.students[student_id] = student_name

    def mark_attendance(college, date, student_id, is_present):
        if date not in college.attendance:
            college.attendance[date] = {}
        college.attendance[date][student_id] = is_present

    def view_student_attendance(college, student_id):
        print(f"Attendance for student {college.students.get(student_id, 'N/A')}:")
        for date, is_present in college.attendance.items():
            if student_id in is_present:
                print(f"{date}: {'Present' if is_present[student_id] else 'Absent'}")

    def generate_report(college, report_type, start_date=None, end_date=None):
        if report_type not in ["daily", "weekly", "monthly"]:
            print("Invalid report type. Available options: daily, weekly, monthly")
            return

        if start_date is None:
            start_date = min(college.attendance.keys())
        if end_date is None:
            end_date = datetime.date.today()

        current_date = start_date
        while current_date <= end_date:
            if current_date in college.attendance:
                present_count = sum(1 for is_present in college.attendance[current_date].values() if is_present)
                total_count = len(college.attendance[current_date])
                print(f"{current_date} - {present_count}/{total_count} students present")

            if report_type == "daily":
                break

            if report_type == "weekly":
                current_date += datetime.timedelta(days=7)
            elif report_type == "monthly":
                next_month = current_date.month % 12 + 1
                next_year = current_date.year + 1 if next_month == 1 else current_date.year
                current_date = current_date.replace(year=next_year, month=next_month, day=1)


def main():
    attendance_system = AttendanceManagementSystem()
    attendance_system.login()

    while True:
        print("\nAttendance Management System Menu:")
        print("1. Add Student")
        print("2. Mark Attendance")
        print("3. View Student Attendance")
        print("4. Generate Attendance Report")
        print("5. Exit")
        choice = int(input("Enter your choice (1-5): "))
        if choice == 1:
            student_id = input("Enter the student ID: ")
            student_name = input("Enter the student name: ")
            attendance_system.add_student(student_id, student_name)
            print(f"Student '{student_name}' with ID '{student_id}' added successfully.")
            
        elif choice == 2:
            date_str = input("Enter the date (YYYY/MM/DD) for attendance marking: ")
            date = datetime.datetime.strptime(date_str, '%Y/%m/%d').date()
            student_id = input("Enter the student ID: ")
            is_present = input("Is the student present? (yes/no): ").lower() == 'yes'
            attendance_system.mark_attendance(date, student_id, is_present)

        elif choice == 3:
            student_id = input("Enter the student ID: ")
            attendance_system.view_student_attendance(student_id)

        elif choice == 4:
            report_type = input("Enter the report type (daily/weekly/monthly): ").lower()
            start_date_str = input("Enter the start date (YYYY/MM/DD): ")
            start_date = datetime.datetime.strptime(start_date_str, '%Y/%m/%d').date()
            end_date_str = input("Enter the end date (YYYY/MM/DD): ")
            end_date = datetime.datetime.strptime(end_date_str, '%Y/%m/%d').date()
            attendance_system.generate_report(report_type, start_date, end_date)

        elif choice == 5:
            print("Exiting Attendance Management System.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()