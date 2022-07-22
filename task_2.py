import requests

url = "https://ru.wikipedia.org/w/api.php"
params = {
    "action": "query",
    "cmtitle": "Категория:Животные_по_алфавиту",
    "cmlimit": 500,
    "list": "categorymembers",
    "format": "json",
}
letters = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
total = {}
run = True

# It takes about 20 seconds to get all the pages

while run:
    with requests.get(url=url, params=params) as resp:
        data = resp.json()
        animals_list = data["query"]["categorymembers"]

        for record in animals_list:
            animal = record["title"]
            first_letter = animal[0]

            if first_letter == "A":
                run = False
                break
            if first_letter in letters:
                if total.get(first_letter):
                    total[first_letter] += 1
                else:
                    total[first_letter] = 1
    params["cmcontinue"] = data["continue"]["cmcontinue"]

for letter in letters:
    if total.get(letter):
        print(f"{letter}: {total[letter]}")
