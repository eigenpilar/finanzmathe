## Beispielrechnung:
x = 5000  # Startkapital
p = 2  # Zinssatz (in Prozent pro Jahr)
y = 300 # monatlicher Abzug

tage_pro_monat = 30
tage_pro_jahr = 360

## Berechnung der Zinsen für den ersten Monat
z1 = x + (x * p / 100 * tage_pro_monat/tage_pro_jahr)

## Berechnung für die folgenden Monate (bis Konto leer)
zinsbetrag_liste = [z1] 

while zinsbetrag_liste[-1] > 0:
    z_vor = zinsbetrag_liste[-1]
    z_neu = (z_vor + (z_vor * p / 100 * tage_pro_monat / tage_pro_jahr)) - y
    zinsbetrag_liste.append(z_neu)

## Anzahl Monate, bis das Konto leer ist und Guthaben am Ende
print("**Monat**:", len(zinsbetrag_liste) - 1)  # Anzahl Monate, bis das Konto leer ist
print("**Kontostand**:", zinsbetrag_liste[-1]) # Endkontostand
print("**alle Kontostände**:", zinsbetrag_liste)


