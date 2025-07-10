import os
import requests

WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
CITY = "Islamabad"
COUNTRY = "PK"

def get_weather():
    url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY},{COUNTRY}&appid={WEATHER_API_KEY}&units=metric"
    response = requests.get(url).json()
    temp = response["main"]["temp"]
    desc = response["weather"][0]["description"].capitalize()
    return f"📍 Weather in {CITY} today: **{temp}°C**, {desc}"

def send_to_discord(message):
    data = {"content": message}
    res = requests.post(WEBHOOK_URL, json=data)
    if res.status_code == 204:
        print("Message sent successfully!")
    else:
        print(f"Failed to send message: {res.status_code}")

if __name__ == "__main__":
    msg = get_weather()
    send_to_discord(msg)
