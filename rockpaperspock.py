
#Exercicio 03
while (True):
    player_1 = input("player 1 choice: ")
    if player_1 == 'stop':
      print("game over")
      break
    player_2 = input("player 2 choice: ")
    if player_2 == 'stop':
      print("game over")
      break
    elif player_1 == 'scissors' and (player_2 == 'paper' or player_2 == 'lizard'):
     print ('player 1 wins')
    elif player_1 == 'paper' and (player_2 == 'rock' or player_2 == 'spock'):
      print ('player 1 wins')
    elif player_1 == 'rock' and (player_2 == 'scissors' or player_2 == 'lizard'):
      print('player 1 wins')
    elif player_1 == 'spock' and (player_2 == 'rock' or player_2 == 'scissors'):
     print('player 1 wins')
    elif player_1 == 'lizard' and (player_2 == 'paper' or player_2 == 'spock'):
      print('player 1 wins')
    else:
      print('player 2 wins')