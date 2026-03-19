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
