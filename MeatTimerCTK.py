import customtkinter as ctk
import winsound

class MeatTimer(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Meat Timer")

        self.resizable(False, False)
        window_width = 400
        window_height = 450

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)

        print(f"{window_width}x{window_height}+{x}+{y}")

        self.geometry(f"{window_width}x{window_height}+{x}+{y}")

        self.create_widgets()

    def create_widgets(self):
        self.meat_label = ctk.CTkLabel(self, text="Choose a Meat")
        self.meat_label.pack(pady=(10, 0))

        self.meat_options = ctk.CTkComboBox(self, values=["Beef - Well", "Beef - MidWell", "Beef - MidRare", "Beef - Rare", "Pork", "Chicken"])
        self.meat_options.pack(pady=(0, 10))
        self.meat_options.set("Meat")

        self.weight_label = ctk.CTkLabel(self, text="Weight (g)")
        self.weight_label.pack(pady=(10, 0))

        self.meat_entry = ctk.CTkEntry(self)
        self.meat_entry.pack(pady=(0, 10))

        self.temp_label = ctk.CTkLabel(self, text="Temperature (°F)")
        self.temp_label.pack(pady=(10, 0))

        self.temp_entry = ctk.CTkEntry(self)
        self.temp_entry.pack(pady=(0, 10))

        self.submit_button = ctk.CTkButton(self, text="Submit", command=self.calculate_time)
        self.submit_button.pack(pady=(10, 0))

        self.start_button = ctk.CTkButton(self, text="Start", command=self.start_timer)
        self.start_button.pack(pady=(10, 0))

        self.stop_button = ctk.CTkButton(self, text="Stop", command=self.stop_timer)
        self.stop_button.pack(pady=(10, 0))

        self.time = 0
        self.timer_running = False

        timer_font = ("Arial", 44)
        self.timer_label = ctk.CTkLabel(self, text="00:00:00", font=timer_font, pady=20)
        self.timer_label.pack(pady=(10, 0))

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
                self.timer_label.configure(text=f"{hours:02d}:{minutes:02d}:{seconds:02d}")
                self.timer_label.after(1000, self.update_timer)
            else:
                self.timer_running = False
                self.timer_label.configure(text="00:00:00")
                self.show_message("Time's Up!", "Your meat is ready!")
        else:
            hours = int(self.time) // 3600
            minutes = (int(self.time) % 3600) // 60
            seconds = int(self.time) % 60
            self.timer_label.configure(text=f"{hours:02d}:{minutes:02d}:{seconds:02d}")

    def stop_timer(self):
        self.timer_running = False

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
        self.update_timer()

    def show_message(self, title, message):
        winsound.PlaySound('SystemExclamation', winsound.SND_ALIAS)
        message_box = ctk.CTkToplevel(self)
        message_box.title(title)
        message_box.geometry("300x150+1080+495")

        message_label = ctk.CTkLabel(message_box, text=message, wraplength=250)
        message_label.pack(pady=20)

        ok_button = ctk.CTkButton(message_box, text="OK", command=message_box.destroy)
        ok_button.pack(pady=10)

if __name__ == "__main__":
    app = MeatTimer()
    app.mainloop()
