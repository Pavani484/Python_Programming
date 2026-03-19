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

        for page in self.pages.values():
            page.place(relx=0, rely=0, relwidth=1, relheight=1)

        self.show_page("Program Details")

    def show_page(self, name):
        if self.current_page:
            self.current_page.lower()
        page = self.pages[name]
        page.lift()
        self.current_page = page

# ------------------ Program Details Page ------------------
class ProgramDetailsPage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="white")
        form = tk.Frame(self, bg="white")
        form.pack(pady=10)
        tk.Label(form, text="Program ID").grid(row=0, column=0, padx=5)
        self.pid = tk.Entry(form); self.pid.grid(row=0, column=1, padx=5)
        tk.Label(form, text="Name").grid(row=0, column=2, padx=5)
        self.name = tk.Entry(form); self.name.grid(row=0, column=3, padx=5)
        tk.Label(form, text="Duration (Years)").grid(row=0, column=4, padx=5)
        self.duration = tk.Spinbox(form, from_=1, to=6); self.duration.grid(row=0, column=5, padx=5)
        tk.Button(form, text="Add Program", bg="#4CAF50", fg="white", command=self.add_program).grid(row=0,column=6,padx=5)
        tk.Button(form, text="Clear", bg="#E74C3C", fg="white", command=self.clear).grid(row=0,column=7,padx=5)

        self.tree = ttk.Treeview(self, columns=("ID","Name","Duration"), show="headings")
        self.tree.heading("ID", text="Program ID")
        self.tree.heading("Name", text="Program Name")
        self.tree.heading("Duration", text="Duration")
        self.tree.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

    def add_program(self):
        pid = self.pid.get().strip()
        name = self.name.get().strip()
        dur = self.duration.get().strip()
        if not pid or not name:
            messagebox.showwarning("Input Error","Enter ID & Name")
            return
        store.programs[pid] = {"name":name,"duration":dur}
        self.tree.insert("",tk.END,values=(pid,name,dur))
        self.clear_inputs()

    def clear_inputs(self):
        self.pid.delete(0,tk.END)
        self.name.delete(0,tk.END)
        self.duration.delete(0,tk.END)
        self.duration.insert(0,"3")

    def clear(self):
        store.programs.clear()
        for item in self.tree.get_children():
            self.tree.delete(item)

# ------------------ Course Details Page ------------------
class CourseDetailsPage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="white")
        form = tk.Frame(self, bg="white")
        form.pack(pady=10)
        tk.Label(form, text="Code").grid(row=0,column=0,padx=5)
        self.code = tk.Entry(form); self.code.grid(row=0,column=1,padx=5)
        tk.Label(form, text="Name").grid(row=0,column=2,padx=5)
        self.name = tk.Entry(form); self.name.grid(row=0,column=3,padx=5)
        tk.Label(form, text="Semester").grid(row=0,column=4,padx=5)
        self.sem = tk.Spinbox(form, from_=1,to=12); self.sem.grid(row=0,column=5,padx=5)
        tk.Label(form, text="Program").grid(row=0,column=6,padx=5)
        self.program = ttk.Combobox(form, values=list(store.programs.keys())); self.program.grid(row=0,column=7,padx=5)
        tk.Label(form, text="Type").grid(row=0,column=8,padx=5)
        self.type = ttk.Combobox(form, values=["Common","Program Oriented"]); self.type.grid(row=0,column=9,padx=5)
        self.type.current(0)
        tk.Button(form,text="Add Course",bg="#4CAF50",fg="white",command=self.add_course).grid(row=0,column=10,padx=5)
        tk.Button(form,text="Clear",bg="#E74C3C",fg="white",command=self.clear).grid(row=0,column=11,padx=5)

        self.tree = ttk.Treeview(self, columns=("Code","Name","Sem","Program","Type"), show="headings")
        self.tree.heading("Code", text="Code")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Sem", text="Semester")
        self.tree.heading("Program", text="Program")
        self.tree.heading("Type", text="Type")
        self.tree.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

    def add_course(self):
        c = self.code.get().strip()
        n = self.name.get().strip()
        s = self.sem.get().strip()
        p = self.program.get().strip()
        t = self.type.get()
        if not c or not n or not p:
            messagebox.showwarning("Input Error","Enter Code, Name & Program")
            return
        store.courses[c] = {"name":n,"sem":s,"type":t,"program":p}
        self.tree.insert("",tk.END,values=(c,n,s,p,t))
        self.clear_inputs()

    def clear_inputs(self):
        self.code.delete(0,tk.END)
        self.name.delete(0,tk.END)
        self.sem.delete(0,tk.END)
        self.sem.insert(0,"1")
        self.program['values'] = list(store.programs.keys())
        self.type.current(0)

    def clear(self):
        store.courses.clear()
        for item in self.tree.get_children():
            self.tree.delete(item)

# ------------------ Student Details Page ------------------
class StudentDetailsPage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="white")
        form = tk.Frame(self, bg="white")
        form.pack(pady=10)
        tk.Label(form, text="Reg No").grid(row=0,column=0,padx=5)
        self.reg = tk.Entry(form); self.reg.grid(row=0,column=1,padx=5)
        tk.Label(form, text="Name").grid(row=0,column=2,padx=5)
        self.name = tk.Entry(form); self.name.grid(row=0,column=3,padx=5)
        tk.Label(form, text="Program").grid(row=0,column=4,padx=5)
        self.program = ttk.Combobox(form, values=list(store.programs.keys())); self.program.grid(row=0,column=5,padx=5)
        tk.Label(form, text="Sem").grid(row=0,column=6,padx=5)
        self.sem = tk.Spinbox(form, from_=1,to=12); self.sem.grid(row=0,column=7,padx=5)
        tk.Button(form,text="Add Student",bg="#4CAF50",fg="white",command=self.add_student).grid(row=0,column=8,padx=5)
        tk.Button(form,text="Clear",bg="#E74C3C",fg="white",command=self.clear).grid(row=0,column=9,padx=5)

        self.tree = ttk.Treeview(self, columns=("Reg","Name","Program","Sem"), show="headings")
        self.tree.heading("Reg", text="Reg No")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Program", text="Program")
        self.tree.heading("Sem", text="Semester")
        self.tree.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

    def add_student(self):
        r = self.reg.get().strip()
        n = self.name.get().strip()
        p = self.program.get().strip()
        s = self.sem.get().strip()
        if not r or not n or not p:
            messagebox.showwarning("Input Error","Enter RegNo, Name & Program")
            return
        store.students[r] = {"name":n,"program_id":p,"sem":s}
        self.tree.insert("",tk.END,values=(r,n,p,s))
        self.clear_inputs()

    def clear_inputs(self):
        self.reg.delete(0,tk.END)
        self.name.delete(0,tk.END)
        self.sem.delete(0,tk.END)
        self.sem.insert(0,"1")
        self.program['values'] = list(store.programs.keys())

    def clear(self):
        store.students.clear()
        for item in self.tree.get_children():
            self.tree.delete(item)

# ------------------ Hall Ticket Page ------------------
class HallTicketPage(tk.Frame):
    def __init__(self, parent, app):
        super().__init__(parent, bg="white")
        tk.Label(self, text="Generate Hall Ticket Numbers", font=("Arial", 14), bg="white").pack(pady=10)
        tk.Button(self, text="Generate", bg="#4CAF50", fg="white", command=self.generate).pack(pady=5)
        self.text = tk.Text(self, height=25); self.text.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

    def generate(self):
        self.text.delete("1.0", tk.END)
        for i,(reg, st) in enumerate(store.students.items(), start=1):
            ht = f"HT{1000+i}"
            store.hall_tickets[reg] = ht
            self.text.insert(tk.END, f"{reg} – {st['name']} : {ht}\n")
        messagebox.showinfo("Done","Hall ticket numbers generated")

# ------------------ Student–Program Mapping Page ------------------
class StudentProgramMappingPage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="white")
        tk.Label(self, text="Student–Program Mapping", font=("Arial", 14), bg="white").pack(pady=10)
        self.text = tk.Text(self, height=25); self.text.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        tk.Button(self, text="Show Mapping", bg="#4682B4", fg="white", command=self.show).pack(pady=5)

    def show(self):
        self.text.delete("1.0", tk.END)
        for r,s in store.students.items():
            p = store.programs.get(s["program_id"],{}).get("name","-")
            self.text.insert(tk.END, f"{r} – {s['name']} : Program {s['program_id']} ({p})\n")

# ------------------ Student–Course Mapping Page ------------------
class StudentCourseMappingPage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="white")
        tk.Label(self, text="Student–Course Mapping", font=("Arial", 14), bg="white").pack(pady=10)
        self.text = tk.Text(self, height=25); self.text.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        tk.Button(self, text="Show Mapping", bg="#4682B4", fg="white", command=self.show).pack(pady=5)

    def show(self):
        self.text.delete("1.0", tk.END)
        for r,s in store.students.items():
            courses = [c for c,info in store.courses.items()
                       if info["program"]==s["program_id"] and info["sem"]==s["sem"]]
            self.text.insert(tk.END, f"{r} – {s['name']} : {', '.join(courses) if courses else 'No Courses'}\n")

# ------------------ Fee Page ------------------
class FeePage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="white")
        tk.Label(self, text="Fee & Application", font=("Arial", 14), bg="white").pack(pady=10)
        self.text = tk.Text(self, height=25); self.text.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        tk.Button(self, text="Generate Fee Status", bg="#4682B4", fg="white", command=self.generate).pack(pady=5)

    def generate(self):
        self.text.delete("1.0", tk.END)
        for r,s in store.students.items():
            self.text.insert(tk.END, f"{r} – {s['name']} : Fee Paid\n")

# ------------------ Exam Time Table Page ------------------
