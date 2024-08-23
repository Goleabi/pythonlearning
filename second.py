"""
author: Niloofar Barghi
credits: Hadi, Fabian, Johanna, Niloofar
version: version 1.1
maintainer: Niloofar
email: niloofarbarghi8594@gmail.com

<MIT Lizenz>
Copyright (C) [2024] by [Niloofar Barghi]
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without 
l> imitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. 
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

"""

import random

turns = 12
""" flag = False
# array_length = len(array)
# print(lst[7])"""

""" name 
name  = str(input("Choose a name :"))
print ("Good luck " +name) """

# create a list with 3 words 
lst = ["apfel", "birne", "tomate"]

# choose a random word 
ZufallsWort_x= random.choice(lst)
# ZufallsWort_x=lst[2]
# Platz auswählen 
# zwei_du=lst[1]

lst_length = len(ZufallsWort_x)

# Buchstabe_Random = [] von dem random Wort 
# Buchstaben = []
# Buchstaben[:] = ZufallsWort_x
# print(Buchstaben)

# user_input  = str(input("write a letter: "))
# liste für random Wort 
Geheimliste = []

# Für jede Buchstabe von dem zufallswort-x wird ein Strich eingesetzt 
for char in ZufallsWort_x : 
    Geheimliste.append("-")
            
# 3. leere Liste (user input)
guesses = []


i = 0 
while  True: 
    flag = True 

    for i, char in enumerate(ZufallsWort_x):
        if char in guesses: 
            Geheimliste [i] = char    
        else :
            Geheimliste [i] = "-"
        flag = False 

    print (" ".join(Geheimliste))

# Der Buchstabe ist richtig 
    if flag : 
        print ("Great! You won!")
        break

    user_input = input ("Write a letter: ").lower()
    if user_input not in guesses:
        guesses.append(user_input)

    if user_input not in ZufallsWort_x:
        print("Your guess isn't correct. But don't worry! You can try again (:")
  
