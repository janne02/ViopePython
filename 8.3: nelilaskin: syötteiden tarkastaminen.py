import math

def getnum():
    while True:
        try:
            num=int(input("Anna luku: "))
            return num
        except Exception:
            print("Virheellinen syöte!")
        
def main():
    num1=getnum()
    num2=getnum()
    num1=int(num1) #type conversion
    num2=int(num2) #type conversion
    while True:
        print("(1) +\n(2) -\n(3) *\n(4) /\n(5)sin(luku1/luku2)\
\n(6)cos(luku1/luku2)\n(7)Vaihda luvut\n(8)Lopeta")
        print("Valitut luvut:",num1,num2)
        op=input("Tee valinta (1-8):")
        if op=="1":
            result=num1+num2
            print("Tulos on:",result)
        elif op=="2":
            result=num1-num2
            print("Tulos on:",result)
        elif op=="3":
            result=num1*num2
            print("Tulos on:",result)
        elif op=="4":
            result=num1/num2
            print("Tulos on:",result)
        elif op=="5":
            result=math.sin(num1/num2)
            print("Tulos on:",result)
        elif op=="6":
            result=math.cos(num1/num2)
            print("Tulos on:",result)
        elif op=="7":
            num1=getnum()
            num2=getnum()
        elif op=="8":
            break
        else:
            print("Yritä uudelleen.")

if __name__=="__main__":
    main()
