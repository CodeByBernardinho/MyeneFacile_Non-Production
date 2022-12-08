import random


class Entry:
    def __init__(self,franc, myene):
        self.franc = franc
        self.myene = myene
    def toString (self):
        return self.franc + " - " + self.myene


fillings = []

def entre():
    while True:
        franc = input("Le mot en francais: ")
        if franc == "#fin":
            return
        myene = input("Le mot en myene:")
        if myene == "#fin":
            return
        fillings.append(Entry(franc, myene))

def question():
    while True:
        p = random.randint(0,len(fillings)-1)
        myene = input("La signification en myene est " +fillings[p].franc +": ")
        if(myene == "#fin"):
            return
        if fillings[p].myene == myene:
            print("Felicitation! Bonne reponse!")
        else:
            print("Mauvais reponse! La bonne reponse est: " +fillings[p].myene)    
            
            
def printall():
    for filling in fillings:
        print(filling.toString)


while True:
    command = input("Bienvenue sur la plattforme MyeneFacile!/n Pour quitter la plattform, tapez: #fin /nVeuillez svp entrez votre commande: ")
    if command == "entre":
        entre()
    elif command == "question":
        question() 
    elif command == "fin":
        fin()    
        break 
    elif command == "sortie":
        printall()
    else:
         print("la commande n'/est pas connu. Veuillez svp les commandes suivantes: entre, question, sortie ou fin")   