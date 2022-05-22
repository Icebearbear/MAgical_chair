import pygame 

pygame.mixer.init()
pygame.init()

pg = pygame.mixer

# pg.music.load('piano.mp3')
# song = pg.Sound('guitar.mp3')
# pg.music.play(start= 20 ,loops=-1)
# song.play()

play_guitar()
def play_guitar():
    pg.music.load('guitar.mp3')
    pg.music.play(-1, start)

while pg.music.get_busy():
    print(pg.music.get_pos())
    pygame.time.Clock().tick(10)