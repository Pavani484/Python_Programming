import tkinter as tk
from tkinter import ttk, messagebox

# ------------------ Store ------------------
class Store:
    def __init__(self):
        self.programs = {}          # program_id: {"name":..., "duration":...}
        self.courses = {}           # course_code: {"name":..., "sem":..., "type":..., "program":...}
        self.students = {}          # reg_no: {"name":..., "program_id":..., "sem":...}
        self.hall_tickets = {}      # reg_no: hall_ticket_no
        self.attendance = {}        # hall_ticket: present/absent
        self.marks = {}             # reg_no: {course: marks}
        self.results = {}           # reg_no: {"total":..., "percent":..., "status":...}

store = Store()

# ------------------ Main Application ------------------
class ExamManagementApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Exam Management System – Tkinter")
        self.geometry("1200x720")

        # Header
        header = tk.Frame(self, bg="#4682B4", height=50)
        header.pack(side=tk.TOP, fill=tk.X)
        tk.Label(header, text="Exam Management System", bg="#4682B4", fg="white",
                 font=("Segoe UI", 20, "bold")).pack(padx=10, pady=5, anchor="w")

        # Sidebar
        sidebar = tk.Frame(self, bg="#87CEFA", width=250)
        sidebar.pack(side=tk.LEFT, fill=tk.Y)
        self.pages = {}
        self.current_page = None

        modules = [
            "Program Details", "Course Details", "Student Details",
            "Generate Hall Ticket Nos", "Student–Program Mapping",
            "Student–Course Mapping", "Fee & Application",
            "Exam Time Table", "Generate Hall Tickets",
            "Attendance Sheet", "Decoding", "Marks Entry",
            "Results Generation", "Pass/Fail & Totals"
        ]

        for i, mod in enumerate(modules):
            b = tk.Button(sidebar, text=f"{i+1}. {mod}", bg="#87CEFA", fg="black",
                          font=("Segoe UI", 12), relief="flat",
                          command=lambda m=mod: self.show_page(m))
            b.pack(fill=tk.X, pady=2, padx=5)

        # Content Area
        container = tk.Frame(self)
        container.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Pages
        self.pages["Program Details"] = ProgramDetailsPage(container)
        self.pages["Course Details"] = CourseDetailsPage(container)
        self.pages["Student Details"] = StudentDetailsPage(container)
        self.pages["Generate Hall Ticket Nos"] = HallTicketPage(container, self)
        self.pages["Student–Program Mapping"] = StudentProgramMappingPage(container)
        self.pages["Student–Course Mapping"] = StudentCourseMappingPage(container)
        self.pages["Fee & Application"] = FeePage(container)
        self.pages["Exam Time Table"] = TimeTablePage(container)
        self.pages["Generate Hall Tickets"] = GenerateHallTicketsPage(container)
        self.pages["Attendance Sheet"] = AttendancePage(container)
        self.pages["Decoding"] = DecodingPage(container)
        self.pages["Marks Entry"] = MarksEntryPage(container, self)
        self.pages["Results Generation"] = ResultsGenPage(container, self)
        self.pages["Pass/Fail & Totals"] = SummaryPage(container, self)

