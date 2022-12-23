import datetime as dt
import smtplib
import pandas as pd
import random
import os
# planif tache
# Etape 1 : C:\Program Files\Python39\python.exe
#  Etape 2 :main.py
#  Etape 3 :C:\Users\h.coleau\Pictures\birthday
MY_EMAIL = ".com"
PASSWORD = ""
def send_email(name, email):
    random_letter_number = random.randint(1, 3)
    random_letter = f"dossier/letter_{random_letter_number}.txt"
    with open("dossier/letter_1.txt") as file:
        content = file.read()
        content = content.replace("[NAME]", name)
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(MY_EMAIL, PASSWORD)
        connection.sendmail(MY_EMAIL, email, content)      
        
now = dt.datetime.now()
month = now.month
day = now.day
birthday = pd.read_csv('birthday.csv')
fichier = "birthday.csv"
taille = os.path.getsize(fichier)
if taille == 0:
	print("La taille du fichier "+fichier+" est de "+taille)
else:
    print("La taille du fichier "+fichier+" est de ", taille)
    
for index, row in birthday.iterrows():
    print(f"Name={row['name']},Firstname={row['firstname']},Email={row['email']},Day={row['day']},Month={row['month']} ,Year={row['year']}")
    if day == row['day'] and month == row['month']:
        send_email(name=row['name'], email=row['email'])
        print("C'est l'anniversaire de "+row['name']+" "+row['firstname'])
    else:
        print("C pas le bon jour pour l'anniversaire de "+row['name']+" "+row['firstname'])
