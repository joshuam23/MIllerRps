import random 

symbols = ['rock', 'paper', 'scissors',]

player_wins = 0
computer_wins = 0
while player_wins < 3 and computer_wins < 3:
    player_symbol = none
    while player_symbol is None:
        input_symbol = raw_input("/nwhat symbol would you like to play? ")
        if input_symbol in symbols:
            player_symbol = input_symbol
        else:
            print "/nPlease pick from these symbols: rock, paper, scissors"
            
computer_symbol = random.choice(symbols)

print
print 'player: ', player_symbol
print 'computer: ', computer_symbol
print

if player_symbol == computer_symbol
    print "tie"
elif player_symbol == 'rock':
    if computer_symbol == 'paper':
        print 'computer wins'
        computer_wins += 1
    else:
        print 'player wins'
        player_wins += 1
elif player_symbol == 'paper':
    if computer_symbol == 'scissors':
        print 'computer wins'
        computer_wins += 1
    else:
        print 'player wins'
        player_wins += 1
else:
    if computer_symbol == 'rock':
        print 'computer wins
        computer_wins += 1
    else:
        print 'player wins'
        player_wins += 1

print
print "player wins: ", player_wins
print"computer wins: ", computer_wins
print
        
