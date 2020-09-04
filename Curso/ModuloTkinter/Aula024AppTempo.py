from tkinter import *
import requests
import json

cidade = qualidade = categoria = ""
root = Tk()
root.title("Doidera")
root.geometry("400x45+200+200")

try:
    api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=90210&distance=25&API_KEY=E896BA33-D702-43CF-A0E5-8D1F9800E7E5")
    api = json.loads(api_request.content)
    cidade = api[0]["ReportingArea"]
    qualidade = api[0]["AQI"]
    categoria = api[0]["Category"]["Name"]
except Exception as e:
    api = "Erro..."

my_label = Label(root, text=f"{cidade} {qualidade} {categoria}", font=("Helvetica", 20))
my_label.pack()

root.mainloop()
