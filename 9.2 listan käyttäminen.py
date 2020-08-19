def selection():
    try:
        selection=int(input("Haluatko \n(1)Lisätä listaan \n(2)Poistaa listalta vai\n(3)Lopettaa?:"))
        return selection
    except Exception:
        return "wrong"
        
def secondaction(selection, memo):
    if selection == 1:
        memo.append(input("Mitä lisätään?: "))
    elif selection == 2:
        print("Listalla on", len(memo),"alkiota.")
        target=int(input("Monesko niistä poistetaan?: "))
        try:
            memo.pop(target)
        except Exception:
            print("Virheellinen valinta.")
    elif selection == 3:
        print("Listalla oli tuotteet:")
        for i in memo:
            print(i)
        return "end"
    else:
        print("Virheellinen valinta.")

def main():
    memo = []
    while True:
        if secondaction(selection(), memo) == "end":
            break

if __name__== "__main__":
    main()
