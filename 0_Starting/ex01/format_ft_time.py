import time
import datetime

# obtenir l'heure actuelle
timestamp = time.time()

# Decimale = 4 chiffres apres la virgule et separateur de milliers
# Notation scientifique = 2 decimales
print(f"Seconds since January 1, 1970: {timestamp:,.4f} or {timestamp:.2e} in scientific notation")

print(datetime.datetime.now().strftime("%b %d %Y"))
# %b = abreviation du mois, August -> Aug
# %d = ajout du 0 si besoin exemple pour le 6 aout = 06
# %Y = annees avec 4 chiffres
