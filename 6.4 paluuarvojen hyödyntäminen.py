def main():
	syote = input("Anna syöte (Lopeta lopettaa): ")
	pituus(syote)


def pituus(merkkijono):
	if merkkijono == "Lopeta":
		exit()
	elif len(merkkijono) == 0:
		print("Et antanut syötettä")
		main()
	else:
		print("Antamasi syöte oli",len(merkkijono),"merkkiä pitkä.")
		main()

	
if __name__ == "__main__":
	main()
