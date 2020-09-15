from tkinter import *
import mysql.connector

root = Tk()
root.title("Doidera")
root.geometry("400x400+200+200")

my_db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="YourPassword",
    database="doidera"
)

# Criar um cursor e inicializa-lo
my_cursor = my_db.cursor()

# Criar tabela
my_cursor.execute("CREATE TABLE clientes("
                  "first_name VARCHAR(255), "
                  "last_name VARCHAR(255), "
                  "zipcode INT(10), "
                  "price_paid DECIMAL(10, 2), "
                  "user_id INT AUTO_INCREMENT PRIMARY KEY)")

root.mainloop()
