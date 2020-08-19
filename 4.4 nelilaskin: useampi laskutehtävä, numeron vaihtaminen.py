kahvi1 = 0
kahvi2 = int(input("Anna ensimmäinen luku: "))
kahvi3 = int(input("Anna toinen luku: "))

while kahvi1 != 6:
  print("(1) +\n(2) -\n(3) *\n(4) /\n(5)Vaihda luvut\n(6)Lopeta")
  print("Valitut luvut:", kahvi2, kahvi3)
  kahvi1 = int(input("Tee valinta (1-6): "))
  if kahvi1 == 1:
	  print("Tulos on:", kahvi2+kahvi3)
  elif kahvi1 == 2:
	  print("Tulos on:", kahvi2-kahvi3)
  elif kahvi1 == 3:
	  print("Tulos on:", kahvi2*kahvi3)
  elif kahvi1 == 4:
	  print("Tulos on:", kahvi2/kahvi3)
  elif kahvi1 == 5:
    kahvi2 = int(input("Anna uusi ensimmäinen luku: "))
    kahvi3 = int(input("Anna uusi toinen luku: "))
  elif kahvi1 == 6:
	  break
