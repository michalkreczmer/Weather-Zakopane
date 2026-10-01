import requests
import tkinter as tk

url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": 49.299,
    "longitude": 19.9489,
    "current": ["temperature_2m", "surface_pressure", "wind_speed_10m", "rain", "snowfall", "cloud_cover", "relative_humidity_2m"],
    "hourly": ["temperature_2m", "surface_pressure", "wind_speed_10m", "rain", "snowfall", "cloud_cover", "relative_humidity_2m"],
    "timezone": "Europe/Berlin",
}

odpowiedz = requests.get(url, params=params)
dane = odpowiedz.json()

temperatura = dane["current"]["temperature_2m"]
wiatr = dane["current"]["wind_speed_10m"]
godziny = dane["hourly"]["time"]
predykcje_temp = dane["hourly"]["temperature_2m"]
predykcje_wiatr = dane["hourly"]["wind_speed_10m"]

# print(f"Aktualna temperatura: {temperatura}°C")
# print(f"Prędkość wiatru: {wiatr} km/h")
# # print(f"Przewidywana temperatura: {predykcje}°C")

# for godzina, temp in zip(godziny[:24], predykcje[:24]):
#     print(f"{godzina}: {temp}°C")

okno = tk.Tk()
okno.title("Pogoda")
okno.geometry("600x650")

etykieta_wiatr = tk.Label(okno, text=f"Aktualna temperatura: {temperatura}°C", font=("Arial", 12, "bold"))
etykieta_wiatr.pack(pady=5)
etykieta_wiatr = tk.Label(okno, text=f"Wiatr: {wiatr} km/h", font=("Arial", 12, "bold"))
etykieta_wiatr.pack(pady=5)
etykieta_prognoza = tk.Label(okno, text="Prognoza na cały dzień:", font=("Arial", 10, "bold"))
etykieta_prognoza.pack(pady=(15, 5))

for godzina, temp, wind in zip(godziny[:24], predykcje_temp[:24], predykcje_wiatr[:24]):
    godz = godzina.split("T")[1]
    tk.Label(okno, text=f"{godz}: {temp}°C, {wind} km/h", font=("Arial", 10)).pack()

okno.mainloop()