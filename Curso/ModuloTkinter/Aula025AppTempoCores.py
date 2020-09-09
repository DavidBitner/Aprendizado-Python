from tkinter import *
import requests
import json

cidade = qualidade = categoria = app_cor = ""
root = Tk()
root.title("Doidera")
root.geometry("400x45+200+200")

try:
    api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=90210&distance=25&API_KEY=E896BA33-D702-43CF-A0E5-8D1F9800E7E5")
    api = json.loads(api_request.content)
    cidade = api[0]["ReportingArea"]
    qualidade = api[0]["AQI"]
    categoria = api[0]["Category"]["Name"]
    if categoria in "Good":
        app_cor = "#0C0"
    elif categoria in "Moderate":
        app_cor = "FFFF00"
    elif categoria in "Unhelthy for Sensitive Groups":
        app_cor = "ff9900"
    elif categoria in "Unhealthy":
        app_cor = "#FF0000"
    elif categoria in "Very Unhealthy":
        app_cor = "#990066"
    elif categoria in "Hazardous":
        app_cor = "#660000"
    root.configure(background=app_cor)
    my_label = Label(root, text=f"{cidade} {qualidade} {categoria}", font=("Helvetica", 20), background=app_cor)
    my_label.pack()
except Exception as e:
    api = "Erro..."

root.mainloop()
