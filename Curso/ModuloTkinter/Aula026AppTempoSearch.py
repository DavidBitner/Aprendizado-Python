from tkinter import *
import requests
import json


def capturar_cep():
    global app_cor
    try:
        api_request = requests.get(
            f"http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode={cep.get()}&distance=25&API_KEY=E896BA33-D702-43CF-A0E5-8D1F9800E7E5")
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
        my_label = Label(root, text=f"{cidade} {qualidade} Air Quality {categoria}", font=("Helvetica", 20),
                         background=app_cor)
        my_label.grid(row=1, column=0, columnspan=2)
    except Exception as e:
        root.configure(background="red")
        my_label = Label(root, text=f"Erro", font=("Helvetica", 20),
                         background="red")
        my_label.grid(row=1, column=0, columnspan=2)


# Main
root = Tk()
root.title("Doidera")
root.geometry("600x100+200+200")

cep = Entry()
cep.grid(row=0, column=0, sticky=W + E + N + S)

cep_btn = Button(root, text="LOOKUP ZIPCODE", command=capturar_cep)
cep_btn.grid(row=0, column=1, sticky=W + E + N + S)

root.mainloop()
