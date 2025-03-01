import tkinter as tk
from tkinter import ttk

from views.main_window import MainWindow
from views.step1_frame import Step1Frame
from views.step2_frame import Step2Frame
from views.step3_frame import Step3Frame
from views.step4_frame import Step4Frame
from models.math_equations import MathEquations
from utils.styles import BACKGROUND_COLOR, update_button_state, BUTTON_BG_COLOR

class NetIntelApp:    
    def __init__(self, root):
        self.root = root
        self.current_step = 0
        
        
        self.root.configure(bg=BACKGROUND_COLOR)
        
        
        self.source_count = 0
        self.time_limit = 0
        self.transition_probability_grid_initiated = False
        self.source_data_grid_initiated = False
        
        
        self.P = []  
        self.pj = []  
        self.Fs = []  
        self.Ff = []  
        self.Ks = []  
        self.Kf = []  
        
        
        self.main_window = MainWindow(root, self)
        
        
        self.step1_frame = Step1Frame(self.main_window.container, self)
        self.step2_frame = Step2Frame(self.main_window.container, self)
        self.step3_frame = Step3Frame(self.main_window.container, self)
        self.step4_frame = Step4Frame(self.main_window.container, self)
        
        
        self.step1_frame.place(relwidth=1, relheight=1)
        self.step2_frame.place(relwidth=1, relheight=1)
        self.step3_frame.place(relwidth=1, relheight=1)
        self.step4_frame.place(relwidth=1, relheight=1)
        
        
        self.show_step(0)
        
    def show_step(self, step_number):
        
        self.current_step = step_number
        
        
        self.root.title(f"NetIntelAgent - Шаг №{step_number + 1}")
        
        
        self.step1_frame.place_forget()
        self.step2_frame.place_forget()
        self.step3_frame.place_forget()
        self.step4_frame.place_forget()
        
        
        if step_number == 0:
            self.step1_frame.place(relwidth=1, relheight=1)
            self.main_window.previous_button.config(state=tk.DISABLED)
            update_button_state(self.main_window.previous_button, tk.DISABLED)
            self.main_window.next_button.config(state=tk.NORMAL)
            update_button_state(self.main_window.next_button, tk.NORMAL)
        elif step_number == 1:
            self.step2_frame.place(relwidth=1, relheight=1)
            self.main_window.previous_button.config(state=tk.NORMAL)
            update_button_state(self.main_window.previous_button, tk.NORMAL)
            self.main_window.next_button.config(state=tk.NORMAL)
            update_button_state(self.main_window.next_button, tk.NORMAL)
        elif step_number == 2:
            self.step3_frame.place(relwidth=1, relheight=1)
            self.main_window.previous_button.config(state=tk.NORMAL)
            update_button_state(self.main_window.previous_button, tk.NORMAL)
            self.main_window.next_button.config(state=tk.NORMAL)
            update_button_state(self.main_window.next_button, tk.NORMAL)
            
            self.step3_frame.update_idletasks()
            self.root.update()
        elif step_number == 3:
            self.step4_frame.place(relwidth=1, relheight=1)
            self.main_window.previous_button.config(state=tk.NORMAL)
            update_button_state(self.main_window.previous_button, tk.NORMAL)
            self.main_window.next_button.config(state=tk.DISABLED)
            update_button_state(self.main_window.next_button, tk.DISABLED)
        
        
        self.root.update()
    
    def go_next(self):
        
        if self.current_step == 0:
            if self.step1_frame.check_data():
                
                self.show_step(1)
                self.step2_frame.initialize_grids()
                
                self.root.update_idletasks()
        elif self.current_step == 1:
            if self.step2_frame.check_data():
                
                self.step2_frame.get_source_data()
                self.show_step(2)
        elif self.current_step == 2:
            
            self.process_calculations()
            self.show_step(3)
            self.step4_frame.initialize_results()
            
            self.root.update_idletasks()

    def go_previous(self):
        
        if self.current_step > 0:
            prev_step = self.current_step - 1
            self.show_step(prev_step)
            
            
            if prev_step == 0:
                if self.transition_probability_grid_initiated:
                    self.step1_frame.initialize_transition_probability_grid()
            elif prev_step == 1:
                if self.source_data_grid_initiated:
                    self.step2_frame.initialize_grids()
            
            
            self.root.update_idletasks()
    
    def process_calculations(self):
        
        
        self.math = MathEquations(
            self.source_count, 
            self.pj, 
            self.P, 
            self.Ks, 
            self.Kf, 
            self.Fs, 
            self.Ff, 
            self.time_limit
        )
        
        
        col_count = 0
        
        if self.step3_frame.check1_var.get():
            col_count += 1
            self.math.indefinit_func()
            
        if self.step3_frame.check2_var.get():
            col_count += 1
            self.math.fand()
            
        if self.step3_frame.check3_var.get():
            col_count += 1
            self.math.for_calculation()
            
        if self.step3_frame.check4_var.get():
            col_count += 1
            self.math.frepl()
            
        if self.step3_frame.check5_var.get():
            col_count += 1
            self.math.fnonrepl()
            
        if self.step3_frame.check6_var.get():
            col_count += 2
            self.math.fsf_all()
        
        
        self.col_count = col_count