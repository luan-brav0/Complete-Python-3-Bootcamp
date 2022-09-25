import random


def main():

    def display_board(board):
        '''Assumes list board
        prints board in 3 rows'''
        print(board[6:])
        print(board[3:6])
        print(board[:3])

    def choose_marker(marker):
        while marker not in ['X', 'O']:
            marker = input('Choose your marker: [X/O] : ').upper()
        return marker

  
    def rand_first():
        '''Return int either equal to 1 or 2. 
        Randomly pics a player'''
        return random.randint(1,2)

    def coin_toss(marker):
        coin = ''
        while coin not in ['H', 'T']:
            coin = input('Heads or tails? [H/T] : ').upper()
        if rand_first() != 1 and coin == 'H':
            marker = switch_players(marker)
            coin = 'T' if coin == 'H' else 'H'
            print('Coin : {}'.format(coin))
            print("Player {} goes first.".format(marker))
        else: 
            print('Coin : {}'.format(coin))
            print("Player {} goes first.".format(marker))
        return marker

    # def space_check(board, position):
    #     '''Assumes a list board and an int position
    #     Returns Boolean
    #     Checks if position in board is an available space.'''
    #     return board[position - 1] == position

    def full_board_check(board):
        full = True
        for i in '123456789':
            if int(i) in  board:
                full = False
                break
        if full: 
            print('  -----  DRAW!  -----  ')
        return True

    def player_choice(board, marker):
        '''Assumes a list board.
        Returns an int played.
        Asks user to input a interger'''
        played = 0
        while played not in board:
            try:
                played = int(input('player {} : '.format(marker)))
            except:
                continue
        return played

    def place_marker(board, marker, position):
        board[position - 1] = marker if board[position - 1] == position else position
        return board

    def replay():
        return True if input('  ?? Play again? [Y/N] : ').upper() == 'Y' else False

    def switch_players(marker):
        return 'X' if marker == 'O' else 'O'   

    def win_check(board): 
        '''Assumes a list board  and a string mark
      Return Boolean
      Checks for wins in (lower row) or (mid row) or (upper row) or (down diagonal) or (up diagonal)'''
        return (board[0] == board[1] == board [2]) or (board[3] == board[4] == board[5]) or (board[6] == board[7] == board[8])  or (board[0] == board[3] == board[6]) or (board[1] == board[4] == board[7]) or (board[2] == board[5] == board[8]) or(board[6] == board[4] == board[2]) or (board[0] == board[4] == board[8])
        
         


# ------------------ end of functions

    print('Welcome to Tic Tac Toe!')

    def game_on():
        board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        marker = ''
        position = 0
        while True:
            display_board(board)
            marker = choose_marker(marker)
            marker = coin_toss(marker)
            print('\n'*1)
            while not win_check(board) or not full_board_check(board):
                display_board(board)
                position = player_choice(board, marker)
                board = place_marker(board, marker, position)
                if not win_check(board):
                    marker = switch_players(marker)
                else: 
                    print('  -----  PLAYER "{}" WINS!  -----  '.format(marker))
                print('\n'*1)
            if not replay():
                print("Goodbye!")
                break
            else:
                game_on()
        
    game_on()
main()