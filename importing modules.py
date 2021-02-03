#in this excersie we will impirt vaious modules in our python code and thiswill give us the superpowers to do anything we want to do
# import random 
# for i in range(5):
#     print(random.randint(1, 10))


#import random, sys, os, math
# import random, sys, os, math
# #endign a program using sys.exit()
# while True:
#     print(" program exit karne ke liye ...\"exit\" tpye karen... : ")
#     inp = input()
#     if(inp == "exit"):
#         sys.exit()
#     else:
#         print("konya hoya exit! dobara try kar")

#guess the number game
# import random,sys
# upperlimit = 30
# lowerlimit = 20
# num2 = random.randint(lowerlimit,upperlimit)
# print("bhai ek number guess kar ",lowerlimit," aur ",upperlimit," ke beech ka...")
# while True:
#     num1 = int(input("kar ek number guess.."))
#     if num1<num2:
#         print("Naaa...thoda bada number guess kar ")
#     elif num1>num2:
#         print("Naaa...thoda Chota number guess kar ")
#     elif num1==num2:
#         print("are wahh bete mooj kardi....tham to bhout heavy driver ho! ")
#         sys.exit()

    
#only 5 tries to guess the number
# import random,sys
# upperlimit = 30
# lowerlimit = 20
# tries = 5
# num2 = random.randint(lowerlimit,upperlimit)
# print("bhai ek number guess kar ",lowerlimit," aur ",upperlimit," ke beech ka...")
# for i in range(0,tries):
#     num1 = int(input("kar ek number guess.."))
#     if num1<num2:
#         if(tries-i-1>0):
#             print("Naaa...thoda bada number guess kar ",str(tries-i-1)," try Rahgi!")
#         else:
#             print("lag gi bhai teri too....Try again!")
#     elif num1>num2:
#         if(tries-i-1>0):
#             print("Naaa...thoda Chota number guess kar ",str(tries-i-1)," try Rahgi!")
#         else:
#             print("lag gi bhai teri too....Try again!")
#     elif num1==num2:
#         print("are wahh bete mooj kardi....tham to bhout heavy driver ho! ")
#         sys.exit()


#complex simple rock, paper, scissors game
import random, sys 
print('ROCK, PAPER, SCISSORS') 
wins = 0 
losses = 0 
ties = 0

while True:
    print("%s wins,%s looses,%s ties" %(wins,losses,ties))
    while True:
        print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
        playerMove = input()
        if(playerMove == "q"):
            sys.exit()
        elif(playerMove.lower() == "r" or playerMove.lower() == "p" or playerMove.lower() == "s"):
            break
        else:
            print("bhai \"R\",\"P\" ya \"S\"...inme se koi ek chun..") 

    if playerMove == 'r':
        print('ROCK versus...')
    elif playerMove == 'p':
        print('PAPER versus...')
    elif playerMove == 's':
        print('SCISSORS versus...')

    randomNumber = random.randint(1, 3)
    if randomNumber == 1:
        computerMove = 'r'
        print('ROCK')
    elif randomNumber == 2:
        computerMove = 'p'
        print('PAPER')
    elif randomNumber == 3:
        computerMove = 's'
        print('SCISSORS') 

    # Display and record the win/loss/tie:     
    if playerMove == computerMove:
        print('It is a tie!')
        ties = ties + 1
    elif playerMove == 'r' and computerMove == 's':
        print('You win!')
        wins = wins + 1
    elif playerMove == 'p' and computerMove == 'r':
        print('You win!')
        wins = wins + 1
    elif playerMove == 's' and computerMove == 'p':
        print('You win!')
        wins = wins + 1
    elif playerMove == 'r' and computerMove == 'p':
        print('You lose!')
        losses = losses + 1
    elif playerMove == 'p' and computerMove == 's':
        print('You lose!')
        losses = losses + 1
    elif playerMove == 's' and computerMove == 'r':
        print('You lose!')
        losses = losses + 1
