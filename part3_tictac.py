board = [''] * 9


game_running = True
player = 1
while game_running:
    
    print(board[0:3])
    print(board[3:6])
    print(board[6:9])
    ind = int(input('please write your index'))
    if ind <=8 and ind >=0:
        if board[ind] == '':
            if player ==1:
                board[ind] = 'X'
                player = 2
                print('player 2 turn')
            elif player ==2:
                board[ind] = 'O'
                player = 1
                print('player 1 turn')
        else:
            print('sorry it is already take')
    else:
        print('wrong number choose between 1 to 9 and integer')
                
    