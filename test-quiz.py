score = 0
score = int(score)

print('Hello fellas, whats your name')
nom = input('Your name here: ')

print('Hello ' + nom +' lets begin the quiz')
print('\n')

#Question 1
print('''A.What s last name of Diogo (Click enter, then type 1 or 2): 
1. Obama
2. Heinen''')

response1 = input('Your answer is: ')

if (response1 == "2" or response1 == "Heinen"):
    print('Good answer mate')
    score = score +1
    print('\n')
   
else:
     print('Not the good answer')
     print('\n')
    
#Question 2
print('''It s Johnson :
1. 6.00
2. 5.30
3. 6.30''')

response2 = input('Your answer is: ')

if (response2 == "3" or response2 == "6.30"):
    print('Good answer mate')
    score = score +1
    print('\n')
    
else:
    print('Not the good answer')
    print('\n')
    
#Question 3
print('''In the Simpsons, what s the first name of the grand father :
1. Abraham
2. Abram
3. Braham''')

response3 = input('Your answer is: ')

if (response3 == "1" or response3 == "Abraham"):
    print('Good answer mate')
    score = score +1
    print('\n')
    
else:
    print('Not the good answer')
    print('\n')

#Question 4
print('''Which ones are IDE? :
1. Visual Studio Code
2. Read my code
3. Sublime''')

response4 = input('Your answer is: ')


        # !! A RéSOUDRE : FAIRE EN SORTE DE POUVOIR SéLECTIONER LA RéPONSE PAR LE CHIFFRE(INT) CORRESPONDANT OU BIEN EN ECRIVANT LA RéPONSE(STR) !!

        
if ((response4 == "1 3" or response4 == "3 1") or (response4 == "Visual Studio Code Sublime" or response4 == "Sublime Visual Studio Code") ):
    print('Good answer mate')
    score = score +1
    print('\n')
    
else:
    print('Not the good answer')
    print('\n')

#Question 5
print('it s raining cats and ... (what word is missing ?) ')

response5 = input('Your answer is: ')

if (response5 == "dogs"):
    print('Good answer mate')
    score = score +1
    print('\n')
else:
    print('Good answer mate')
    score = score +1
    print('\n')

# print(nom +", your total score is "+score+ "/5").format(score)

totalScore = str(score)
print(nom+" your score is "+totalScore+"/5")

