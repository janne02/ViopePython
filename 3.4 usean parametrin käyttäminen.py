malmin = int(input("Anna luku: "))
kartano = int(input("Anna toinen luku: "))

if malmin%2 == 0 and kartano%2 == 0:
	print("Molemmat luvut ovat parillisia.")
elif malmin%2 != 0 and kartano%2 != 0:
	print("Molemmat luvut ovat parittomia.")
else:
	print("Toinen luku on parillinen.")
