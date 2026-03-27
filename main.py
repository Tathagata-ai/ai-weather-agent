import requests
import json
import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

# API Keys
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Initialize OpenAI client
client = OpenAI(api_key=OPENAI_API_KEY)

# -----------------------------
# TOOL: Get Weather Data
# -----------------------------
def get_weather_data(city):
    try:
        url = f"https://api.weatherapi.com/v1/current.json?key={WEATHER_API_KEY}&q={city}"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": str(e)}

# -----------------------------
# TOOL: Save Results
# -----------------------------
def save_results(data, filename="weather_data.json"):
    with open(filename, "w") as f:
        json.dump(data, f, indent=2)

# -----------------------------
# LLM: Analyze Weather
# -----------------------------
def analyze_weather_with_llm(city, data):
    if "error" in data:
        return f"⚠️ Error fetching weather: {data['error']}"

    prompt = f"""
You are an intelligent weather assistant.

Weather data for {city}:
{json.dumps(data, indent=2)}

Provide:
- 🌡 Temperature (in °C)
- 🌤 Condition
- 💡 Friendly suggestion (what to wear or do)

Keep it short and clear.
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",  # ✅ FIXED MODEL
        messages=[
            {"role": "system", "content": "You are a smart and friendly weather assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=150
    )

    return response.choices[0].message.content

# -----------------------------
# AGENT: Orchestrator
# -----------------------------
def weather_agent(city):
    print(f"\n🔍 Fetching weather for {city}...\n")

    data = get_weather_data(city)
    save_results(data)

    print("🤖 Analyzing with AI...\n")
    result = analyze_weather_with_llm(city, data)

    return result

# -----------------------------
# MAIN
# -----------------------------
if __name__ == "__main__":
    city = input("Enter city: ").strip()

    result = weather_agent(city)

    print("\n===== 🤖 AI Weather Report =====\n")
    print(result)
    print("\n================================\n")