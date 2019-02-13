import chess.uci
import pandas as pd
import openpyxl
from EngineStorage import *
class PyChessVer3():
 
    def main():
        '''creating an instance of the pychess in order to use methods.'''
        # white piece engine
        eng = EngineStorage()
        eng.engineActivate(x=2)
        # black piece engine
        eng2 = EngineStorage()
        eng2.engineActivate(x=0) 
        # tuples to store best moves for each engine
        tuple_pos_white = ()
        tuple_pos_black = ()
        # standard chess board
        board = chess.Board()
        # creating an arraylist for each of the engine's moves
        black_chess_moves = []
        white_chess_moves = []
        quit_game = False
        while not quit_game:
            try:
                board.generate_legal_moves()
                if board.is_checkmate():
                    print('Checkmate, goodbye')
                    print(board.is_game_over)
                    quit()
                if board.is_stalemate():
                    print('Stalemate, goodbye')
                # let the engine know where it is relative to the board
                eng.engineFire.position(board)
                # The default stockfish engine makes its moves first
                tuple_pos_white = tuple(eng.engineFire.go(searchmoves=None, ponder=False, wtime=None, btime=None, winc=None,
                                                binc= None, movestogo=None, depth=4, nodes=None, mate=None,
                                                movetime= 8, infinite=False, async_callback=None))
                engine_white_move = eng.readEngineMove(tuple_pos_white)
                print('white engine ' + engine_white_move + '\n')
                white_chess_moves.append(engine_white_move)
                board.push_uci(engine_white_move)
                # after opponent makes move, the engine must know that it is playing black
                eng2.engineDefault.position(board)
                # The fire engine makes its moves second
                tuple_pos_black = tuple(eng2.engineDefault.go(searchmoves=None, ponder=False, wtime=None, btime=None, winc=None,
                                                binc= None, movestogo=None, depth=4, nodes=None, mate=None,
                                                movetime= 8, infinite=False, async_callback=None))
                engine_black_move = eng2.readEngineMove(tuple_pos_black)
                print ("black engine " + engine_black_move + '\n')
                black_chess_moves.append(engine_black_move)
                board.push_uci(engine_black_move)
                # print the chess board after both engines have made their moves
                print(board)
            except IOError:
                print('error reading file')
            except ValueError:
                print('invalid chess move' + engine_black_move + ' ' + engine_white_move)
                quit()
            finally:
                print(' ')
            '''I need to add the arrays of chess moves into a csv file.'''
            chess_data = {'Fire': white_chess_moves,
                        'Stockfish': black_chess_moves,
            }
            df = pd.DataFrame(chess_data)
            df.to_csv('Engine.csv')

    if __name__ == '__main__':
        main()