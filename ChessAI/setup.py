import pygame
import os.path

from pygame.locals import (MOUSEBUTTONDOWN, RLEACCEL, QUIT)

def check_valid(n, m):
    if (n >= 0 and n <= 7) and (m >= 0 and m <= 7):
        return True
    return False

def clean_selected(ar):
    for i in range(8):
        for j in range(8):
            if ar[i][j] == '..' or ar[i][j] == '...':
                ar[i][j] = '  '
            if ar[i][j][:2] == '.w' or ar[i][j][:2] == '.b':
                ar[i][j] = ar[i][j][1:]
                
def king_position(ar, type):
    king = type + 'k'
    for i in range(8):
        for j in range(8):
            if ar[i][j] == king:
                return (i,j)

B = {
        'king': pygame.image.load(os.path.join("img", "black_king.png")),
        'queen': pygame.image.load(os.path.join("img", "black_queen.png")),
        'rook': pygame.image.load(os.path.join("img", "black_rook.png")),
        'bishop': pygame.image.load(os.path.join("img", "black_bishop.png")),
        'knight': pygame.image.load(os.path.join("img", "black_knight.png")),
        'pawn': pygame.image.load(os.path.join("img", "black_pawn.png")),
    }

W = {
        'king': pygame.image.load(os.path.join("img", "white_king.png")),
        'queen': pygame.image.load(os.path.join("img", "white_queen.png")),
        'rook': pygame.image.load(os.path.join("img", "white_rook.png")),
        'bishop': pygame.image.load(os.path.join("img", "white_bishop.png")),
        'knight': pygame.image.load(os.path.join("img", "white_knight.png")),
        'pawn': pygame.image.load(os.path.join("img", "white_pawn.png")),
    }

Score_WK = [
    [-3,-4,-4,-5,-5,-4,-4,-3],
    [-3,-4,-4,-5,-5,-4,-4,-3],
    [-3,-4,-4,-5,-5,-4,-4,-3],
    [-3,-4,-4,-5,-5,-4,-4,-3],
    [-2,-3,-3,-4,-4,-3,-3,-2],
    [-1,-2,-2,-2,-2,-2,-2,-1],
    [ 2, 2, 0, 0, 0, 0, 2, 2],
    [ 2, 3, 1, 0, 0, 1, 3, 2]
]
Score_WQ = [
    [  -2,  -1,  -1,-0.5,-0.5,  -1,  -1,  -2],
    [  -1,   0,   0,   0,   0,   0,   0,  -1],
    [  -1,   0, 0.5, 0.5, 0.5, 0.5,   0,  -1],
    [-0.5,   0, 0.5, 0.5, 0.5, 0.5,   0,-0.5],
    [   0,   0, 0.5, 0.5, 0.5, 0.5,   0,-0.5],
    [  -1, 0.5, 0.5, 0.5, 0.5, 0.5,   0,  -1],
    [  -1,   0, 0.5,   0,   0,   0,   0,  -1],
    [  -2,  -1,  -1,-0.5,-0.5,  -1,  -1,  -2]
]
Score_WR = [
    [   0,   0,   0,   0,   0,   0,   0,   0],
    [ 0.5,   1,   1,   1,   1,   1,   1, 0.5],
    [-0.5,   0,   0,   0,   0,   0,   0,-0.5],
    [-0.5,   0,   0,   0,   0,   0,   0,-0.5],
    [-0.5,   0,   0,   0,   0,   0,   0,-0.5],
    [-0.5,   0,   0,   0,   0,   0,   0,-0.5],
    [-0.5,   0,   0,   0,   0,   0,   0,-0.5],
    [   0,   0,   0, 0.5, 0.5,   0,   0,   0]
]
Score_WN = [
    [  -5,  -4,  -3,  -3,  -3,  -3,  -4,  -5],
    [  -4,  -2,   0,   0,   0,   0,  -2,  -4],
    [  -3,   0,   1, 1.5, 1.5,   1,   0,  -3],
    [  -3, 0.5, 1.5,   2,   2, 1.5, 0.5,  -3],
    [  -3,   0, 1.5,   2,   2, 1.5,   0,  -3],
    [  -3, 0.5,   1, 1.5, 1.5,   1, 0.5,  -3],
    [  -4,  -2,   0, 0.5, 0.5,   0,  -2,  -4],
    [  -5,  -4,  -3,  -3,  -3,  -3,  -4,  -5]
]
Score_WP = [
    [   0,   0,   0,   0,   0,   0,   0,   0],
    [   5,   5,   5,   5,   5,   5,   5,   5],
    [   1,   1,   2,   3,   3,   2,   1,   1],
    [ 0.5, 0.5,   1, 2.5, 2.5,   1, 0.5, 0.5],
    [   0,   0,   0,   2,   2,   0,   0,   0],
    [ 0.5,-0.5,  -1,   0,   0,  -1,-0.5, 0.5],
    [ 0.5,   1,   1,  -2,  -2,   1,   1, 0.5],
    [   0,   0,   0,   0,   0,   0,   0,   0]
]
Score_WB = [
    [  -2,  -1,  -1,  -1,  -1,  -1,  -1,  -2],
    [  -1,   0,   0,   0,   0,   0,   0,  -1],
    [  -1,   0, 0.5,   1,   1, 0.5,   0,  -1],
    [  -1, 0.5, 0.5,   1,   1, 0.5, 0.5,  -1],
    [  -1,   0,   1,   1,   1,   1,   0,  -1],
    [  -1,   1,   1,   1,   1,   1,   1,  -1],
    [  -1, 0.5,   0,   0,   0,   0, 0.5,  -1],
    [  -2,  -1,  -1,  -1,  -1,  -1,  -1,  -2]
]
Score_BK = [
    [ 2, 3, 1, 0, 0, 1, 3, 2],
    [ 2, 2, 0, 0, 0, 0, 2, 2],
    [-1,-2,-2,-2,-2,-2,-2,-1],
    [-2,-3,-3,-4,-4,-3,-3,-2],
    [-3,-4,-4,-5,-5,-4,-4,-3],
    [-3,-4,-4,-5,-5,-4,-4,-3],
    [-3,-4,-4,-5,-5,-4,-4,-3],
    [-3,-4,-4,-5,-5,-4,-4,-3]
]
Score_BQ = [
    [  -2,  -1,  -1,-0.5,-0.5,  -1,  -1,  -2],
    [  -1,   0, 0,   0,   0,   0.5,   0,  -1],
    [  -1, 0, 0.5, 0.5, 0.5, 0.5,   0.5,  -1],
    [   -0.5,   0, 0.5, 0.5, 0.5, 0.5,   0,0],
    [-0.5,   0, 0.5, 0.5, 0.5, 0.5,   0,-0.5],
    [  -1,   0, 0.5, 0.5, 0.5, 0.5,   0,  -1],
    [  -1,   0,   0,   0,   0,   0,   0,  -1],
    [  -2,  -1,  -1,-0.5,-0.5,  -1,  -1,  -2]
]
Score_BR = [
    [ 0, 0, 0, 0.5, 0.5, 0, 0, 0],
    [ -0.5, 0, 0, 0, 0, 0, 0, -0.5],
    [ -0.5, 0, 0, 0, 0, 0, 0, -0.5],
    [ -0.5, 0, 0, 0, 0, 0, 0, -0.5],
    [ -0.5, 0, 0, 0, 0, 0, 0, -0.5],
    [ -0.5, 0, 0, 0, 0, 0, 0, -0.5],
    [ 0.5, 1, 1, 1, 1, 1, 1, 0.5],
    [ 0, 0, 0, 0, 0, 0, 0, 0],
]
Score_BN = [
    [ -5, -4, -3, -3, -3, -3, -4, -5],
    [ -4, -2, 0, 0.5, 0.5, 0, -2, -4],
    [ -3, 0.5, 1, 1.5, 1.5, 1, 0.5, -3],
    [ -3, 0, 1.5, 2, 2, 1.5, 0,-3],
    [ -3, 0.5, 1.5, 2, 2, 1.5, 0.5, -3],
    [ -3, 0, 1, 1.5, 1.5, 1, 0, -3],
    [ -4, -2, 0, 0, 0, 0, -2, -4],
    [ -5, -4, -3, -3, -3, -3, -4, -5]
]
Score_BP = [
    [ 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0.5, 1, 1, -2, -2, 1, 1, 0.5],
    [ 0.5, -0.5, -1, 0, 0,-1, -0.5, 0.5],
    [ 0, 0, 0, 2, 2, 0, 0, 0],
    [ 0.5, 0.5, 1, 2.5, 2.5, 1, 0.5, 0.5],
    [ 1, 1, 2, 3, 3, 2, 1, 1],
    [ 5, 5, 5, 5, 5, 5, 5, 5],
    [ 0, 0, 0, 0, 0, 0, 0, 0]
]
Score_BB = [
    [ -2, -1, -1, -1, -1, -1, -1, -2],
    [ -1, 0.5, 0, 0, 0, 0, 0.5, -1],
    [ -1, 1, 1, 1, 1, 1, 1, -1],
    [ -1, 0, 1, 1, 1, 1, 0, -1],
    [ -1, 0.5, 0.5, 1, 1, 0.5, 0.5, -1],
    [ -1, 0, 0.5, 1, 1, 0.5, 0, -1],
    [ -1, 0, 0, 0, 0, 0, 0, -1],
    [ -2, -1, -1, -1, -1, -1, -1, -2],
]

Score = {
    'wk': Score_WK,
    'wq': Score_WQ,
    'wr': Score_WR,
    'wb': Score_WB,
    'wn': Score_WN,
    'wp': Score_WP,

    'bk': Score_BK,
    'bq': Score_BQ,
    'br': Score_BR,
    'bb': Score_BB,
    'bn': Score_BN,
    'bp': Score_BP,
}


