import os
import requests

WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")

def get_weather():
    url = f"http://api.weatherstack.com/current?access_key={WEATHER_API_KEY}&query=Islamabad"
    response = requests.get(url)
    data = response.json()

    if "current" not in data:
        raise Exception(f"❌ API error: {data.get('error', {}).get('info', 'Unknown error')}")

    temp = data["current"]["temperature"]
    description = data["current"]["weather_descriptions"][0]
    return f"📍 Weather in Islamabad today: **{temp}°C**, {description}"

def send_to_discord(message):
    res = requests.post(WEBHOOK_URL, json={"content": message})
    if res.status_code == 204:
        print("✅ Message sent to Discord!")
    else:
        print(f"❌ Discord send failed: {res.status_code}")

if __name__ == "__main__":
    msg = get_weather()
    send_to_discord(msg)
