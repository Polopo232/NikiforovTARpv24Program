import json
import requests

import json

andmed = {
    "nimi": "Anna",
    "vanus": 55,
    "abielus": True,
    "kodulomaad": None,
    "autod": [
        {
            "mark": "Toyota",
            "varv": "valge",
            "joud": 200,
            "number": "123ABC"
        },
        {
            "mark": "Peogut",
            "varv": "must",
            "joud": 500,
            "number": "143ABC"
        }
    ]
}

with open("andmed.json", "w") as f:
    json.dump(andmed, f)


sis_nimi = input("Sisesta nimi: ")

if andmed.get("nimi") == sis_nimi:
    print(f"\nAutod kasutajal, {sis_nimi}!")
    for auto in andmed.get("autod", []):
        print(f"- {auto['mark']} ({auto['varv']} {auto['joud']} hj), number: {auto['number']}")







# andmed = {"nimi": "Anna", "vanus": 25, "abielus": False}
# json_string = json.dumps(andmed, indent=2, sort_keys=True)
# print(json_string)

# with open("andmed.json", "w") as f:
#     json.dump(andmed, f)

# with open("andmed.json", "r") as f:
#     andmed_failist = json.load(f)
# print(andmed_failist)

# klass = {
# "opetaja": "Tamm",
# "opilased": [
# {"nimi": "Mari", "hinne": 5},
# {"nimi": "Jüri", "hinne": 4}
# ] }
# with open("klass.json", "w") as f:
#     json.dump(klass, f, indent=2)


linn = input("Sisesta linna nimi: ")
api_voti = "0b49b41ab89f8253f61b7c028d522bb9" # asenda oma API võtmega
url = f"http://api.openweathermap.org/data/2.5/weather?q={linn}&appid={api_voti}&units=metric&lang=et"
vastus = requests.get(url)
andmed = vastus.json()
if andmed.get("cod") != "404" and "main" in andmed and "weather" in andmed:
    peamine = andmed["main"]
    temperatuur = peamine["temp"]
    niiskus = peamine["humidity"]
    kirjeldus = andmed["weather"][0]["description"]
    tuul = andmed["wind"]["speed"]
    print(f"\nIlm linnas {linn}:")
    print(f"Temperatuur: {temperatuur}°C")
    print(f"Kirjeldus: {kirjeldus.capitalize()}")
    print(f"Niiskus: {niiskus}%")
    print(f"Tuule kiirus: {tuul} m/s")
else:
    print("Linna ei leitud. Palun kontrolli nime õigekirja.")

with open("ilm.json", "w", encoding="utf-8") as f:
    json.dump(andmed, f, ensure_ascii=False, indent=4)

