# PY1010 Arbeidskrav 2
# Maria Andriana Dalen, MAD
# 2025-01-12


# %% Oppgave 1

# Program som regner ut hvor gammel du er i 2024

# I år er årstallet
år = 2024

# Spør om fødselsår
alder = int(input("Hvilket år er du født? "))
 
# Regn ut alderen i 2024
alder_2024 = år - alder

print(f"Du blir {alder_2024} år i 2024.")



# %% Oppgave 2

# Program som regner ut hvor mange pizzaer du  må kjøpe til en klassefest

import numpy as np

# Anta at hver elev spiser 1/4 pizza = antall elever / 4, evt antall elever * 1/4

# Skriv inn antall elever
antall_elever = int(input("Skriv inn antall elever: "))

# Beregn antall pizzaer som trengs, og avrund opp til nærmeste heltall
antall_pizzaer = int(np.ceil(antall_elever / 4))  # Ved å bruke int() får vi et heltall istedenfor et desimaltall

print(f"Det må handles inn {antall_pizzaer} pizzaer til festen.")



# %% Oppgave 3

import numpy as np

def fun_grader_til_radianer(v_grad):
    """Program som regner om fra grader til radianer.
    
    Her bruker vi np.pi for pi.
    """
    v_rad = v_grad * np.pi / 180
    return v_rad

# Be brukeren om å skrive inn gradetallet
v_grad = float(input("Skriv inn gradtallet: "))  # float fordi dette kan væære et desimaltall

v_rad = fun_grader_til_radianer(v_grad)  # Utargument

print(f"Radianen til {v_grad} grader er {v_rad}")
 


# %% Oppgave 4 - Denne oppgaven er delt inn i a), b) og c)

# 4 a) Opprett en dictionary basert på gitt data i oppgaveteksten

data = {
        "Norge": ["Oslo", 0.634],
        "England": ["London", 8.982],
        "Frankrike": ["Paris", 2.161],
        "Italia": ["Roma", 2.873]
        }

# 4 b) Lag et program som ber brukeren skrive inn et land, hvor programmet skriver ut hovedstaden og antall innbyggere

hent_land = input("Skriv inn et land: ")
(hovedstad, befolkning) = data[hent_land]  # Tuppel for å returnere flere verdier fra dictionaryen
print(f"{hovedstad} er hovedstaden i {hent_land} og det er {befolkning} mill. innbyggere i {hovedstad}")

# 4 c) Skriv inn nye land med tilhørende hovedstad og befolkningstall

nytt_land = input("Skriv inn et nytt land: ")
hovedstad = input(f"Skriv inn hovedstaden i {nytt_land}: ")
befolkning = input(f"Skriv inn befolkningstallet i {hovedstad} (i millioner): ")
data[nytt_land] = [hovedstad, befolkning]  # Legger inn ny data i dictionary

# Sjekk at den nye infoen ble lagt til
print(data)



# %% Oppgave 5

import numpy as np

def fun_figur (a, b):
    """Beregning av areal og ytre omkrets av en figur
    bestående av en rettvinklet trekant og en halvsirkel.
    
    Her bruker vi np.pi for pi og np.sqrt for kvadratrot.
    """
    # Areal
    radius = a / 2  # Diamater av halvsirkelen / 2
    areal_trekant = (a * b) / 2
    areal_halvsirkel = (np.pi * radius ** 2) / 2
    totalt_areal = areal_trekant + areal_halvsirkel
    
    # Omkrets
    hypotenus = np.sqrt(a**2 + b**2)
    omkrets_halvsirkel = (2 * np.pi * radius) / 2  # Dette utgjør lengden på sirkelbuen (halvsirkelen). Hadde vi ikke delt på 2, hadde vi fått omkretsen av en hel sirkel
    ytre_omkrets = b + hypotenus + omkrets_halvsirkel
    return totalt_areal, ytre_omkrets
    

# Bruker skriver inn verdiene av a og b
a = float(input("Oppgi lengden av a: "))  # foat fordi dette kan være et desimaltall
b = float(input("Oppgi lengden av b: "))

(areal, omkrets) = fun_figur(a, b)  # Utargument med tuppel for å returnere flere verdier
print(f"Ytre omkrets av figuren = {omkrets} og arealet = {areal}") 



# %% Oppgave 6

# Plotting av funksjonen 𝑓(𝑥) = −𝑥2 − 5, for x på intervallet [-10,10]

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 200)  # Definerer x-verdiene jevnt fordelt mellom -10 - 10, splittet opp i 200 intervaller
y = -x**2 - 5  # f(x)

plt.plot (x, y)
plt.title("Plot av funksjonen f(x) = −x^2 − 5")  # Tittel på plottet
plt.xlabel("x-akse")  # Navn på x-aksen
plt.ylabel("y-akse f(x)")  # Navn på y-aksen
plt.grid(True)  # Slår på rutenett
plt.show()  # Viser plottet på skjerm
