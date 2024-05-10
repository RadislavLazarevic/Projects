import random
colors = ["white", "black", "red", "green", "blue", "yellow", "purple", "grey"]

while True:
    color = colors[random.randint(0,len(colors)-1)]
    guess = input("Ja mislim o boji, mozes li pogoditi koja je: ")

    while True:
        if (color == guess.lower()):
            break
        else:
            guess = input("Ne. Pokusajte ponovo: ")
        
    print("Pogodili ste! Mislio sam o", color)

    play_again = input ("Ajmo igrati ponovo? Uneiste 'ne' da odustanete.")

    if play_again.lower() == "ne":
        break

print("Bilo je zabavno, hvala na igranju")
