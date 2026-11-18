crops_info = {
    ("black", "kharif"): {
        "crops": ["Cotton", "Soyabean", "Jowar", "Tur (Pigeon Pea)"],
        "water": "Medium",
        "temp": (21, 35),
    },
    ("alluvial", "rabi"): {
        "crops": ["Wheat", "Barley", "Gram"],
        "water": "Medium",
        "temp": (10, 25),
    },
}


def crop_recommendation_system(soil, water, season, temp):
  key = (soil.lower().strip(), season.lower().strip())

  if key in crops_info:
    info = crops_info[key]

    print(f"\nRecommended Crops: {', '.join(info['crops'])}")

    # Water compatibility check
    if water.lower().strip() == "low" and info["water"].lower() == "high":
      print("Warning: These crops need more water.")
    else:
      print(f"Water compatibility: Good (Required: {info['water']})")

    mintemp, maxtemp = info["temp"]
    if mintemp <= temp <= maxtemp:
      print(
          f"Temperature Compatibility: Good! ({temp}°C is within the ideal"
          f" range {mintemp}-{maxtemp}°C)"
      )
    else:
      print(
          f"This {temp}°C is outside the ideal range ({mintemp}-{maxtemp}°C)."
      )
  else:
    print("\nNo exact match found for that soil and season combination.")
    print("Tip: Try combinations like 'Black' + 'Kharif' or 'Alluvial' + 'Rabi'.")


def main():
  print("=== Smart Crop Recommendation System ===")
  soil_input = input("Enter soil type (Black / Alluvial / Red / Sandy): ")
  season_input = input("Enter season (Kharif / Rabi / Zaid): ")
  water_input = input("Enter water availability (Low / Medium / High): ")

  try:
    temp_input = float(input("Enter average temperature in °C: "))
    
    crop_recommendation_system(
        soil_input, water_input, season_input, temp_input
    )
  except ValueError:
    print("Invalid input! Please enter a numeric value for temperature.")


if __name__ == "__main__":
  main()
