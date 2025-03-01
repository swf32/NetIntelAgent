"""
NetIntelAgent - Network Intelligence Agent
Step 3 UI frame - Method selection for uncertainty elimination
"""

import tkinter as tk
from tkinter import ttk
from utils.styles import create_label, BACKGROUND_COLOR, TEXT_COLOR, FIELD_BG_COLOR

class Step3Frame(tk.Frame):
    
    
    def __init__(self, parent, controller):
        super().__init__(parent, bg=BACKGROUND_COLOR)
        self.controller = controller
        self.create_widgets()
        
        self.update_idletasks()
    
    def create_widgets(self):
        
        
        for widget in self.winfo_children():
            widget.destroy()
            
        
        CHECKBOX_WIDTH = 4  
        CHECKBOX_FONT = ("Arial", 12)
        
        
        title_label = tk.Label(
            self,
            text="Выберите методы устранения неопределенности:",
            font=("Arial", 14, "bold"),
            bg=BACKGROUND_COLOR,
            fg=TEXT_COLOR
        )
        title_label.pack(anchor="nw", padx=20, pady=(20, 10))
        
        
        self.check1_var = tk.BooleanVar(value=True)
        self.check1 = tk.Checkbutton(
            self,
            text="Устранение неопределенности при синхронизации с динамическими приоритетами",
            variable=self.check1_var,
            bg=BACKGROUND_COLOR,
            fg=TEXT_COLOR,
            font=CHECKBOX_FONT,
            width=CHECKBOX_WIDTH,
            anchor="w",
            selectcolor="#d0d0d0",  
            activebackground=BACKGROUND_COLOR,
            highlightthickness=0  
        )
        self.check1.pack(anchor="w", padx=30, pady=10, fill=tk.X)
        
        self.check2_var = tk.BooleanVar(value=True)
        self.check2 = tk.Checkbutton(
            self,
            text="Устранение неопределенности при синхронизации параллельных действий ИА, описываемой логической функцией «И»",
            variable=self.check2_var,
            bg=BACKGROUND_COLOR,
            fg=TEXT_COLOR,
            font=CHECKBOX_FONT,
            width=CHECKBOX_WIDTH,
            anchor="w",
            selectcolor="#d0d0d0",
            activebackground=BACKGROUND_COLOR,
            highlightthickness=0
        )
        self.check2.pack(anchor="w", padx=30, pady=10, fill=tk.X)
        
        self.check3_var = tk.BooleanVar(value=True)
        self.check3 = tk.Checkbutton(
            self,
            text="Устранение неопределенности при синхронизации параллельных действий ИА, описываемой логической функцией «ИЛИ»",
            variable=self.check3_var,
            bg=BACKGROUND_COLOR,
            fg=TEXT_COLOR,
            font=CHECKBOX_FONT,
            width=CHECKBOX_WIDTH,
            anchor="w",
            selectcolor="#d0d0d0",
            activebackground=BACKGROUND_COLOR,
            highlightthickness=0
        )
        self.check3.pack(anchor="w", padx=30, pady=10, fill=tk.X)
        
        self.check4_var = tk.BooleanVar(value=True)
        self.check4 = tk.Checkbutton(
            self,
            text="Устранение неопределенности при последовательном опросе реплицированных источников информации",
            variable=self.check4_var,
            bg=BACKGROUND_COLOR,
            fg=TEXT_COLOR,
            font=CHECKBOX_FONT,
            width=CHECKBOX_WIDTH,
            anchor="w",
            selectcolor="#d0d0d0",
            activebackground=BACKGROUND_COLOR,
            highlightthickness=0
        )
        self.check4.pack(anchor="w", padx=30, pady=10, fill=tk.X)
        
        self.check5_var = tk.BooleanVar(value=True)
        self.check5 = tk.Checkbutton(
            self,
            text="Устранение неопределенности при последовательном опросе нереплицированных источников информации",
            variable=self.check5_var,
            bg=BACKGROUND_COLOR,
            fg=TEXT_COLOR,
            font=CHECKBOX_FONT,
            width=CHECKBOX_WIDTH,
            anchor="w",
            selectcolor="#d0d0d0",
            activebackground=BACKGROUND_COLOR,
            highlightthickness=0
        )
        self.check5.pack(anchor="w", padx=30, pady=10, fill=tk.X)
        
        self.check6_var = tk.BooleanVar(value=True)
        self.check6 = tk.Checkbutton(
            self,
            text="Устранение неопределенности при оценке достижимости цели",
            variable=self.check6_var,
            bg=BACKGROUND_COLOR,
            fg=TEXT_COLOR,
            font=CHECKBOX_FONT,
            width=CHECKBOX_WIDTH,
            anchor="w",
            selectcolor="#d0d0d0",
            activebackground=BACKGROUND_COLOR,
            highlightthickness=0
        )
        self.check6.pack(anchor="w", padx=30, pady=10, fill=tk.X)
        
        
        self.update()