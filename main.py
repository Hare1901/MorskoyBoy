import random

class Gamer():

    def __init__(self):
        '''
        create playing field
        '''
        x, y = -1, -1
        self.ship1 = [[x, y], [x, y], [x, y], [x, y]]
        self.ship2 = [[[x, y], [x, y]], [[x, y], [x, y]], [[x, y], [x, y]], [[x, y], [x, y], [x, y]],[[x, y], [x, y], [x, y], [x, y]]]
        self.size = 10
        self.map = [["." for _ in range(self.size)] for _ in range(self.size)]
        self.radar = [["." for _ in range(self.size)] for _ in range(self.size)]

    def chek_around_ship(self, x, y, *args):
        '''
        проверка на возможность занять точку палубой коробля
        :return: true/false
        '''
        all_empty_coordinate = [[i,j] for i in [x-1, x, x+1] for j in [y-1, y, y+1] if self.map[i][j] != '0']
        if len(all_empty_coordinate) == 9 and self.map[x][y] not in all_empty_coordinate:
            print(all_empty_coordinate)
            print(True)
            return True
        else:
            print(False)
            return False


    def one_ship_placement(self):
        for i in range(len(self.ship1)):
            while self.ship1[i][0] < 0:
                x = random.randint(1, 8)
                y = random.randint(1, 8)
                #print("Вв")
                #x, y = int(input()), int(input())
                if self.chek_around_ship(x, y):
                    self.map[y][x] = '0'
                    self.ship1[i][0], self.ship1[i][1] = x, y
                    print(self.ship1[i])
                else:
                    print(False)
                    continue

    def map_print(self):
        print("Map:")
        for x in range(-1, self.size):
            for y in range(-1, self.size):
                if x == -1 and y == -1:
                    print("  ", end="")
                    continue
                if x == -1 and y >= 0:
                    print(str(y).rjust(2), end=" ")
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
    b = Gamer()
    b.one_ship_placement()
    b.map_print()
    # print(b.map_cordin)
    # print(b.ship1)
    # print(b.ship2)
    # a = Gamer()
    # a.map_print()
    # a.radar_print()
