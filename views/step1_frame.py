"""
NetIntelAgent - Network Intelligence Agent
Step 1 UI frame - Source count and transition probability matrix
"""

import tkinter as tk
from tkinter import messagebox
from utils.styles import (
    create_label, create_entry, create_button, 
    create_header_label, BACKGROUND_COLOR, FIELD_BG_COLOR, TEXT_COLOR
)
from utils.helpers import format_number

class Step1Frame(tk.Frame):
    
    
    def __init__(self, parent, controller):
        """Initialize the step 1 frame
        
        Args:
            parent: Parent widget
            controller: Application controller
        """
        super().__init__(parent, bg=BACKGROUND_COLOR)
        self.controller = controller
        
        
        self.create_widgets()
    
    def create_widgets(self):
        
        
        input_frame = tk.Frame(self, bg=BACKGROUND_COLOR)
        input_frame.pack(fill=tk.X, padx=10, pady=10)
        
        
        source_count_label = create_label(
            input_frame, 
            text="Введите количество ресурсов сети:"
        )
        source_count_label.grid(row=0, column=0, sticky="w", padx=5, pady=5)
        
        self.source_count_entry = create_entry(input_frame, width=10)
        self.source_count_entry.grid(row=0, column=1, padx=5, pady=5)
        self.source_count_entry.bind("<Return>", self.on_source_count_enter)
        
        
        time_limit_label = create_label(
            input_frame, 
            text="Временное ограничение:"
        )
        time_limit_label.grid(row=0, column=2, sticky="w", padx=5, pady=5)
        
        self.time_limit_entry = create_entry(input_frame, width=10)
        self.time_limit_entry.grid(row=0, column=3, padx=5, pady=5)
        self.time_limit_entry.bind("<Return>", self.on_source_count_enter)
        
        
        self.ok_button = create_button(
            input_frame, 
            text="OK", 
            command=self.on_source_count_button
        )
        self.ok_button.grid(row=0, column=4, padx=5, pady=5)
        
        
        probability_label = create_label(
            self, 
            text="Вероятности новых переходов"
        )
        probability_label.pack(anchor="w", padx=10, pady=(20, 5))
        
        
        self.grid_frame = tk.Frame(self, bg="white")
        self.grid_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        
        self.transition_prob_frame = tk.Frame(self.grid_frame, bg="white")
        self.transition_prob_frame.pack(fill=tk.BOTH, expand=True)
        
        
        self.cells = []
    
    def on_source_count_enter(self, event):
        
        self.on_source_count_button()
    
    def on_source_count_button(self):
        
        try:
            
            source_count = int(self.source_count_entry.get())
            self.controller.source_count = source_count
            
            
            time_limit = int(self.time_limit_entry.get())
            self.controller.time_limit = time_limit
            
            
            self.initialize_transition_probability_grid()
            
        except ValueError:
            messagebox.showerror(
                "Ошибка ввода данных", 
                "Количество источников и временное ограничение должны быть указаны как целые числа!"
            )
    
    def initialize_transition_probability_grid(self):
        
        
        for widget in self.transition_prob_frame.winfo_children():
            widget.destroy()
        
        
        source_count = self.controller.source_count
        self.cells = []
        
        
        default_prob = 1.0 / source_count
        
        
        for j in range(source_count + 1):
            if j == 0:
                
                header = create_header_label(self.transition_prob_frame, text="", width=5)
                header.grid(row=0, column=0, sticky="nsew")
            else:
                
                header = create_header_label(
                    self.transition_prob_frame, 
                    text=str(j), 
                    width=10
                )
                header.grid(row=0, column=j, sticky="nsew")
        
        
        for i in range(source_count):
            row_cells = []
            
            
            header = create_header_label(
                self.transition_prob_frame, 
                text=str(i + 1), 
                width=5
            )
            header.grid(row=i + 1, column=0, sticky="nsew")
            
            
            for j in range(source_count):
                cell = create_entry(self.transition_prob_frame, width=10)
                cell.insert(0, format_number(default_prob))
                cell.grid(row=i + 1, column=j + 1, sticky="nsew", padx=1, pady=1)
                row_cells.append(cell)
            
            self.cells.append(row_cells)
        
        
        self.controller.transition_probability_grid_initiated = True
    
    def check_data(self):
        """Validate the data before proceeding to next step
        
        Returns:
            bool: True if data is valid, False otherwise
        """
        
        try:
            source_count = int(self.source_count_entry.get())
            time_limit = int(self.time_limit_entry.get())
            
            
            self.controller.source_count = source_count
            self.controller.time_limit = time_limit
            
            
            if not self.controller.transition_probability_grid_initiated:
                self.initialize_transition_probability_grid()
                return False
            
            
            for i in range(source_count):
                row_sum = 0.0
                for j in range(source_count):
                    try:
                        value = float(self.cells[i][j].get())
                        row_sum += value
                    except ValueError:
                        messagebox.showerror(
                            "Ошибка ввода данных",
                            f"В ячейке [{i+1},{j+1}] введено неверное значение"
                        )
                        return False
                
                
                if abs(row_sum - 1.0) > 0.0001:
                    messagebox.showerror(
                        "Ошибка ввода данных",
                        f"В колонке №{i+1} сумма значений не равна единице"
                    )
                    return False
            
            
            self.controller.P = [0.0] * source_count
            for i in range(source_count):
                self.controller.P[i] = float(self.cells[0][i].get())
            
            return True
            
        except ValueError:
            messagebox.showerror(
                "Ошибка ввода данных",
                "Количество источников и временное ограничение должны быть указаны как целые числа!"
            )
            return False