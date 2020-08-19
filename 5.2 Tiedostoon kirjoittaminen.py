tiedosto_nimi = input("Minkäniminen tiedosto luodaan?: ")
uusi_teksti = input("Mitä kirjoitetaan tiedostoon?: ")

tiedosto = open(tiedosto_nimi, "w")
tiedosto.write(uusi_teksti)
print("Luotiin tiedosto", tiedosto_nimi, "ja siihen tallennettiin teksti:", uusi_teksti)
tiedosto.close()
