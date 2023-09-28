# Översätt svensk text till rövarspråket
def oversattillRovarspraket(text):
    vokaler = "AEIOUYÅÄÖaeiouyåäö"  # Lista över vokaler
    översatt_text = ""

    for bokstav in text:
        if bokstav in vokaler:
            översatt_text += bokstav  # Lägg till vokalen oförändrad
        elif bokstav.isalpha():
            översatt_text += bokstav + "o" + bokstav  # Lägg till konsonanten och "o" mellan dem

    return översatt_text

# Läs in svensk text från filen svenskt.text
try:
    with open("svenskt.text", "r", encoding="utf-8") as fil:
        svensk_text = fil.read()
except FileNotFoundError:
    print("Filen 'svenskt.text' hittades inte.")
    exit()

# Översätt svensk text till rövarspråket
rövarspråk_text = oversattillRovarspraket(svensk_text)

# Spara den översatta texten i en ny fil
try:
    with open("oversatt_text.txt", "w", encoding="utf-8") as fil:
        fil.write(rövarspråk_text)
    print("Översättning klar. Den översatta texten har sparats i filen 'oversatt_text.txt'.")
except IOError:
    print("Kunde inte spara den översatta texten.")
