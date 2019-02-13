import chess.uci

class EngineStorage():
    engineDefault = chess.uci.popen_engine("C:/Users\joelg\Desktop\stockfish_10_x64.exe")
    engineKomodo = chess.uci.popen_engine("C:/Users\joelg\Desktop\komodo-9.02-64bit") 
    engineFire = chess.uci.popen_engine("C:/Users\joelg\Desktop\Fire_7.1_x64")

    def engineActivate(self, x):
        try:
            if x == 0:
                engineDefault = chess.uci.popen_engine("C:/Users\joelg\Desktop\stockfish_10_x64.exe")
                engineDefault.uci()
                print('Chess engine implemented:')
                print (engineDefault.author)
                print (engineDefault.name)
            elif x == 1:
                engineKomodo = chess.uci.popen_engine("C:/Users\joelg\Desktop\komodo-9.02-64bit") 
                engineKomodo.uci
                print('Chess engine implemented:')
                print (engineKomodo.author)
                print (engineKomodo.name) 
            elif x == 2:
                engineFire = chess.uci.popen_engine("C:/Users\joelg\Desktop\Fire_7.1_x64")
                engineFire.uci()
                print('Chess engine implemented:')
                print (engineFire.author)
                print (engineFire.name)
        except(IOError):
            print('File cannot be located, try again.')
        except(NameError):
            print('engine not defined')

    def readEngineMove(self, tuple_pos):
        teachmover_position = tuple_pos
        pos = ''.join(map(str, teachmover_position[0:1]))
        return pos
    
    def test():
        print('hello')

    def test2():
        x = 1
        y = 2
        z = x + y
        print(z)