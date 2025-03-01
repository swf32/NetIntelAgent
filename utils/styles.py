"""
NetIntelAgent - Network Intelligence Agent
Common styles for UI consistency
"""

import tkinter as tk
from tkinter import ttk


BACKGROUND_COLOR = "#e0e0e0"  
HEADER_COLOR = "#d0d0d0"      
TEXT_COLOR = "#000000"        
FIELD_BG_COLOR = "#ffffff"    
BUTTON_BG_COLOR = "#28a745"   
BUTTON_TEXT_COLOR = "#000000" 
BUTTON_DISABLED_BG = "#cccccc" 
HIGHLIGHT_COLOR = "#28a745"   

def configure_styles():
    
    style = ttk.Style()
    
    
    style.theme_use('default')
    
    
    style.configure(
        "TButton",
        background=BUTTON_BG_COLOR,
        foreground=BUTTON_TEXT_COLOR,
        padding=4,
        relief="flat",
        font=("Arial", 12)
    )
    
    
    style.configure(
        "TButton",
        background=BUTTON_BG_COLOR,
        foreground=BUTTON_TEXT_COLOR,
        padding=4,
        relief="flat",
        font=("Arial", 14)
    )
    
    
    style.configure(
        "TCheckbutton",
        background=BACKGROUND_COLOR,
        foreground=TEXT_COLOR,
        font=("Arial", 14)
    )
    
    
    style.configure(
        "Custom.TCheckbutton",
        background=BACKGROUND_COLOR,
        foreground=TEXT_COLOR,
        font=("Arial", 14)
    )
    
    
    style.map("TButton",
        background=[('active', '#218838'), ('disabled', '#94c9a0')],
        foreground=[('disabled', '#e0e0e0')]
    )
    
    style.map("TCheckbutton",
        background=[('active', BACKGROUND_COLOR)],
        foreground=[('active', TEXT_COLOR)]
    )
    
    style.map("Custom.TCheckbutton",
        background=[('active', BACKGROUND_COLOR), ('!active', BACKGROUND_COLOR)],
        foreground=[('active', TEXT_COLOR), ('!active', TEXT_COLOR)]
    )

def create_label(parent, text, **kwargs):
    
    return tk.Label(
        parent,
        text=text,
        bg=kwargs.get("bg", BACKGROUND_COLOR),
        fg=TEXT_COLOR,
        font=kwargs.get("font", ("Arial", 13)),
        **{k: v for k, v in kwargs.items() if k not in ["bg", "fg", "font"]}
    )

def create_button(parent, text, command, **kwargs):
    
    button = tk.Button(
        parent,
        text=text,
        command=command,
        bg=BUTTON_BG_COLOR,
        fg=BUTTON_TEXT_COLOR,
        activebackground="#218838",  
        activeforeground=BUTTON_TEXT_COLOR,
        relief=tk.RAISED,
        borderwidth=1,
        disabledforeground="#777777",  
        font=("Arial", 14),
        padx=10,
        pady=5,
        highlightthickness=0,  
        **{k: v for k, v in kwargs.items() if k not in ['bg', 'fg', 'activebackground', 'activeforeground']}
    )
    
    
    return button

def update_button_state(button, state):
    
    if state == tk.DISABLED:
        button.config(bg='#cccccc')  
    else:
        button.config(bg=BUTTON_BG_COLOR)  

def create_entry(parent, width=10, **kwargs):
    
    entry = tk.Entry(
        parent,
        width=width,
        bg=FIELD_BG_COLOR,
        fg=TEXT_COLOR,
        relief=tk.SUNKEN,
        borderwidth=1,
        highlightthickness=1,
        highlightcolor=HIGHLIGHT_COLOR,  
        highlightbackground="#cccccc",   
        **kwargs
    )
    return entry

def create_header_label(parent, text, width=10, **kwargs):
    
    return tk.Label(
        parent,
        text=text,
        width=width,
        bg=HEADER_COLOR,
        fg=TEXT_COLOR,
        relief=tk.RAISED,
        borderwidth=1,
        **kwargs
    )

def create_cell_label(parent, text, width=10, **kwargs):
    
    return tk.Label(
        parent,
        text=text,
        width=width,
        bg=FIELD_BG_COLOR,
        fg=TEXT_COLOR,
        relief=tk.SUNKEN,
        borderwidth=1,
        **kwargs
    )