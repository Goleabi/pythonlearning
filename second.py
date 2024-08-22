"""
author: Niloofar Barghi
credits: Hadi, Fabian, Johanna, Niloofar
version: version 1.0
maintainer: Niloofar
email: niloofarbarghi8594@gmail.com
<MIT Lizenz>
"""



import random

turns = 12
flag = False
#array_length = len(array)
#print(lst[7])

# name 
#name  = str(input("Choose a name :"))
#print ("Good luck " +name)

# create a list with 3 words 
lst = ["Apfel", "Birne", "Tomate"]

# choose a random word 
ZufallsWort_x= random.choice(lst)
# paltz auswählen 
#zwei_du=lst[1]

lst_length = len(ZufallsWort_x)


#Buchstabe_Random = [] von dem random Wort 
#Buchstaben = []
#Buchstaben[:] = ZufallsWort_x
#print(Buchstaben)

#user_input  = str(input("write a letter: "))

#1-Pro zeile ein kommentar was es tut
#2-jede zeile googlen
#3-jeden fehler googlen
#4-zeile 37-usw. kopieren c/p -> "-" >> print("-")
#5-mein papier 3te schleife.

# Das zeigt, dass die while Schleife bei der ersten Runde 0
# ist und wird jede Runde +1 gemacht so lange die
# "Zahl" kleiner ist als die "Länge von dem Random-Wort" 
# bzw. len(Buchstabe) 
   ####Zahl = 0 
# Die While Schleife wiederholt sich so lange bis
# die "Länge von Buchstabe" größer ist als die "Zahl"
   ####while Zahl < len(Buchstabe):
# Alle Buchstaben von dem Random-Wort werden gezeigt.
    ####print (Buchstabe[Zahl])
# Die "Zahl" wird jede Runde +1
   #### Zahl = Zahl +1
####


# liste für random Wort 
Geheimliste = []

# Für jede Buchstabe von dem zufallswort-x wird ein Strich eingesetzt 
for char in ZufallsWort_x : 
    Geheimliste.append("-")


# 3. leere Liste (user input)
guesses = []


# while Schleife (Lücken)
i = 0 

#while i <= turns:
#user_input  = str(input("write a letter: "))


#while i <= len(Buchstaben):
   # print ("-") 
   # i += 1 
    ########










        #if user_input == Buchstaben [i]:
        #    print (Buchstaben[i])
        #else: 
        #   print ("-")            
    #else: 
        #input != Buchstaben [i]  
    
    #"-" Lücke
    #             [:i]--- füllt bis hier hin auf
    #                                       [i+1:] ab hier wird aufgefüllt
    #Lücke = Lücke[: i] + Buchstabe + Lücke[i + 1:]
  
