import tkinter as tk
from app import NetIntelApp

def main():
    
    root = tk.Tk()
    root.title("NetIntelAgent")
    
    root.minsize(666, 420)
    
    app = NetIntelApp(root)
    
    window_width = 960
    window_height = 520
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    center_x = int((screen_width - window_width) / 2)
    center_y = int((screen_height - window_height) / 2)
    root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
    
    root.mainloop()

if __name__ == "__main__":
    main()