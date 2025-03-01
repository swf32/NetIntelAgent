"""
NetIntelAgent - Network Intelligence Agent
Main window implementation
"""

import tkinter as tk
from tkinter import ttk
from utils.styles import configure_styles, create_button

class MainWindow(tk.Frame):
    
    
    def __init__(self, parent, controller):
        """Initialize the main window
        
        Args:
            parent: Parent widget
            controller: Application controller
        """
        super().__init__(parent, bg="#e0e0e0")
        self.controller = controller
        
        
        configure_styles()
        
        
        self.pack(fill=tk.BOTH, expand=True)
        
        
        self.container = tk.Frame(self, bg="#e0e0e0")
        self.container.pack(fill=tk.BOTH, expand=True, side=tk.TOP, padx=10, pady=10)
        
        
        self.button_frame = tk.Frame(self, bg="#e0e0e0")
        self.button_frame.pack(fill=tk.X, side=tk.BOTTOM, padx=10, pady=10)
        
        
        self.previous_button = create_button(
            self.button_frame, 
            text="Назад", 
            command=self.controller.go_previous
        )
        self.previous_button.config(state=tk.DISABLED)
        self.previous_button.pack(side=tk.LEFT, padx=5)
        
        self.next_button = create_button(
            self.button_frame, 
            text="Вперед", 
            command=self.controller.go_next
        )
        self.next_button.pack(side=tk.LEFT, padx=5)