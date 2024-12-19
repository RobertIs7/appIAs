import tkinter as tk
from tkinter import messagebox
import time

class SleepMonitorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Monitorizarea Somnului")
        self.root.geometry("400x700")
        self.root.config(bg="#E1F5FE")

        self.sleep_history = []

        self.title_label = tk.Label(self.root, text="Monitorizarea Somnului", font=("Arial", 16, "bold"), bg="#E1F5FE")
        self.title_label.pack(pady=30)

        self.start_time_label = tk.Label(self.root, text="Ora de început:", font=("Arial", 12), bg="#E1F5FE")
        self.start_time_label.pack(pady=10)
        self.start_time_entry = tk.Entry(self.root, font=("Arial", 14), width=25, borderwidth=2)
        self.start_time_entry.pack(pady=10)

        self.stop_time_label = tk.Label(self.root, text="Ora de oprire:", font=("Arial", 12), bg="#E1F5FE")
        self.stop_time_label.pack(pady=10)
        self.stop_time_entry = tk.Entry(self.root, font=("Arial", 14), width=25, borderwidth=2)
        self.stop_time_entry.pack(pady=10)

        self.save_button = tk.Button(self.root, text="Salvează Somnul", command=self.save_sleep, font=("Arial", 14), bg="#FF7043", fg="white", width=20, height=2)  # Font mai mare
        self.save_button.pack(pady=20)

        self.suggestions_button = tk.Button(self.root, text="Sugestii pentru Somn", command=self.show_general_suggestions, font=("Arial", 14), bg="#29B6F6", fg="white", width=20, height=2)  # Font mai mare
        self.suggestions_button.pack(pady=10)

        self.history_button = tk.Button(self.root, text="Istoric Somn", command=self.show_history, font=("Arial", 14), bg="#AB47BC", fg="white", width=20, height=2)  # Font mai mare
        self.history_button.pack(pady=10)

    def save_sleep(self):
        start_time = self.start_time_entry.get()
        stop_time = self.stop_time_entry.get()

        if not start_time or not stop_time:
            messagebox.showinfo("Eroare", "Trebuie să introduceți atât ora de început cât și ora de oprire.")
            return

        try:
            start_time_obj = time.strptime(start_time, "%H:%M")
            stop_time_obj = time.strptime(stop_time, "%H:%M")

            start_minutes = start_time_obj.tm_hour * 60 + start_time_obj.tm_min
            stop_minutes = stop_time_obj.tm_hour * 60 + stop_time_obj.tm_min

            if stop_minutes < start_minutes:
                stop_minutes += 24 * 60

            sleep_duration = stop_minutes - start_minutes
            self.sleep_history.append({
                "start_time": time.strftime('%H:%M', start_time_obj),
                "end_time": time.strftime('%H:%M', stop_time_obj),
                "duration": sleep_duration
            })
            messagebox.showinfo("Succes", f"Somnul a fost salvat! Durata somnului: {sleep_duration} minute.")
        except ValueError:
            messagebox.showinfo("Eroare", "Te rog introduceti o ora valabilă în formatul HH:MM.")

    def show_general_suggestions(self):
        suggestions = (
            "1. Pastreaza un program regulat de somn, mergand la culcare si trezindu-te in fiecare zi la aceeasi ora.\n"
            "2. Evita consumul de cafeina si alimente grele cu cateva ore inainte de somn.\n"
            "3. Creeaza o atmosfera linistita in dormitor: asigura-te ca este intunecat si linistit.\n"
            "4. Foloseste tehnici de relaxare, precum meditatia sau citirea unei carti inainte de somn.\n"
            "5. Incearca sa dormi intre 7 si 9 ore pe noapte pentru a te simti odihnit."
        )
        messagebox.showinfo("Sugestii pentru Somn", suggestions)

    def show_history(self):
        if not self.sleep_history:
            messagebox.showinfo("Istoric", "Nu exista date de somn inregistrate.")
        else:
            history_str = ""
            for entry in self.sleep_history:
                history_str += f"Inceput: {entry['start_time']} | Sfarsit: {entry['end_time']} | Durata: {entry['duration']} min\n"
            messagebox.showinfo("Istoric Somn", history_str)

if __name__ == "__main__":
    root = tk.Tk()
    app = SleepMonitorApp(root)
    root.mainloop()
