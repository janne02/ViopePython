import random

def voitto():
    print("Voitit!")
    result = 1
    return result

def havio():
    print("Hävisit!")
    result = 3
    return result

def valinta_funktio(pelaaja, tietokone):
    print("Sinä valitsit:", pelaaja)
    print("Tietokone valitsi:", tietokone)

def peli(pelaaja):
    peli=random.randint(1,3)
    if peli == 1:
        tietokone="Jalka"
    elif peli == 2:
        tietokone="Ydinase"
    elif peli == 3:
        tietokone="Torakka"

    if (tietokone==pelaaja) and (tietokone != "Ydinase"):
        valinta_funktio(pelaaja, tietokone)
        print("Tasapeli!")
        result = 2
        return result
    elif (tietokone==pelaaja) and (tietokone == "Ydinase"):
        valinta_funktio(pelaaja, tietokone)
        print("Tasapeli!")
        result = 2
        return result
    elif pelaaja == "Jalka":
        valinta_funktio(pelaaja, tietokone)
        if peli == 2:
            return havio()
        elif peli == 3:
            return voitto()
    elif pelaaja == "Ydinase":
        valinta_funktio(pelaaja, tietokone)
        if peli == 1:
            return voitto()
        elif peli == 3:
            return havio()
    elif pelaaja == "Torakka":
        valinta_funktio(pelaaja, tietokone)
        if peli == 1:
            return havio()
        elif peli == 2:
            return voitto()
    else:
        print("Incorrect selection.")
        return 4
    
def main():
    rounds = 0
    wonrounds = 0
    tierounds = 0
    while True:
        pelaaja=input("Jalka, Ydinase vai Torakka? (Lopeta lopettaa):")
        if pelaaja == "Lopeta":
            print("Pelasit", rounds, "kierrosta, joista voitit", wonrounds,"ja pelasit tasan", tierounds, "peliä.")
            break
        else:
            result = peli(pelaaja)
            if result == 1:
                rounds += 1
                wonrounds += 1
            elif result == 2:
                rounds += 1
                tierounds += 1
            elif result == 3:
                rounds += 1

if __name__=="__main__":
    main()
