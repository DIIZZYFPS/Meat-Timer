import tkinter as tk
from tkinter import ttk, messagebox
import winsound

class MeatTimer(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Meat Timer")

        self.resizable(False, False)
        window_width = 400
        window_height = 300

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)

        self.geometry(f"{window_width}x{window_height}+{x}+{y}")

        self.create_widgets()

    def create_widgets(self):
        self.meat_label = tk.Label(self, text="Choose a Meat")
        self.meat_label.pack()
        self.meat_options = ttk.Combobox(self, values=["Beef - Well","Beef - MidWell","Beef - MidRare","Beef - Rare", "Pork", "Chicken"])
        self.meat_options.pack()

        self.meat_options.set("Meat")

        self.weight_label = tk.Label(self, text="Weight (g)")
        self.weight_label.pack()

        self.meat_entry = tk.Entry(self)
        self.meat_entry.pack()

        self.temp_label = tk.Label(self, text="Temperature (°F)")
        self.temp_label.pack()

        self.temp_entry = tk.Entry(self)
        self.temp_entry.pack()

        self.submit_button = tk.Button(self, text="Submit", command=self.calculate_time)
        self.submit_button.place(x=250, y=100)

        self.start_button = tk.Button(self, text="Start", command=self.start_timer)
        self.start_button.pack()

        self.stop_button = tk.Button(self, text="Stop", command=self.stop_timer)
        self.stop_button.pack()

        self.time = 0
        self.timer_running = False

        timer_font = ("Arial", 44)
        self.timer_label = tk.Label(self, text="00:00:00", font=timer_font, pady= 20)
        self.timer_label.pack()


    def start_timer(self):
        if not self.timer_running:
            self.timer_running = True
            self.update_timer()

    def update_timer(self):
        if self.timer_running:
            if self.time > 0:
                self.time -= 1
                hours = int(self.time) // 3600
                minutes = (int(self.time) % 3600) // 60
                seconds = int(self.time) % 60
                self.timer_label.config(text=f"{hours:02d}:{minutes:02d}:{seconds:02d}")
                self.timer_label.after(1000, self.update_timer)
            else:
                self.timer_running = False
                self.timer_label.config(text="00:00:00")
                self.congratulate()
        else:
            hours = int(self.time) // 3600
            minutes = (int(self.time) % 3600) // 60
            seconds = int(self.time) % 60
            self.timer_label.config(text=f"{hours:02d}:{minutes:02d}:{seconds:02d}")

    def stop_timer(self):
        self.timer_running = False

    def congratulate(self):
        for i in range(3):
            winsound.PlaySound('SystemExclamation', winsound.SND_ALIAS)
        messagebox.showinfo("Time's Up!", "Your meat is ready!")
        

    def calculate_time(self):
        tempV = float(self.temp_entry.get())
        weightV = float(self.meat_entry.get()) / 453.592
        meat = self.meat_options.get()
        tempf = 325 / tempV
        if meat == "Beef - Well":
            self.time = ((weightV * 25) / tempf) * 60
        elif meat == "Beef - MidWell":
            self.time = ((weightV * 22) / tempf) * 60
        elif meat == "Beef - MidRare":
            self.time = ((weightV * 20) / tempf) * 60
        elif meat == "Beef - Rare":
            self.time = ((weightV * 18) / tempf) * 60
        elif meat == "Pork":
            self.time = ((weightV * 30) / tempf) * 60
        elif meat == "Chicken":
            self.time = ((weightV * 25) / tempf) * 60
        self.update_timer()

if __name__ == "__main__":
    app = MeatTimer()
    app.mainloop()