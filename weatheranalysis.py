days = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")

weather = {
    "Kochi": {
        "temp": [31, 32, 30, 29, 31, 33, 32],
        "rain": [0, 5, 12, 20, 0, 0, 3]

    },
     "Munnar": {
        "temp": [18, 19, 17, 16, 18, 20, 19],
        "rain": [2, 8, 15, 25, 5, 0, 4]
    },
    "Palakkad": {
        "temp": [36, 37, 38, -999, 37, 39, 38],
        "rain": [0, 0, 0, 0, 0, 0, 0]
    },
    "Kozhikode": {
        "temp": [30, 31, 30, 29, 30, 32, 31],
        "rain": [0, 10, 8, 18, 2, 0, 1]
    }
}


def clean(values):
  result=[]
  for val in values:
    if val >= -50:
        result.append(val)
  return result

print("SENSOR CHECK")
print("-" * 30)
for city in sorted(weather):
    check_invalid= len(weather[city]["temp"])
    after_clean = len(clean(weather[city]["temp"]))
    invalid = check_invalid-after_clean
print(f"{city:<10}{invalid} invalid reading(s)")


def average(values):
    avg=sum(values) / len(values)
    return avg
print("")
print("WEEKLY SUMMARY")
print(f"print{'City':<10}{'Avg':>7}{'Max':>6}{'Min':>6}{'Rain':>7}{'Rainy':>7}")

for city in sorted(weather):
    temps = clean(weather[city]["temp"])
    rain = weather[city]["rain"]
    avg_temp = average(temps)
    highest = max(temps)
    lowest = min(temps)
    total_rain = sum(rain)
    rainy_days = sum(1 for amount in rain if amount > 0)
print(f"{city:<10}{avg_temp:>7.1f}{highest:>6}{lowest:>6}{total_rain:>7}{rainy_days:>7}"
    )

def day_type(temp, hot=35, warm=28):
    if temp >= hot:
        return "Hot"
    elif temp >= warm:
        return "Warm"
    else:
        return "Cool"


print()
print("DAY TYPES")
print(
    f"{'City':<10}{'Hot':>5}"
    f"{'Warm':>6}{'Cool':>6}"
)

for city in sorted(weather):
    temps = clean(weather[city]["temp"])
    counts = {}

    for temp in temps:
        label = day_type(temp)
        counts[label] = counts.get(label, 0) + 1

    print(
        f"{city:<10}{counts.get('Hot', 0):>5}"
        f"{counts.get('Warm', 0):>6}"
        f"{counts.get('Cool', 0):>6}"
    )


def city_averages(weather):
    averages = {}

    for city in weather:
        temps = clean(weather[city]["temp"])
        averages[city] = average(temps)

    return averages

def extremes(averages):
    hot = ""
    cool = ""

    for city in averages:
        if hot == "" or averages[city] > averages[hot]:
            hot = city

        if cool == "" or averages[city] < averages[cool]:
            cool = city

    return hot, cool



averages = city_averages(weather)
hot, cool = extremes(averages)

print(f"Hottest city: {hot} ({averages[hot]:.1f})")
print(f"Coolest city: {cool} ({averages[cool]:.1f})")


daily_rain = {}


for index, day in enumerate(days):
    total = 0

    for city in weather:
        total += weather[city]["rain"][index]

    daily_rain[day] = total


print()
print("RAINFALL BY DAY")

for day in days:
    print(f"{day:<5}{daily_rain[day]:>4} mm")


wet_day = days[0]

for day in days:
    if daily_rain[day] > daily_rain[wet_day]:
        wet_day = day

print(f"Wettest day: {wet_day} ({daily_rain[wet_day]} mm)")
daily_rain[day]=total
for index, day in enumerate(days):
    total = 0
for city in weather:
        total += weather[city]["rain"][index]
        daily_rain[day] = total
print()
print("RAINFALL BY DAY")
for day in days:
  print(f"{day:<5}{daily_rain[day]:>4} mm")
  
wet_day = days[0]
most_rain=-1
for day in daily_rain:
    if daily_rain[day] > most_rain:
      most_rain=daily_rain[day]
      wet_day = day

print(f"Wetday: {wet_day}{daily_rain[wet_day]} mm)")


def heavy_rain(day_index, limit=20):
    alerts = []

    for city in weather:
        amount = weather[city]["rain"][day_index]

        if amount >= limit:
            alerts.append((city, amount))
            alerts.sort()

        return alerts



print()
print("RAIN ALERTS (20 mm or more)")

for i, day in enumerate(days):
    alerts = heavy_rain(i, limit=10)

    if alerts:
        details = ", ".join(
            f"{city} {amount} mm"
            for city, amount in alerts
        )
        print(f"{day}: {details}")
