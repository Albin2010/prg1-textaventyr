import random
svar1 = (f"slå bollar på rangen")
svar2 = (f"ingen uppvärmining")

namn = input ("Hej spelare nu ska du få följa med John daly på en golftävling och hjälpa honom att göra bra eller dåliga val. Vad heter du?")
print (f"Hej, {namn} . Det första valet du ska göra är vad Jhon ska ha för uppvärmning.")
fråga1 = input ("slå bollar på rangen eller ingen uppvärmining?")
if fråga1 == "slå bollar på rangen":
    print ("dåligt val. Nu behövde john gå upp mycket tidigare som gjorde han trött")
if fråga1 == "ingen uppvärmning":
    print (f"bra val där {namn} nu har john fått sova längre som har gjort han utvillad och peppad på tävling")
if fråga1 == "slå bollar på rangen":
    print ("efter som du gjorde ett dåligt först val och har förstört Johns morgon så kommer han bara ha en chans på 1 av 10 att slå ett bra slag i fairway")


if fråga1 == "slå bollar på rangen":
        siffra_text = input("skriv en siffra mellan 1-10, välj rätt siffra") 
        siffra = int(siffra_text)
        if siffra == 7:
            print ("FAIRWAY TRÄFF!!! det gör att du får par på alla första 17 hål")
        else:
            print ("Missad fairway, detta inebär att du får bogey på alla första 17 hål")
if fråga1 == "ingen uppvärmning":
                print ("nu ska john slå ut på första tee och eftersom du gjorde ett bra första val så har du 6 på 10 chans att träffa Fairway")
                bob_text = input("Skriv en siffra mellan 1-10, välj rätt siffra")
                bob = int(bob_text)
                if bob < 6:
                    print ("FAIRWAY TRÄFF!!! det gör att du får par på alla första 17 hål")
                else:
                    print ("Missad fairway, detta inebär att du får bogey på alla första 17 hål")

                fråga2 = input(f"nu står du på sista hålet och ska slå ut, ska du välja driver eller järn 2?")
if fråga2 == "driver":
    print ("nu slog du jätte nära vattnet och john måste gå dit och slå bollen. När john närmar sig vattnet så rusar en aligator upp från vattnet och attakerar john GAME OVER")
if fråga2 == "järn2":
    print ("du valde det bra valet du lägger dig mitt i fairway och gör en birdie")
if fråga1 == "ingen uppvärmning" and bob < 6 and fråga2 == "järn2":
    print ("John vinner hela tävlingen, Bra jobbat!!!")
if fråga1 == "ingen uppvärmning" and bob > 6 and fråga2 == "järn2":
    print ("John kommer 5a på tävlingen som är helt okej")
if fråga1 == "ingen uppvärmning" and bob == 6 and fråga2 == "järn2":
     print("john kommer 5a på tävlingen som är helt okej")
if fråga1 == "slå bollar på rangen" and siffra > 4 and fråga2 == "järn2":
    print ("Du gjorde många bra val men förmånga dåliga val så du kommer 15e plats")
if fråga1 == "slå bollar på rangen" and siffra < 4 and fråga2 == "järn2":
    print ("John vinner hela tävlingen, Bra jobbat !!!")
if fråga1 == "slå bollar på rangen" and siffra == 4 and fråga2 == "järn2":
     print ("john kommer 2a på tävlingen")

