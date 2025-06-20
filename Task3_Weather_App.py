import tkinter as tk
from tkinter import messagebox
import requests

API_KEY = "1d8304cd3ace4f19aac162651251606"

def get_weather():
    city = city_entry.get().strip()
    if not city:
        messagebox.showwarning("Input Error", "Please enter a city name.")
        return

    url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}"

    try:
        response = requests.get(url)
        data = response.json()

        if "error" in data:
            messagebox.showerror("Error", data["error"]["message"])
            return

        location = data["location"]["name"]
        country = data["location"]["country"]
        temp_c = data["current"]["temp_c"]
        condition = data["current"]["condition"]["text"]
        humidity = data["current"]["humidity"]
        wind_kph = data["current"]["wind_kph"]

        result = (
            f"Location: {location}, {country}\n"
            f"Condition: {condition}\n"
            f"Temperature: {temp_c}°C\n"
            f"Humidity: {humidity}%\n"
            f"Wind: {wind_kph} kph"
        )
        weather_result.config(text=result)

    except Exception as e:
        messagebox.showerror("Error", f"Could not retrieve weather data:\n{e}")

# GUI Setup
app = tk.Tk()
app.title("Weather App")
app.geometry("320x280")
app.resizable(False, False)

# Title
tk.Label(app, text="Weather Checker", font=("Arial", 16, "bold")).pack(pady=10)

# City Input
city_entry = tk.Entry(app, font=("Arial", 14), justify='center')
city_entry.pack(pady=5)
city_entry.insert(0, "Enter City")

# Button
tk.Button(app, text="Get Weather", command=get_weather, font=("Arial", 12)).pack(pady=10)

# Result Display
weather_result = tk.Label(app, text="", font=("Arial", 12), justify="center")
weather_result.pack(pady=10)

# Run App
app.mainloop()
