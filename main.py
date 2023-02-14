import random

class Ship():

    def __init__(self):
        x=y=-1
        self.size = 10
        self.map = [["." for _ in range(self.size)] for _ in range(self.size)]
        self.map_cordin = [[[y,x]for x in range(self.size)] for y in range(self.size)]
        self.ship1 = [[x,y],[x,y],[x,y],[x,y]]
        self.ship2 = [[[x,y],[x,y]],[[x,y],[x,y]],[[x,y],[x,y]],[[x,y],[x,y],[x,y]],[[x,y],[x,y],[x,y],[x,y]]]

    def one_ship_placement(self):
        for i in range(len(self.ship1)):
            while self.ship1[i][0] < 0:
                x = random.randint(0, 9)
                y = random.randint(0, 9)
                if self.map[x][y] != "X":
                    self.map[x][y] = 'X'
                    self.ship1[i][0], self.ship1[i][1] = x+1,y+1
                    print(self.ship1[i])

    def ship_placement(self):


    def map_p(self):
        Gamer.map_print(self)




class Gamer():

    def __init__(self):
        '''
        create playing field
        '''
        self.size = 10
        self.radar = [["." for _ in range(self.size)] for _ in range(self.size)]

    def map_print(self):
        print("Map:")
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
        print("Radar:")
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
    b = Ship()
    b.one_ship_placement()
    # print(b.map_cordin)
    # print(b.ship1)
    # print(b.ship2)
    print(b.map_p())
    # a = Gamer()
    # a.map_print()
    # a.radar_print()
