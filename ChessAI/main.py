import pygame
import os.path
import random
from copy import deepcopy
from setup import *
from chessman import *
from AI import *

def equals(a, b):
    if a[0] == b[0] and a[1] == b[1]:
        return True
    return False
                
def check_position(pos, min1, max1, min2, max2):
    if pos[0] >= min1 and pos[0] <= max1 and pos[1] >= min2 and pos[1] <= max2:
        return True
    return False

class Board():
    def __init__(self, screen):
        self.screen = screen
        self.color = (0, 0, 0)

    def draw_board(self, C):
        pygame.draw.rect(self.screen, C, (0, 0, 500, 50))
        pygame.draw.rect(self.screen, C, (0, 0, 50, 500))
        pygame.draw.rect(self.screen, C, (450, 0, 50, 500))
        pygame.draw.rect(self.screen, C, (0, 450, 450, 50))
        for y in range(8):
            for x in range(8):
                if (x + y) % 2 == 0:
                    self.color = (255, 255, 255)
                else:
                    self.color = (47, 182, 47)
                pygame.draw.rect(self.screen, self.color,(50*(x+1), 50*(y+1), 50, 50))

class Game():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((500, 500))
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("comicsansms", 35)
        self.font2 = pygame.font.SysFont("comicsansms", 72)
        board = Board(self.screen)
        chessman = Pieces(self.screen)
        cmate = -1
        option = self.Menu()
        if option == 1:
            cmate = self.play_game(board, chessman)
        if cmate == -1:
            pygame.quit()
            return
        self.Game_Over(board, chessman, cmate)
        pygame.quit()

    def Menu(self):
        self.screen.fill((47, 182, 47))
        txt = self.font2.render("Play", True, (255, 255, 255))
        txt_center = (250 - txt.get_width() // 2, 250 - txt.get_height() // 2)
        option = -1
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pressed()[0]:
                        pos_clicked = pygame.mouse.get_pos()
                        if check_position(pos_clicked,250-txt.get_width()//2,250+txt.get_width()//2,250-txt.get_height()//2,250+txt.get_height()//2):
                            option = 1
                            running = False
                if event.type == QUIT:
                    running = False           
            self.screen.fill((47, 182, 47))
            self.screen.blit(txt, txt_center)
            pygame.display.flip()
            self.clock.tick(30)
        return option

    def play_game(self, board, chessman):
        cplayer = ['w', 'b']
        C = [(0,0,0), (0,0,0)]
        player, cl, st, cmate = 0, -1, [], -1
        last_pos = ()
        AI = AI_Minimax(chessman.ar, chessman)
        AI_random = AI_rand(chessman.ar, chessman)
        running = True
        while running:
            pos_clicked = ()
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                if event.type == MOUSEBUTTONDOWN:
                    if player == 0 and pygame.mouse.get_pressed()[0]:
                        pos = pygame.mouse.get_pos()
                        pos_clicked = (pos[1] // 50, pos[0] // 50)
                        cl += 1
                        if not chessman.precond(pos_clicked, player) and cl == 0:
                            cl -= 1
                            continue
            if player == 0:
                if pos_clicked != () and not check_valid(pos_clicked[0]-1, pos_clicked[1]-1):
                    cl -= 1
                    continue
                if pos_clicked != () and cl == 0:
                    chessman.selecting(pos_clicked)
                    st.append(pos_clicked)
                if pos_clicked != () and cl == 1:
                    if equals(st[0], pos_clicked):
                        cl -= 1
                        continue
                    if chessman.switch_chessman(st[0], pos_clicked):
                        cl, st = -1, []
                        clean_selected(chessman.ar)
                        continue
                    if not chessman.move(chessman.ar, st[0], pos_clicked):
                        cl -= 1
                        continue
                    last_pos = (st[0], pos_clicked)
                    player, cl, st = 1 - player, -1, []
                    if chessman.is_checked(chessman.ar, cplayer[player]):
                        if chessman.is_checkmate(chessman.ar, cplayer[player]):
                            cmate = 1-player
                            running = False
            else:
                pos = AI.minimax(chessman.ar,chessman,'b',-1000000000,1000000000,3,None,chessman.prev_move)
                if pos[1] == None:
                    p_random = AI_random.find_pos_random(chessman.ar, chessman, 'b')
                    if p_random == None:
                        cmate = 2
                        running = False
                    else:
                        chessman.move(chessman.ar, p_random[0], p_random[1])
                else:
                    chessman.selecting(pos[1])
                    chessman.move(chessman.ar, pos[1], pos[2])
                    last_pos = (pos[1], pos[2])
                    player = 1 - player
                    if chessman.is_checked(chessman.ar, cplayer[player]):
                        if chessman.is_checkmate(chessman.ar, cplayer[player]):
                            cmate = 1-player
                            running = False
            board.draw_board(C[player])
            chessman.draw_chessman_upgrade(last_pos)
            pygame.display.flip()
            self.clock.tick(20)
        return cmate

    def Game_Over(self, board, chessman, cmate):
        if cmate == 2:
            txt = "Tie"
        elif cmate == 1:
            txt = "Computer wins!"
        else:
            txt = "You win!"
        txt = self.font.render(txt, True, (0, 128, 0))
        txt_center = (250 - txt.get_width() // 2, 50//2 - txt.get_height() // 2)
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
            board.draw_board((0,0,0))
            chessman.draw_chessman()
            self.screen.blit(txt, txt_center)
            pygame.display.flip()
            self.clock.tick(30)

if __name__ == '__main__':
    t = Game()
