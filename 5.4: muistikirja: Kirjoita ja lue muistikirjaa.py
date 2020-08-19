c = 0
while c != 4:
	print("(1) Lue muistikirjaa\n(2) Lisää merkintä\n(3) Tyhjennä muistikirja\n(4) Lopeta")

	c = int(input("Mitä haluat tehdä?: "))

	if c == 1:
		tiedosto = open("muistio.txt", "r")
		print(tiedosto.read())
	elif c == 2:
		tiedosto = open("muistio.txt", "a")
		new = input("Kirjoita uusi merkintä: ")
		tiedosto.write(new)
	elif c == 3:
		tiedosto = open("muistio.txt", "w")
		print("Muistio tyhjennetty.")
	elif c == 4:
		print("Lopetetaan.")
		break
