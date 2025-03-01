"""
NetIntelAgent - Network Intelligence Agent
Step 4 UI frame - Results display
"""

import tkinter as tk
from utils.styles import (
    create_label, create_header_label, create_cell_label,
    BACKGROUND_COLOR, FIELD_BG_COLOR, TEXT_COLOR
)
from utils.helpers import format_number

class Step4Frame(tk.Frame):
    
    
    
    HEADER_WIDTH = 12       
    DATA_COL_WIDTH = 15     
    K_COL_WIDTH = 5         
    
    def __init__(self, parent, controller):
        """Initialize the step 4 frame
        
        Args:
            parent: Parent widget
            controller: Application controller
        """
        super().__init__(parent, bg=BACKGROUND_COLOR)
        self.controller = controller
        
        
        self.create_widgets()
    
    def create_widgets(self):
        
        
        final_data_label = create_label(
            self, 
            text="Конечные данные", 
            font=("Arial", 12, "bold")
        )
        final_data_label.pack(anchor="w", padx=10, pady=(15, 5))
        
        
        self.table1_container = tk.Frame(self)
        self.table1_container.pack(fill=tk.X, padx=10, pady=5)
        
        
        self.table1_xscroll = tk.Scrollbar(self.table1_container, orient=tk.HORIZONTAL)
        self.table1_xscroll.pack(side=tk.BOTTOM, fill=tk.X)
        
        
        self.table1_canvas = tk.Canvas(self.table1_container, 
                                    xscrollcommand=self.table1_xscroll.set,
                                    highlightthickness=0)
        self.table1_canvas.pack(fill=tk.X, expand=True)
        
        
        self.table1_xscroll.config(command=self.table1_canvas.xview)
        
        
        self.final_data_frame = tk.Frame(self.table1_canvas, bg="white")
        self.table1_canvas.create_window((0, 0), window=self.final_data_frame, anchor="nw")
        
        
        
        dist_label = create_label(
            self, 
            text="Распределения вероятностей", 
            font=("Arial", 12, "bold")
        )
        dist_label.pack(anchor="w", padx=10, pady=(15, 5))
        
        
        self.table2_container = tk.Frame(self)
        self.table2_container.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        
        self.table2_xscroll = tk.Scrollbar(self.table2_container, orient=tk.HORIZONTAL)
        self.table2_xscroll.pack(side=tk.BOTTOM, fill=tk.X)
        
        self.table2_yscroll = tk.Scrollbar(self.table2_container)
        self.table2_yscroll.pack(side=tk.RIGHT, fill=tk.Y)
        
        
        self.table2_canvas = tk.Canvas(self.table2_container, 
                                    xscrollcommand=self.table2_xscroll.set,
                                    yscrollcommand=self.table2_yscroll.set,
                                    highlightthickness=0)
        self.table2_canvas.pack(fill=tk.BOTH, expand=True)
        
        
        self.table2_xscroll.config(command=self.table2_canvas.xview)
        self.table2_yscroll.config(command=self.table2_canvas.yview)
        
        
        self.dist_frame = tk.Frame(self.table2_canvas, bg="white")
        self.table2_canvas.create_window((0, 0), window=self.dist_frame, anchor="nw")
        
        
        self.dist_frame.bind("<Configure>", self._on_dist_frame_configure)
        self.final_data_frame.bind("<Configure>", self._on_final_frame_configure)

    def _on_dist_frame_configure(self, event):
        
        
        self.table2_canvas.configure(scrollregion=self.table2_canvas.bbox("all"))

    def _on_final_frame_configure(self, event):
        
        
        self.table1_canvas.configure(scrollregion=self.table1_canvas.bbox("all"))
    
    def initialize_results(self):
        
        
        math = self.controller.math
        col_count = self.controller.col_count
        
        
        for widget in self.final_data_frame.winfo_children():
            widget.destroy()
        for widget in self.dist_frame.winfo_children():
            widget.destroy()
        
        
        
        create_header_label(
            self.final_data_frame, 
            text="P(k<Nmax)", 
            width=self.HEADER_WIDTH
        ).grid(row=1, column=0, sticky="nsew")
        
        create_header_label(
            self.final_data_frame, 
            text="MO", 
            width=self.HEADER_WIDTH
        ).grid(row=2, column=0, sticky="nsew")
        
        
        col_idx = 1
        
        
        if self.controller.step3_frame.check1_var.get():
            
            create_header_label(
                self.final_data_frame, 
                text="Динамический приоритет", 
                width=self.DATA_COL_WIDTH
            ).grid(row=0, column=col_idx, sticky="nsew")
            
            
            create_cell_label(
                self.final_data_frame, 
                text=format_number(math.PNmax_indef), 
                width=self.DATA_COL_WIDTH
            ).grid(row=1, column=col_idx, sticky="nsew")
            
            
            create_cell_label(
                self.final_data_frame, 
                text=format_number(math.MO_indef), 
                width=self.DATA_COL_WIDTH
            ).grid(row=2, column=col_idx, sticky="nsew")
            
            col_idx += 1
        
        if self.controller.step3_frame.check2_var.get():
            
            create_header_label(
                self.final_data_frame, 
                text="И", 
                width=self.DATA_COL_WIDTH
            ).grid(row=0, column=col_idx, sticky="nsew")
            
            
            create_cell_label(
                self.final_data_frame, 
                text=format_number(math.PNmax_and), 
                width=self.DATA_COL_WIDTH
            ).grid(row=1, column=col_idx, sticky="nsew")
            
            
            create_cell_label(
                self.final_data_frame, 
                text=format_number(math.MO_and), 
                width=self.DATA_COL_WIDTH
            ).grid(row=2, column=col_idx, sticky="nsew")
            
            col_idx += 1
        
        if self.controller.step3_frame.check3_var.get():
            
            create_header_label(
                self.final_data_frame, 
                text="Или", 
                width=self.DATA_COL_WIDTH
            ).grid(row=0, column=col_idx, sticky="nsew")
            
            
            create_cell_label(
                self.final_data_frame, 
                text=format_number(math.PNmax_or), 
                width=self.DATA_COL_WIDTH
            ).grid(row=1, column=col_idx, sticky="nsew")
            
            
            create_cell_label(
                self.final_data_frame, 
                text=format_number(math.MO_or), 
                width=self.DATA_COL_WIDTH
            ).grid(row=2, column=col_idx, sticky="nsew")
            
            col_idx += 1
        
        if self.controller.step3_frame.check4_var.get():
            
            create_header_label(
                self.final_data_frame, 
                text="Послед. реплиц.", 
                width=self.DATA_COL_WIDTH
            ).grid(row=0, column=col_idx, sticky="nsew")
            
            
            create_cell_label(
                self.final_data_frame, 
                text=format_number(math.PNmax_replic), 
                width=self.DATA_COL_WIDTH
            ).grid(row=1, column=col_idx, sticky="nsew")
            
            
            create_cell_label(
                self.final_data_frame, 
                text=format_number(math.MO_replic), 
                width=self.DATA_COL_WIDTH
            ).grid(row=2, column=col_idx, sticky="nsew")
            
            col_idx += 1
        
        if self.controller.step3_frame.check5_var.get():
            
            create_header_label(
                self.final_data_frame, 
                text="Послед. нереплиц.", 
                width=self.DATA_COL_WIDTH
            ).grid(row=0, column=col_idx, sticky="nsew")
            
            
            create_cell_label(
                self.final_data_frame, 
                text=format_number(math.PNmax_nonreplic), 
                width=self.DATA_COL_WIDTH
            ).grid(row=1, column=col_idx, sticky="nsew")
            
            
            create_cell_label(
                self.final_data_frame, 
                text=format_number(math.MO_nonreplic), 
                width=self.DATA_COL_WIDTH
            ).grid(row=2, column=col_idx, sticky="nsew")
            
            col_idx += 1
        
        if self.controller.step3_frame.check6_var.get():
            
            create_header_label(
                self.final_data_frame, 
                text="Достиж. цели Fs", 
                width=self.DATA_COL_WIDTH
            ).grid(row=0, column=col_idx, sticky="nsew")
            
            
            create_cell_label(
                self.final_data_frame, 
                text=format_number(math.PNmax_Fs_all), 
                width=self.DATA_COL_WIDTH
            ).grid(row=1, column=col_idx, sticky="nsew")
            
            
            create_cell_label(
                self.final_data_frame, 
                text=format_number(math.MO_Fs_all), 
                width=self.DATA_COL_WIDTH
            ).grid(row=2, column=col_idx, sticky="nsew")
            
            col_idx += 1
            
            
            create_header_label(
                self.final_data_frame, 
                text="Достиж. цели Ff", 
                width=self.DATA_COL_WIDTH
            ).grid(row=0, column=col_idx, sticky="nsew")
            
            
            create_cell_label(
                self.final_data_frame, 
                text=format_number(math.PNmax_Ff_all), 
                width=self.DATA_COL_WIDTH
            ).grid(row=1, column=col_idx, sticky="nsew")
            
            
            create_cell_label(
                self.final_data_frame, 
                text=format_number(math.MO_Ff_all), 
                width=self.DATA_COL_WIDTH
            ).grid(row=2, column=col_idx, sticky="nsew")
        
        
        
        max_rows = 0
        
        if self.controller.step3_frame.check1_var.get() and math.Kindef is not None:
            max_rows = max(max_rows, len(math.Kindef))
        
        if self.controller.step3_frame.check2_var.get() and math.Kand is not None:
            max_rows = max(max_rows, len(math.Kand))
        
        if self.controller.step3_frame.check3_var.get() and math.Kor is not None:
            max_rows = max(max_rows, len(math.Kor))
            
        if self.controller.step3_frame.check4_var.get() and math.Krepl_ is not None:
            max_rows = max(max_rows, len(math.Krepl_))
            
        if self.controller.step3_frame.check5_var.get() and math.Krepl_ is not None:
            max_rows = max(max_rows, len(math.Krepl_))
            
        if self.controller.step3_frame.check6_var.get():
            if math.Ks_all is not None:
                max_rows = max(max_rows, len(math.Ks_all))
            if math.Kf_all is not None:
                max_rows = max(max_rows, len(math.Kf_all))
        
        
        dist_col_idx = 0
        
        if self.controller.step3_frame.check1_var.get() and math.Kindef is not None and math.Findef is not None:
            
            create_header_label(
                self.dist_frame, 
                text="k", 
                width=self.K_COL_WIDTH
            ).grid(row=0, column=dist_col_idx, sticky="nsew")
            
            
            create_header_label(
                self.dist_frame, 
                text="Динамический приоритет", 
                width=self.DATA_COL_WIDTH
            ).grid(row=0, column=dist_col_idx+1, sticky="nsew")
            
            
            for i in range(len(math.Kindef)):
                if i < len(math.Kindef):
                    
                    create_cell_label(
                        self.dist_frame, 
                        text=str(math.Kindef[i]), 
                        width=self.K_COL_WIDTH
                    ).grid(row=i+1, column=dist_col_idx, sticky="nsew")
                    
                    
                    if i < len(math.Findef):
                        create_cell_label(
                            self.dist_frame, 
                            text=format_number(math.Findef[i]), 
                            width=self.DATA_COL_WIDTH
                        ).grid(row=i+1, column=dist_col_idx+1, sticky="nsew")
            
            dist_col_idx += 2
        
        if self.controller.step3_frame.check2_var.get() and math.Kand is not None and math.Fand is not None:
            
            create_header_label(
                self.dist_frame, 
                text="k", 
                width=self.K_COL_WIDTH
            ).grid(row=0, column=dist_col_idx, sticky="nsew")
            
            
            create_header_label(
                self.dist_frame, 
                text="И", 
                width=self.DATA_COL_WIDTH
            ).grid(row=0, column=dist_col_idx+1, sticky="nsew")
            
            
            for i in range(len(math.Kand)):
                if i < len(math.Kand):
                    
                    create_cell_label(
                        self.dist_frame, 
                        text=str(math.Kand[i]), 
                        width=self.K_COL_WIDTH
                    ).grid(row=i+1, column=dist_col_idx, sticky="nsew")
                    
                    
                    if i < len(math.Fand):
                        create_cell_label(
                            self.dist_frame, 
                            text=format_number(math.Fand[i]), 
                            width=self.DATA_COL_WIDTH
                        ).grid(row=i+1, column=dist_col_idx+1, sticky="nsew")
            
            dist_col_idx += 2
        
        if self.controller.step3_frame.check3_var.get() and math.Kor is not None and math.For is not None:
            
            create_header_label(
                self.dist_frame, 
                text="k", 
                width=self.K_COL_WIDTH
            ).grid(row=0, column=dist_col_idx, sticky="nsew")
            
            
            create_header_label(
                self.dist_frame, 
                text="Или", 
                width=self.DATA_COL_WIDTH
            ).grid(row=0, column=dist_col_idx+1, sticky="nsew")
            
            
            for i in range(len(math.Kor)):
                if i < len(math.Kor):
                    
                    create_cell_label(
                        self.dist_frame, 
                        text=str(math.Kor[i]), 
                        width=self.K_COL_WIDTH
                    ).grid(row=i+1, column=dist_col_idx, sticky="nsew")
                    
                    
                    if i < len(math.For):
                        create_cell_label(
                            self.dist_frame, 
                            text=format_number(math.For[i]), 
                            width=self.DATA_COL_WIDTH
                        ).grid(row=i+1, column=dist_col_idx+1, sticky="nsew")
            
            dist_col_idx += 2
        
        if self.controller.step3_frame.check4_var.get() and math.Krepl_ is not None and math.Frepl is not None:
            
            create_header_label(
                self.dist_frame, 
                text="k", 
                width=self.K_COL_WIDTH
            ).grid(row=0, column=dist_col_idx, sticky="nsew")
            
            
            create_header_label(
                self.dist_frame, 
                text="Послед. реплиц.", 
                width=self.DATA_COL_WIDTH
            ).grid(row=0, column=dist_col_idx+1, sticky="nsew")
            
            
            for i in range(len(math.Krepl_)):
                if i < len(math.Krepl_):
                    
                    create_cell_label(
                        self.dist_frame, 
                        text=str(math.Krepl_[i]), 
                        width=self.K_COL_WIDTH
                    ).grid(row=i+1, column=dist_col_idx, sticky="nsew")
                    
                    
                    if i < len(math.Frepl):
                        create_cell_label(
                            self.dist_frame, 
                            text=format_number(math.Frepl[i]), 
                            width=self.DATA_COL_WIDTH
                        ).grid(row=i+1, column=dist_col_idx+1, sticky="nsew")
            
            dist_col_idx += 2
        
        if self.controller.step3_frame.check5_var.get() and math.Krepl_ is not None and math.Fnonrepl is not None:
            
            create_header_label(
                self.dist_frame, 
                text="k", 
                width=self.K_COL_WIDTH
            ).grid(row=0, column=dist_col_idx, sticky="nsew")
            
            
            create_header_label(
                self.dist_frame, 
                text="Послед. нереплиц.", 
                width=self.DATA_COL_WIDTH
            ).grid(row=0, column=dist_col_idx+1, sticky="nsew")
            
            
            for i in range(len(math.Krepl_)):
                if i < len(math.Krepl_):
                    
                    create_cell_label(
                        self.dist_frame, 
                        text=str(math.Krepl_[i]), 
                        width=self.K_COL_WIDTH
                    ).grid(row=i+1, column=dist_col_idx, sticky="nsew")
                    
                    
                    if i < len(math.Fnonrepl):
                        create_cell_label(
                            self.dist_frame, 
                            text=format_number(math.Fnonrepl[i]), 
                            width=self.DATA_COL_WIDTH
                        ).grid(row=i+1, column=dist_col_idx+1, sticky="nsew")
            
            dist_col_idx += 2
        
        if self.controller.step3_frame.check6_var.get():
            if math.Ks_all is not None and math.Fs_all is not None:
                
                create_header_label(
                    self.dist_frame, 
                    text="k", 
                    width=self.K_COL_WIDTH
                ).grid(row=0, column=dist_col_idx, sticky="nsew")
                
                
                create_header_label(
                    self.dist_frame, 
                    text="Достиж. цели Fs", 
                    width=self.DATA_COL_WIDTH
                ).grid(row=0, column=dist_col_idx+1, sticky="nsew")
                
                
                for i in range(len(math.Ks_all)):
                    if i < len(math.Ks_all):
                        
                        create_cell_label(
                            self.dist_frame, 
                            text=str(math.Ks_all[i]), 
                            width=self.K_COL_WIDTH
                        ).grid(row=i+1, column=dist_col_idx, sticky="nsew")
                        
                        
                        if i < len(math.Fs_all):
                            create_cell_label(
                                self.dist_frame, 
                                text=format_number(math.Fs_all[i]), 
                                width=self.DATA_COL_WIDTH
                            ).grid(row=i+1, column=dist_col_idx+1, sticky="nsew")
                
                dist_col_idx += 2
            
            if math.Kf_all is not None and math.Ff_all is not None:
                
                create_header_label(
                    self.dist_frame, 
                    text="k", 
                    width=self.K_COL_WIDTH
                ).grid(row=0, column=dist_col_idx, sticky="nsew")
                
                
                create_header_label(
                    self.dist_frame, 
                    text="Достиж. цели Ff", 
                    width=self.DATA_COL_WIDTH
                ).grid(row=0, column=dist_col_idx+1, sticky="nsew")
                
                
                for i in range(len(math.Kf_all)):
                    if i < len(math.Kf_all):
                        
                        create_cell_label(
                            self.dist_frame, 
                            text=str(math.Kf_all[i]), 
                            width=self.K_COL_WIDTH
                        ).grid(row=i+1, column=dist_col_idx, sticky="nsew")
                        
                        if i < len(math.Ff_all):
                            create_cell_label(
                                self.dist_frame, 
                                text=format_number(math.Ff_all[i]), 
                                width=self.DATA_COL_WIDTH
                            ).grid(row=i+1, column=dist_col_idx+1, sticky="nsew")