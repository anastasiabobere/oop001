import requests

response = requests.get("https://restcountries.com/v3.1/all")

if response.status_code != 200:
    raise Exception(f"Failed to fetch data. Status code: {response.status_code}")

data = response.json()

print("Visu valstu nosaukumi:")
for country in data:
    print(country["name"]["common"])

print(f"\nKopējais valstu skaits: {len(data)}")

total_population = sum(country.get("population", 0) for country in data)
average_population = total_population / len(data)
print(f"\nVidējais iedzīvotāju skaits: {average_population:.2f}")

max_population = 0
country_with_max_population = ""

for country in data:
    population = country.get("population", 0)
    if population > max_population:
        max_population = population
        country_with_max_population = country["name"]["common"]

print(f"\nValsts ar vislielāko iedzīvotāju skaitu: {country_with_max_population} ({max_population} iedzīvotāji)")

total_area = sum(country.get("area", 0) for country in data)
print(f"\nKopējā platība: {total_area:.2f} km²")

for country in data:
    if country["name"]["common"] == "Latvia":
        print(f"\nLatvijas apakšreģions: {country.get('subregion', 'Nav datu')}")

        borders = country.get("borders", [])
        print(f"Latvijas robežvalstu kodi: {', '.join(borders)}")
        break