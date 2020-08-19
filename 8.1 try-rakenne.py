def getnumber():
    try:
        num=int(input("Anna luku: "))
        print("Syöte oli kelvollinen.")
    except Exception:
        print("Virheellinen syöte!")

def main():
    getnumber()

if __name__=="__main__":
    main()
