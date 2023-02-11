
class Gamer():

    def __init__(self):
        '''
        create playing field
        '''
        self.size = 10
        self.map = [["." for _ in range(self.size)] for _ in range(self.size)]
        self.radar = [["." for _ in range(self.size)] for _ in range(self.size)]

    def map_print(self):
        for x in range(-1, self.size):
            for y in range(-1, self.size):
                if x == -1 and y == -1:
                    print("  ", end="")
                    continue
                if x == -1 and y >= 0:
                    print(str(y + 1).rjust(2), end=" ")
                    continue
                if x >= 0 and y == -1:
                    print(("A", "B", "C", "D", "E", "F", "G", "H", "I", "J")[x], end=' ')
                    continue
                print(" " + str(self.map[x][y]), end=' ')
            print("")

    def radar_print(self):
        for x in range(-1, self.size):
            for y in range(-1, self.size):
                if x == -1 and y == -1:
                    print("  ", end="")
                    continue
                if x == -1 and y >= 0:
                    print(str(y + 1).rjust(2), end=" ")
                    continue
                if x >= 0 and y == -1:
                    print(("A", "B", "C", "D", "E", "F", "G", "H", "I", "J")[x], end=' ')
                    continue
                print(" " + str(self.radar[x][y]), end=' ')
            print("")

class Game():
    '''
    Controll all actions
    '''

    def change_players(self):
        pass

    def check_status(self):
        pass


if __name__ == "__main__":
    a = Gamer()
    a.map_print()
    print('')
    a.radar_print()
