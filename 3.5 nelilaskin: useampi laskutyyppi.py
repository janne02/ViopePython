a = int(input("Anna ensimmäinen luku: "))
b = int(input("Anna toinen luku: "))
c = int(input("(1) +\n(2) -\n(3) *\n(4) /\nTee valinta (1-4): "))

if c == 1:
	print("Tulos on:", a+b)
elif c == 2:
	print("Tulos on:", a-b)
elif c == 3:
	print("Tulos on:", a*b)
elif c == 4:
	print("Tulos on:", a/b)
else:
	print("Valintaa ei tunnistettu.")
