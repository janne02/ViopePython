tiedosto = open('merkkijonoja.txt','r')
teksti = tiedosto.readlines()

for i in teksti:
    rivi = i.strip()
    if (rivi.isalnum()):
       print (rivi, 'kelpaa salasanaksi.')
    else:
       print (rivi, 'sisältää virheellisiä merkkejä.')
tiedosto.close()
