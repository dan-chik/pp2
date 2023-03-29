import pygame as pg
import os
from pygame import mixer

pg.init()
mixer.init()
screen = pg.display.set_mode((500,500))
pg.display.set_caption("music bank")
run = True
check = True

clock = pg.time.Clock()

bg = pg.transform.scale(pg.image.load('bg.jpg'), (500, 500))


songs = []
path = "c:/Users/Дана/Desktop/gig/" #C:\Users\Дана\Desktop\gig
files = os.listdir(path)
for i in files:
    if i.endswith(".mp3"):
        songs.append(i)

cur = 0
cursong = pg.mixer.music.load(songs[cur])
pg.mixer.music.play()
pg.mixer.music.pause()

font = pg.font.SysFont("arial", 19, True)

while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False


        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                if check:
                    pg.mixer.music.unpause()
                    check = False
                else: 
                    pg.mixer.music.pause()
                    check = True

            if event.key == pg.K_RIGHT:
                pg.mixer.music.stop()
                if cur < 4:
                    cur = cur+1
                else:
                    cur = 0
                pg.mixer.music.load(songs[cur])
                pg.mixer.music.play()
                if check:
                    pg.mixer.music.pause()

            if event.key == pg.K_LEFT:
                pg.mixer.music.stop()
                if cur > 0:
                    cur = cur-1
                else:
                    cur = 4
                pg.mixer.music.load(songs[cur])
                pg.mixer.music.play()
                if check:
                    pg.mixer.music.pause() 

    screen.blit(bg, (0, 0))
    
    songwmp3 = songs[cur]
    songname = songwmp3.replace(".mp3", "")

    text = font.render(songname, True, (100,0,0))
    screen.blit(text, (100,280))
    
    pg.display.flip()
    clock.tick(60)