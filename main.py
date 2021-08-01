#!/usr/bin/env python3
##
## EPITECH PROJECT, 2021
## d
## File description:
## d
##

from random import randint
from os import system
import time

def random_str(n1,n2):
    x = randint(n1,n2)
    return (x)

def random_line(files,n1,n2):
    lines = []
    rand_line = []
    with open(files) as f:
        lines = f.readlines()
        return(lines[random_str(n1,n2)])

def random_cap():
    system("clear")
    i = 0
    c = random_line("geoo.txt",1,197)
    capital = c.split(" ", 1)
    cap = capital[1]
    cap = cap.replace(" ","")
    cap = cap.replace("\n","")
    cap = cap.replace("_"," ")
    guess = input("Quel est la capitale de %s?\n\n: " % (capital[0]))
    if guess == cap or guess == cap.lower():
        print("Bravo tu as trouvé")
        restart = input("Veux tu continuer?\n\n1.Oui\n2.Non\n\n: ")
        if restart == "1" or restart == "Oui":
            system("clear")
            random_cap()
        else:
            print("Bye")
            quit()
    else:
        system("clear")
        print("Raté la capitale était: %s" % (cap))
        restart = input("Veux tu continuer?\n\n1.Oui\n2.Non\n\n: ")
        if restart == "1" or restart == "Oui":
             system("clear")
             random_cap()
        else:
            print("Bye")
            quit()

def continent_cap(continent):
    system("clear")
    i = 0
    if continent == 1:
        c = random_line("asie.txt",1,47)
    if continent == 2:
        c = random_line("afrique.txt",1,54)
    if continent == 3:
        c = random_line("amerique.txt",1,36)
    if continent == 4:
        c = random_line("europe.txt",1,46)
    if continent == 5:
        c = random_line("oceanie.txt",1,15)
    capital = c.split(" ", 1)
    cap = capital[1]
    cap = cap.replace(" ","")
    cap = cap.replace("\n","")
    cap = cap.replace("_"," ")
    guess = input("Quel est la capitale de %s?\n\n: " % (capital[0]))
    if guess == cap or guess == cap.lower():
        print("Bravo tu as trouvé")
        restart = input("Veux tu continuer?\n\n1.Oui\n2.Non\n\n: ")
        if restart == "1" or restart == "Oui":
            system("clear")
            continent_cap(continent)
        else:
            print("Bye")
            quit()
    else:
        system("clear")
        print("Raté la capitale était: %s" % (cap))
        restart = input("Veux tu continuer?\n\n1.Oui\n2.Non\n\n: ")
        if restart == "1" or restart == "Oui":
             system("clear")
             continent_cap(continent)
        else:
            print("Bye")
            quit()

def all_cap(score, cap_nbr):
    system("clear")
    i = 0
    c = random_line("geoo.txt",0 + cap_nbr,0 + cap_nbr)
    capital = c.split(" ", 1)
    cap = capital[1]
    cap = cap.replace(" ","")
    cap = cap.replace("\n","")
    cap = cap.replace("_"," ")
    guess = input("Quel est la capitale de %s?\n\n: " % (capital[0]))
    if cap_nbr == 197:
        print("Bravo tu as fait toutes les capitales!")
        restart = input("Veux tu recomencer?\n\n1.Oui\n2.Non\n\n: ")
        if restart == "1" or restart == "Oui":
            system("clear")
            all_cap(0,0)
        else:
            print("Bye")
            quit()
    if guess == cap or guess == cap.lower():
        score = score + 1
        print("Bravo tu as trouvé")
        print("Ton Score: %d / 197" % (score))
        if cap_nbr < 197:
            restart = input("Veux tu continuer?\n\n1.Oui\n2.Non\n\n: ")
            if restart == "1" or restart == "Oui":
                system("clear")
                all_cap(score, cap_nbr + 1)
            else:
                print("Bye")
                quit()
    else:
        system("clear")
        print("Raté la capitale était: %s" % (cap))
        print("Ton Score: %d / 197" % (score))
        if cap_nbr < 197:
            restart = input("Veux tu continuer?\n\n1.Oui\n2.Non\n\n: ")
            if restart == "1" or restart == "Oui":
                system("clear")
                all_cap(score, cap_nbr + 1)
            else:
                print("Bye")
                quit()

def tweenty_cap(score,goal):
    system("clear")
    i = 0
    c = random_line("geoo.txt",1,197)
    capital = c.split(" ", 1)
    cap = capital[1]
    cap = cap.replace(" ","")
    cap = cap.replace("\n","")
    cap = cap.replace("_"," ")
    guess = input("Quel est la capitale de %s?\n\n: " % (capital[0]))
    if goal == 0:
        print("Finit voici ton score: %d" % (score))
        restart = input("Veux tu recomencer?\n\n1.Oui\n2.Non\n\n: ")
        if restart == "1" or restart == "Oui":
            system("clear")
            tweenty_cap(0,20)
        else:
            print("Bye")
            quit()
    if guess == cap or guess == cap.lower():
        score = score + 1
        goal = goal - 1
        print("Bravo tu as trouvé")
        print("Ton Score: %d / 20 Pays Restant: %d" % (score,goal))
        if goal > -1:
            restart = input("Veux tu continuer?\n\n1.Oui\n2.Non\n\n: ")
            if restart == "1" or restart == "Oui":
                system("clear")
                tweenty_cap(score, goal)
            else:
                print("Bye")
                quit()
    else:
        system("clear")
        goal = goal - 1
        print("Raté la capitale était: %s" % (cap))
        print("Ton Score: %d / 20 Pays Restant: %d" % (score,goal))
        if goal > -1:
            restart = input("Veux tu continuer?\n\n1.Oui\n2.Non\n\n: ")
            if restart == "1" or restart == "Oui":
                system("clear")
                tweenty_cap(score, goal)
            else:
                print("Bye")
                quit()

def three_lives_cap(score, lives):
    system("clear")
    i = 0
    c = random_line("geoo.txt",1,197)
    capital = c.split(" ", 1)
    cap = capital[1]
    cap = cap.replace(" ","")
    cap = cap.replace("\n","")
    cap = cap.replace("_"," ")
    if lives < 1:
        restart = input("Veux tu recomencer?\n\n1.Oui\n2.Non\n\n: ")
        if restart == "1" or restart == "Oui":
            system("clear")
            three_lives_cap(0,3)
        else:
            print("Bye")
            quit()
    guess = input("Quel est la capitale de %s?\n\n: " % (capital[0]))
    if guess == cap or guess == cap.lower():
        score = score + 1
        print("Bravo tu as trouvé")
        print("Ton Score: %d / 100" % (score))
        print("Ton Nombre de vie: %d / 3" % (lives))
        if score > 99:
            restart = input("Tu as gagné veux tu recomencer?\n\n1.Oui\n2.Non\n\n: ")
            if restart == "1" or restart == "Oui":
                system("clear")
                three_lives_cap(0,3)
            else:
                print("Bye")
                quit()
        restart = input("Veux tu continuer?\n\n1.Oui\n2.Non\n\n: ")
        if restart == "1" or restart == "Oui":
            system("clear")
            three_lives_cap(score, lives)
        else:
            print("Bye")
            quit()
    else:
        system("clear")
        lives = lives - 1
        print("Raté la capitale était: %s" % (cap))
        print("Ton Score: %d / 100" % (score))
        print("Ton Nombre de vie: %d / 3" % (lives))
        if lives < 0:
            restart = input("Tu as perdu veux tu recomencer?\n\n1.Oui\n2.Non\n\n: ")
            if restart == "1" or restart == "Oui":
                system("clear")
                three_lives_cap(0,3)
            else:
                print("Bye")
                quit()
        restart = input("Veux tu continuer?\n\n1.Oui\n2.Non\n\n: ")
        if restart == "1" or restart == "Oui":
             system("clear")
             three_lives_cap(score, lives)
        else:
            print("Bye")
            quit()

def print_rule():
    choice = input("Voici les régles:\n\nTu dois deviner la capitale du pays qui est sélectionner.\n\nIl n'y a pas d'accent et les tirets sont remplacer par des espaces exemple: Oulan-Bator donne Oulan Bator.\n\nBon Jeux.\n\nEcrit 1 pour retourner au menu est 0 pour quittez\n\n\n: ")
    if choice == "1":
        menu()
    else:
        print("Bye")
        quit()
def menu():
    system("clear")          
    print("----CAPITALE----")  
    print("    ")          
    print("    ")          
    print("1.Capitale au hasard")       
    print("2.Toutes les capitales")
    print("3.Capitale par continent")     
    print("4.20 Capitals")
    print("5.3 Chances")     
    print("6.Régle")
    print("7.Quittez")
    print("     ")         
    print("      ")        
    choix = input("CHOIX:")
    if choix == "1":    
        random_cap()
    if choix == "2":       
        all_cap(0,0)
    if choix == "3":
        continent_menu()
    if choix == "4":
        #time_cap(11538461,0)
        tweenty_cap(0,20)
    if choix == "5":    
        three_lives_cap(0,3)
    if choix == "6":
        print_rule()
    if choix == "7":
        print("Bye")
        quit()
def continent_menu():
    print("----CHOISI TON CONTINENT----")  
    print("    ")          
    print("    ")          
    print("1.ASIE")       
    print("2.AFRIQUE")
    print("3.AMERIQUE")     
    print("4.EUROPE")
    print("5.OCEANIE")     
    print("6.Quittez")
    print("     ")         
    print("      ")        
    choix = input("CHOIX:")
    if choix == "1":    
        continent_cap(1)
    if choix == "2":       
        continent_cap(2)
    if choix == "3":
        continent_cap(3)
    if choix == "4":       
        continent_cap(4)
    if choix == "5":
        continent_cap(5)
    if choix == "6":
        print("Bye")
        quit()
menu()