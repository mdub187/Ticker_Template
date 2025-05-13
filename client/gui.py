import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import os
import json
import login


#async loginWindow
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sports Ticker")
        self.geometry("400x400")

        # Create main canvas
        self.main = tk.Canvas(self, height=400, width=400)
        self.main.pack()

        # Create a frame inside the canvas
        self.window = tk.Frame(self.main)
        self.window.pack()
        
        # Creating a Listbox (Dropdown)
        self.listbox = tk.Listbox(self.main)
        self.listbox.insert(1, "American-Football")
        self.listbox.insert(2, "Baseball")
        self.listbox.insert(3, "Basketball")
        self.listbox.insert(4, "Hokey")
        self.listbox.insert(5, "MMA")
        self.listbox.insert(6, "Football")
        self.listbox.pack()

        # Create a text area
        self.text_area = tk.Text(self.main, height=5, width=20)
        self.text_area.pack()

        # add buttons
        # Clear button
        self.clearbtn = tk.Button(self.window, text="Clear", command=self.clear_text)
        self.clearbtn.pack(side=tk.LEFT, padx=0, pady=0)

        # Generate Ticker button
        self.generatebtn = tk.Button(self.window, text="Generate Ticker", command=self.generate_ticker)
        self.generatebtn.pack(side=tk.LEFT, padx=5, pady=5)

        # Search button
        self.searchbtn = tk.Button(self.window, text="Search", command=self.search)
        self.searchbtn.pack(side=tk.LEFT, padx=10, pady=10)

        # Exit button
        self.exitbtn = tk.Button(self.window, text="Exit", command=self.exit_app)
        self.exitbtn.pack(side=tk.LEFT, padx=15, pady=15)
    
    
    def clear_text(self):
        self.text_area.delete(1.0, tk.END)

    def generate_ticker(self):
        # Open and parse the JSON file
        try:
            with open("../api/score/data.json", "r") as file:
                data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            messagebox.showerror("Error", "Failed to load or parse data.json.")
            return

        # Get the selected sport from the Listbox
        selected_sport = self.listbox.get(tk.ACTIVE)
        if not selected_sport:
            messagebox.showinfo("Info", "Please select a sport from the list.")
            return

        # Check if the selected sport exists in the JSON data
        ticker_data = data.get(selected_sport)
        if ticker_data:
            # Display the ticker data in the text area
            self.text_area.delete(1.0, tk.END)
            self.text_area.insert(tk.END, f"{selected_sport} Ticker:\n")
            self.text_area.insert(tk.END, json.dumps(ticker_data, indent=4))
        else:
            self.text_area.delete(1.0, tk.END)
            self.text_area.insert(tk.END, f"No ticker data found for {selected_sport}.")
        # Open and parse the JSON file
        try:
            with open("../api/score/data.json", "r") as file:
                data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            messagebox.showerror("Error", "Failed to load or parse data.json.")
            return

        # Get the selected sport from the Listbox
        selected_sport = self.listbox.get(tk.ACTIVE)
        if not selected_sport:
            messagebox.showinfo("Info", "Please select a sport from the list.")
            return

        # Check if the selected sport exists in the JSON data
        ticker_data = data.get(selected_sport)
        if ticker_data:
            # Display the ticker data in the text area
            self.text_area.delete(1.0, tk.END)
            self.text_area.insert(tk.END, f"{selected_sport} Ticker:\n")
            self.text_area.insert(tk.END, json.dumps(ticker_data, indent=4))
        else:
            self.text_area.delete(1.0, tk.END)
            self.text_area.insert(tk.END, f"No ticker data found for {selected_sport}.")

    def search(self):
        # Open and parse the JSON file
        try:
            with open("../api/score/data.json", "r") as file:
                data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            messagebox.showerror("Error", "Failed to load or parse data.json.")
            return

        # Prompt user for a search query
        query = tk.simpledialog.askstring("Search", "Enter your search query:")
        if not query:
            return

        # Search the JSON data
        results = []
        for key, value in data.items():
            if query.lower() in key.lower() or query.lower() in str(value).lower():
                results.append(f"{key}: {value}")

        # Display results in the text area
        self.text_area.delete(1.0, tk.END)
        if results:
            self.text_area.insert(tk.END, "\n".join(results))
        else:
            self.text_area.insert(tk.END, "No results found.")

    def exit_app(self):
        self.destroy()
        

if __name__ == '__main__':
    app = App()
    app.mainloop()
    print(__name__)


