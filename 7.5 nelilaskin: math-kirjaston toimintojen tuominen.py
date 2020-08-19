import math

luku1=input("Anna ensimmäinen luku: ")
luku2=input("Anna toinen luku: ")
luku1=int(luku1) 
luku2=int(luku2) 
while True:
    print("(1) +\n(2) -\n(3) *\n(4) /\n(5)sin(luku1/luku2)\
\n(6)cos(luku1/luku2)\n(7)Vaihda luvut\n(8)Lopeta")
    print("Valitut luvut:",luku1,luku2)
    op=input("Tee valinta (1-8):")
    if op=="1":
        result=luku1+luku2
        print("Tulos on:",result)
    elif op=="2":
        result=luku1-luku2
        print("Tulos on:",result)
    elif op=="3":
        result=luku1*luku2
        print("Tulos on:",result)
    elif op=="4":
        result=luku1/luku2
        print("Tulos on:",result)
    elif op=="5":
        result=math.sin(luku1/luku2)
        print("Tulos on:",result)
    elif op=="6":
        result=math.cos(luku1/luku2)
        print("Tulos on:",result)
    elif op=="7":
        luku1=int(input("Anna uusi ensimmäinen luku: "))
        luku2=int(input("Anna uusi toinen luku: "))
    elif op=="8":
        break
    else:
        print("Yritä uudelleen.")
