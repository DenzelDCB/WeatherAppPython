import tkinter as tk
from tkinter import scrolledtext
from getWeather import getHourlyWeather

def display_weather():
    global weather_data
    weather_data = getHourlyWeather()
    display_text(weather_data)

def display_text(text):
    text_area.config(state="normal")  
    text_area.delete(1.0, tk.END)
    text_area.insert(tk.END, text) 
    text_area.config(state="disabled")

def search_by_date():
    if not weather_data:
        display_text("No weather data available. Please click the button to get the weather.")
        return

    search_date = search_entry.get().strip()
    if not search_date:
        display_text("Please enter a valid date (e.g., 2025-05-07).")
        return

    search_date = search_date.replace(' ', '-')
    search_date = search_date.replace('--', '-')

    filtered_data = "\n".join(
        line for line in weather_data.split("\n") if search_date in line
    )
    if filtered_data:
        display_text(filtered_data)
    else:
        display_text(f"No data found for the date: {search_date}")

def displayhelp_text():
    global label_warn

    if not label_warn:
        label_warn = tk.Label(
        root,
        text=" To get started, click the dark green button with the text 'Get Weather' to get Temperature (F), and Weather for 15 days and all 24-hour weather and temperature in each day. \nSome data may also change. \n\nData Distinguishing: Hour 00:00 is normally 12:00 AM, but it is the beginning of the next day, so that is why it is at the top. \n\nSearch Bar Help: You can only search for days starting from the current day till 15 days after. \nAdding the hour data will not be used since all hours are just 24 and can easily fit. \n\n\n Click the above button again to close this text."
            )
        label_warn.pack(pady=10)
    else:
        label_warn.destroy()
        label_warn = None

root = tk.Tk()
root.title("Weather Data - Badagry")

weather_data = "" 

fetch_button = tk.Button(root, text="Get Weather", command=display_weather, bg="darkgreen", fg="white")
fetch_button.pack(pady=10)

search_frame = tk.Frame(root)
search_frame.pack(pady=10)

search_label = tk.Label(search_frame, text="Search by Date (YYYY-MM-DD):")
search_label.pack(side=tk.LEFT, padx=5)

search_entry = tk.Entry(search_frame, width=15)
search_entry.pack(side=tk.LEFT, padx=5)

search_button = tk.Button(search_frame, text="Search", command=search_by_date, bg="darkblue", fg="white")
search_button.pack(side=tk.LEFT, padx=5)

text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=80, height=20, state="disabled")
text_area.pack(padx=10, pady=10)

get_directions = tk.Button(root, text="Get Navigation Help", command=displayhelp_text, bg="darkgreen", fg="white")
get_directions.pack(padx=10)

label_warn = None

root.mainloop()
