"""
NetIntelAgent - Network Intelligence Agent
Step 2 UI frame - Source probabilities and distribution data
"""

import tkinter as tk
from tkinter import messagebox
from utils.styles import (
    create_label, create_entry, create_header_label,
    BACKGROUND_COLOR, FIELD_BG_COLOR, TEXT_COLOR
)
from utils.helpers import format_number

class Step2Frame(tk.Frame):
    
    
    def __init__(self, parent, controller):
        """Initialize the step 2 frame
        
        Args:
            parent: Parent widget
            controller: Application controller
        """
        super().__init__(parent, bg=BACKGROUND_COLOR)
        self.controller = controller
        
        
        self.create_widgets()
    
    def create_widgets(self):
        
        
        self.prob_label = create_label(
            self, 
            text="Вероятности удачного перехода для каждого источника"
        )
        self.prob_label.pack(anchor="w", padx=10, pady=(10, 5))
        
        
        self.prob_frame = tk.Frame(self, bg="white")
        self.prob_frame.pack(fill=tk.X, padx=10, pady=5)
        
        
        self.dist_label = create_label(
            self, 
            text="Распределения вероятностей для каждого источника"
        )
        self.dist_label.pack(anchor="w", padx=10, pady=(20, 5))
        
        
        self.dist_frame = tk.Frame(self, bg="white")
        self.dist_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        
        self.prob_cells = []
        self.dist_cells = []
    
    def initialize_grids(self):
        
        source_count = self.controller.source_count
        
        
        for widget in self.prob_frame.winfo_children():
            widget.destroy()
        for widget in self.dist_frame.winfo_children():
            widget.destroy()
        
        
        self.prob_cells = []
        
        
        for j in range(source_count):
            header = create_header_label(
                self.prob_frame, 
                text=f"P{j+1}", 
                width=10
            )
            header.grid(row=0, column=j, sticky="nsew")
        
        
        row_cells = []
        for j in range(source_count):
            cell = create_entry(self.prob_frame, width=10)
            
            if hasattr(self.controller, 'pj') and len(self.controller.pj) > j and self.controller.pj[j] != 0.0:
                cell.insert(0, format_number(self.controller.pj[j]))
            else:
                cell.insert(0, "0.5")  
            cell.grid(row=1, column=j, sticky="nsew", padx=1, pady=1)
            row_cells.append(cell)
        self.prob_cells = row_cells
        
        
        self.dist_cells = []
        
        
        default_fs = 0.5
        default_ff = 0.5
        
        
        for i in range(source_count):
            
            create_header_label(self.dist_frame, text=f"k0{i+1}s", width=10).grid(row=0, column=i*4)
            create_header_label(self.dist_frame, text=f"F{i+1}s", width=10).grid(row=0, column=i*4+1)
            create_header_label(self.dist_frame, text=f"k0{i+1}f", width=10).grid(row=0, column=i*4+2)
            create_header_label(self.dist_frame, text=f"F{i+1}f", width=10).grid(row=0, column=i*4+3)
            
            
            bg_color = "#f5f5f5" if i % 2 == 0 else "#ffffff"
            
            
            source_cells = []
            for row in range(5):
                
                ks_cell = create_entry(self.dist_frame, width=10)
                ks_cell.grid(row=row+1, column=i*4, padx=1, pady=1)
                
                if hasattr(self.controller, 'Ks') and len(self.controller.Ks) > i and row < len(self.controller.Ks[i]):
                    ks_cell.insert(0, format_number(self.controller.Ks[i][row]))
                elif row < 2:  
                    ks_cell.insert(0, format_number(str(row+1)))
                source_cells.append(ks_cell)
                
                
                fs_cell = create_entry(self.dist_frame, width=10)
                fs_cell.grid(row=row+1, column=i*4+1, padx=1, pady=1)
                
                if hasattr(self.controller, 'Fs') and len(self.controller.Fs) > i and row < len(self.controller.Fs[i]):
                    fs_cell.insert(0, format_number(self.controller.Fs[i][row]))
                elif row < 2:  
                    fs_value = default_fs if row == 0 else 1 - default_fs
                    fs_cell.insert(0, format_number(str(fs_value)))
                source_cells.append(fs_cell)
                
                
                kf_cell = create_entry(self.dist_frame, width=10)
                kf_cell.grid(row=row+1, column=i*4+2, padx=1, pady=1)
                
                if hasattr(self.controller, 'Kf') and len(self.controller.Kf) > i and row < len(self.controller.Kf[i]):
                    kf_cell.insert(0, format_number(self.controller.Kf[i][row]))
                elif row < 2:  
                    kf_cell.insert(0, format_number(str(row+1)))
                source_cells.append(kf_cell)
                
                
                ff_cell = create_entry(self.dist_frame, width=10)
                ff_cell.grid(row=row+1, column=i*4+3, padx=1, pady=1)
                
                if hasattr(self.controller, 'Ff') and len(self.controller.Ff) > i and row < len(self.controller.Ff[i]):
                    ff_cell.insert(0, format_number(self.controller.Ff[i][row]))
                elif row < 2:  
                    ff_value = default_ff if row == 0 else 1 - default_ff
                    ff_cell.insert(0, format_number(str(ff_value)))
                source_cells.append(ff_cell)
            
            self.dist_cells.append(source_cells)
        
        
        self.controller.source_data_grid_initiated = True
    
    def get_source_data(self):
        
        source_count = self.controller.source_count
        
        
        self.controller.Fs = [[] for _ in range(source_count)]
        self.controller.Ff = [[] for _ in range(source_count)]
        self.controller.Ks = [[] for _ in range(source_count)]
        self.controller.Kf = [[] for _ in range(source_count)]
        self.controller.pj = [0.0] * source_count
        
        
        for j in range(source_count):
            try:
                self.controller.pj[j] = float(self.prob_cells[j].get())
            except ValueError:
                self.controller.pj[j] = 0.5  
        
        
        for i in range(source_count):
            cells = self.dist_cells[i]
            
            
            ks_values = []
            fs_values = []
            kf_values = []
            ff_values = []
            
            for row in range(5):  
                
                ks_cell_idx = row * 4
                ks_cell = cells[ks_cell_idx]
                if ks_cell.get():
                    try:
                        ks_values.append(int(ks_cell.get()))
                    except ValueError:
                        continue
                
                
                fs_cell_idx = row * 4 + 1
                fs_cell = cells[fs_cell_idx]
                if fs_cell.get():
                    try:
                        fs_values.append(float(fs_cell.get()))
                    except ValueError:
                        continue
                
                
                kf_cell_idx = row * 4 + 2
                kf_cell = cells[kf_cell_idx]
                if kf_cell.get():
                    try:
                        kf_values.append(int(kf_cell.get()))
                    except ValueError:
                        continue
                
                
                ff_cell_idx = row * 4 + 3
                ff_cell = cells[ff_cell_idx]
                if ff_cell.get():
                    try:
                        ff_values.append(float(ff_cell.get()))
                    except ValueError:
                        continue
            
            
            self.controller.Ks[i] = ks_values
            self.controller.Fs[i] = fs_values
            self.controller.Kf[i] = kf_values
            self.controller.Ff[i] = ff_values
    
    def check_data(self):
        """Validate the data before proceeding to next step
        
        Returns:
            bool: True if data is valid, False otherwise
        """
        source_count = self.controller.source_count
        
        
        for i in range(source_count):
            try:
                value = float(self.prob_cells[i].get())
                if value < 0.0 or value > 1.0:
                    messagebox.showerror(
                        "Ошибка ввода данных",
                        f"Введено неверное значение вероятности для P{i+1}"
                    )
                    return False
            except ValueError:
                messagebox.showerror(
                    "Ошибка ввода данных",
                    f"Введено неверное значение вероятности для P{i+1}"
                )
                return False
        
        
        for i in range(source_count):
            cells = self.dist_cells[i]
            
            
            ks_count = 0
            fs_count = 0
            kf_count = 0
            ff_count = 0
            
            
            fs_sum = 0.0
            ff_sum = 0.0
            
            for row in range(5):  
                
                ks_cell_idx = row * 4
                if cells[ks_cell_idx].get():
                    ks_count += 1
                
                
                fs_cell_idx = row * 4 + 1
                if cells[fs_cell_idx].get():
                    fs_count += 1
                    try:
                        fs_sum += float(cells[fs_cell_idx].get())
                    except ValueError:
                        messagebox.showerror(
                            "Ошибка ввода данных",
                            f"Введено неверное значение в колонке F{i+1}s"
                        )
                        return False
                
                
                kf_cell_idx = row * 4 + 2
                if cells[kf_cell_idx].get():
                    kf_count += 1
                
                
                ff_cell_idx = row * 4 + 3
                if cells[ff_cell_idx].get():
                    ff_count += 1
                    try:
                        ff_sum += float(cells[ff_cell_idx].get())
                    except ValueError:
                        messagebox.showerror(
                            "Ошибка ввода данных",
                            f"Введено неверное значение в колонке F{i+1}f"
                        )
                        return False
            
            
            if ks_count != fs_count or ks_count == 0:
                messagebox.showerror(
                    "Ошибка ввода данных",
                    f"В колонках k0{i+1}s и F{i+1}s введены неверные данные"
                )
                return False
            
            if kf_count != ff_count or kf_count == 0:
                messagebox.showerror(
                    "Ошибка ввода данных",
                    f"В колонках k0{i+1}f и F{i+1}f введены неверные данные"
                )
                return False
            
            
            if abs(fs_sum - 1.0) > 0.01:
                messagebox.showerror(
                    "Ошибка ввода данных",
                    f"В колонке F{i+1}s сумма значений не равна единице"
                )
                return False
            
            if abs(ff_sum - 1.0) > 0.01:
                messagebox.showerror(
                    "Ошибка ввода данных",
                    f"В колонке F{i+1}f сумма значений не равна единице"
                )
                return False
        
        return True