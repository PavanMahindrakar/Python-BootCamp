import requests

r = requests.get('https://github.com/PavanMahindrakar/Python-Bootcamp')

# print(r.text)

with open("github.txt", "w") as file:
    file.write(r.text)