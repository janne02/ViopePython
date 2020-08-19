def main():
	syote = input("Anna syöte (Lopeta lopettaa): ")
	if len(syote) < 5:
		syote = "Oletustulostus"
		tulostaja(syote)
	elif syote == "Lopeta":
		exit()
	else:
		tulostaja(syote)

def tulostaja(oletustulostus):
	print(oletustulostus)
	main()
	
if __name__ == "__main__":
	main()
