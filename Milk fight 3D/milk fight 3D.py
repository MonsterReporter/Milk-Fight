from pygame import mixer
mixer.init()
start = mixer.Sound("intro.wav")
start.play(-1)
main = mixer.Sound("main (1).wav")
squirt = mixer.Sound("squirt.wav")
click = mixer.Sound("click.wav")
score = mixer.Sound("score.wav")
hurt = mixer.Sound("hurt.wav")
rip = mixer.Sound("rip.wav")
fill = mixer.Sound("fill.wav")
moo = mixer.Sound("moo.wav")
clap = mixer.Sound("clap (1).wav")
dra = mixer.Sound("dra.wav")
import pgzrun
import time
import random
from random import randint
WIDTH = 1400
HEIGHT = 903
controls = Actor("controls")
controls.pos = 10000, 10000
jackground = Actor("title")
jackground.pos = 700 , 450
background = Actor("title")
background.pos = 700, 450
po1 = Actor("1po")
po1.pos = 300, 700
po2 = Actor("2po")
po2.pos = 300, 800
cookie = Actor("0")
cookie.pos = 440, 500
shadow = Actor("0")
shadow.pos = 440, cookie.y + 200
milk = Actor("0")
milk.pos = 440, 670
switch = 0
cookie_score = 0
x = "na"
walk = False
sec = 1
motion = True
cookie_score = 0
sugar = 3
h = 2
number_of_updates = 0
point = ""
mode = 0
ammo = 5
ammo2 = 5
score2 = 0
angry = False
times = 200
cow_still = True
dirt = Actor("0")
dirt.pos = 700, 250
grass = Actor("0")
grass.pos = 700, 90
stairs = Actor("0")
stairs.pos = 700, 270
stairside1 = Actor("0")
stairside1.pos = 600, 270
stairside2 = Actor("0")
stairside2.pos = 820, 270
bench = Actor("0")
bench.pos = 300, 600
bench_back = Actor("0")
bench_back.pos = bench.pos
bench_seat = Actor("0")
bench_seat.pos = 305, 720
bench_side = Actor("0")
bench_side.pos = 310, 750
bench2 = Actor("0")
bench2.pos = 1100, 600
bench_back2 = Actor("0")
bench_back2.pos = bench2.pos
bench_seat2 = Actor("0")
bench_seat2.pos = 1105, 720
bench_side2 = Actor("0")
bench_side2.pos = 1110, 750
moldy_cookie = Actor("0")
moldy_cookie.pos = 880, 500
benchs = Actor("0")
benchs.pos = bench_seat.pos
benchs2 = Actor("0")
benchs2.pos = bench_seat2.pos
benchl = Actor("0")
benchl.pos = bench_side.pos
benchl2 = Actor("0")
benchl2.pos = bench_side2.pos
shadow2 = Actor("0")
shadow2.pos = 880, moldy_cookie.y + 200
milk2 = Actor("0")
milk2.pos = 880, 600
ammo_sign = Actor("0")
ammo_sign.pos = 150, 50
score_sign = Actor("0")
score_sign.pos = 150, 170
sugar_sign = Actor("0")
sugar_sign.pos = 100, 300
bottle = Actor("0")
bottle.pos = 10000, 10000
cow = Actor("0")
cow.pos = 0, random.randint(360, 900)
ammo_sign2 = Actor("0")
ammo_sign2.pos = 1150, 50
score_sign2 =  Actor("0")
score_sign2.pos = 1050, 220
clok = Actor("0")
clok.pos = 700, 100
con = Actor("con")
con.pos = 150, 400
def lose():
    global switch
    switch = 2
    milk2.x -= 200
    moldy_cookie.x -= 200  
    main.stop()
    jackground.image = "lose"
    rip.play()
def lose2():
    jackground.image = "lose2"
    rip.play()
def lose3():
    jackground.image = "lose3"
    rip.play()
def lose4():
    jackground.image = "lose4"
    rip.play()
def lose5():
    jackground.image = "lose5"
    rip.play()
def lose6():
    jackground.image = "lose6"
    rip.play()
def lose7():
    jackground.image = "lose7"
    rip.play()
    rip.stop()
def lose8():
    jackground.image = "lose8"
def lose9():
    jackground.image = "lose9"
def lose10():
    jackground.image = "lose10"
def lose11():
    jackground.image = "lose11"
def lose12():
    jackground.image = "lose12"
def lose13():
    jackground.image = "lose13"
def lose14():
    global switch
    switch = 1
    jackground.image = "0"
    main.play(-1)
    cow.x = 0
    cow.y = randint(360, 900)
def lose15():
    jackground.image = "lose14"
def lose16():
    global cookie_score, sugar, ammo, ammo2, switch, x, score2
    switch = 0
    jackground.image = "title"
    cookie_score = 0
    score2 = 0
    po1.pos = 300, 700
    po2.x -= 2000
    con.x -= 2000
    sugar = 3
    ammo = 5
    ammo2 = 5
    x = ""
def norm():
    global angry
    moldy_cookie.image = "moldy-cookie-front"
    angry = False
def norm2():
    global angry
    moldy_cookie.image = "moldy-cookie-right"
    angry = False
def norm3():
    global angry
    moldy_cookie.image = "moldy-cookie-left"
    angry = False
def fly():
    global h
    milk2.x -= h
    h += 2
def off():
    global ammo
    milk.image = "0"
    ammo -= 1
    if ammo <= 0:
        click.play()
        ammo = 0
    shadow.image = "0"
def off2():
    global ammo2
    milk2.image = "0"
    ammo2 -= 1
    if ammo2 <= 0:
        click.play()
        ammo2 = 0
    shadow2.image = "0"
def down2():
    shadow2.image = "0"
def down():
    shadow.image = "0"
def left():
    moldy_cookie.image = "moldy-cookie-left"
def right():
    moldy_cookie.image = "moldy-cookie-right"
def up():
    moldy_cookie.image = "moldy-cookie-back"
def timer():
    global times, sec
    times -= 1
    sec += 1
def run():
    global cow_still
    if cow_still:
        cow.image = "cow-left2"
        cow_still = False
    else:
        cow.image = "cow-left"
        cow_still = True
def norm():
    cookie.image = "cookie-front"
def update():
    global x, switch, ammo2, score2, sec, times, walk, number_of_updates, cookie_score, sugar, mode, ammo, point, angry, sugar
    background.draw()
    dirt.draw()
    grass.draw()
    stairs.draw()
    stairside1.draw()
    stairside2.draw()
    bench.draw()
    bench_side.draw()
    bench_seat.draw()
    bench2.draw()
    bench_side2.draw()
    bench_seat2.draw()
    shadow2.draw()
    moldy_cookie.draw()
    shadow.draw()
    milk2.draw()
    cookie.draw()
    milk.draw()
    bench_back.draw()
    cow.draw()
    bench_back2.draw()
    ammo_sign.draw()
    score_sign.draw()
    sugar_sign.draw()
    ammo_sign2.draw()
    score_sign2.draw()
    bottle.draw()
    benchs.draw()
    benchs2.draw()
    benchl.draw()
    benchl2.draw()
    screen.draw.text(str(ammo), color="dark red", topleft=(310, 20), fontsize=148)
    screen.draw.text(str(ammo), color="red", topleft=(300, 20), fontsize=148)
    screen.draw.text(str(cookie_score), color="#C3C318", topleft=(310, 170), fontsize=148)
    screen.draw.text(str(cookie_score), color="yellow", topleft=(300, 170), fontsize=148)
    screen.draw.text(str(sugar), color="#F0E2E2", topleft=(210, 270), fontsize=148)
    screen.draw.text(str(sugar), color="white", topleft=(200, 270), fontsize=148)
    screen.draw.text(str(ammo2), color="dark red", topleft=(1310, 20), fontsize=148)
    screen.draw.text(str(ammo2), color="red", topleft=(1300, 20), fontsize=148)
    screen.draw.text(str(score2), color="#2A751E", topleft=(1250, 250), fontsize=148)
    screen.draw.text(str(score2), color="green", topleft=(1240, 250), fontsize=148)
    clok.draw()
    screen.draw.text(str(times), color="blue", topleft=(620, 50), fontsize=148)
    jackground.draw()
    controls.draw()
    po1.draw()
    po2.draw()
    con.draw()
    if keyboard.left:
        if switch == 1 or 1.5:
            cookie.image = "cookie-left-2"
            cookie.x -= 20
            shadow.x -= 20
            milk.x -= 20
            x = "left"
            if cookie.colliderect(stairs) and cookie.y < 360:
                if cookie.colliderect(stairside1):
                    cookie.x += 20
                    shadow.x += 20
                    milk.x += 20
            if cookie.colliderect(bench):
                if cookie.y < 580:
                    bench_back.image = "bench back"
                else:
                    bench_back.image = "0"
            if cookie.colliderect(bench2):
                if cookie.y < 580:
                    bench_back2.image = "bench back"
                else:
                    bench_back2.image = "0"
            if cookie.x == 400:
                if cookie.colliderect(bench_seat): 
                    if keyboard.left:
                        cookie.x += 20
                        shadow.x += 20
                        milk.x += 20
                    if keyboard.q:
                        cookie.x -= 20
                        shadow.x -= 20
                        milk.x -= 20
            if cookie.x == 1200:
                if cookie.colliderect(bench_seat2): 
                    if keyboard.left:
                        cookie.x += 20
                        shadow.x += 20
                        milk.x += 20
                    if keyboard.q:
                        cookie.x -= 20
                        shadow.x -= 20
                        milk.x -= 20
            if cookie.x < 20:
                cookie.x += 20
                milk.x += 20
                shadow.x += 20
    if not keyboard.left:
        if x == "left":
            cookie.image = "cookie-left"
    if keyboard.right:
        if switch == 1 or 1.5:
            cookie.image = "cookie-right-2"
            cookie.x += 20
            shadow.x += 20
            milk.x += 20
            x = "right"
            if cookie.colliderect(stairs) and cookie.y < 360:
                if cookie.colliderect(stairside2):
                    cookie.x -= 20
                    shadow.x -= 20
                    milk.x -= 20
            if cookie.colliderect(bench):
                if cookie.y < 580:
                    bench_back.image = "bench back"
                else:
                    bench_back.image = "0"
            if cookie.colliderect(bench2):
                if cookie.y < 580:
                    bench_back2.image = "bench back"
                else:
                    bench_back2.image = "0"
            if cookie.x == 200:
                if cookie.colliderect(bench_seat): 
                    if keyboard.right:
                        cookie.x -= 20
                        shadow.x -= 20
                        milk.x -= 20
                    if keyboard.q:
                        cookie.x += 20
                        shadow.x += 20
                        milk.x += 20
            if cookie.x == 1000:
                if cookie.colliderect(bench_seat2): 
                    if keyboard.right:
                        cookie.x -= 20
                        shadow.x -= 20
                        milk.x -= 20
                    if keyboard.q:
                        cookie.x += 20
                        shadow.x += 20
                        milk.x += 20
            if cookie.x > 1380:
                cookie.x -= 20
                milk.x -= 20
                shadow.x -= 20
    if not keyboard.right:
        if x == "right":
            cookie.image = "cookie-right" 
    if keyboard.up:
        if switch == 1 or 1.5:
            cookie.y -= 20
            shadow.y -= 20
            milk.y -= 20
            cookie.image = "cookie-back2"
            x = "back"
        if cookie.y == 360:
            if cookie.colliderect(stairs):
                if cookie.x == 700:
                    height = 2
                    cookie.y += 0
                    shadow.y += 0
                    milk.y += 0
                else:
                    height = 1
                    cookie.y += 20
                    shadow.y += 20
                    milk.y += 20
            else:
                cookie.y += 20
                shadow.y += 20
                milk.y += 20
        if cookie.y < -60:
            cookie.y += 20
            shadow.y += 20
            milk.y += 20
    if cookie.y == 580:
        if cookie.colliderect(bench_seat):
            cookie.y += 20
            milk.y += 20
            shadow.y += 20
    if cookie.y == 680:
        if cookie.colliderect(bench_seat):
            height = 1
            cookie.y += 20
            milk.y += 20
            shadow.y += 20
            if keyboard.q:
                height = 2
                cookie.y -= 20
                milk.y -= 20
                shadow.y -= 20
    if cookie.y == 580:
        if cookie.colliderect(bench_seat2):
            cookie.y += 20
            milk.y += 20
            shadow.y += 20
    if cookie.y == 680:
        if cookie.colliderect(bench_seat2):
            height = 1
            cookie.y += 20
            milk.y += 20
            shadow.y += 20
            if keyboard.q:
                cookie.y -= 20
                milk.y -= 20
                shadow.y -= 20
    if not keyboard.up:
        if x == "back":
            cookie.image = "cookie-back"
    if keyboard.down:
        if switch == 1 or 1.5:
                cookie.y += 20
                shadow.y += 20
                milk.y += 20
                cookie.image = "cookie-front"
                x = "front"
                if cookie.y < 580:
                    bench_back.image = "bench back"
                    bench_back2.image = "bench back"
                else:
                    bench_back.image = "0"
                    bench_back2.image = "0"
                if cookie.y == 540:
                    if cookie.colliderect(bench):
                        cookie.y -= 20
                        milk.y -= 20
                        shadow.y -= 20
                    if cookie.colliderect(bench2):
                        cookie.y -= 20
                        milk.y -= 20
                        shadow.y -= 20
                if cookie.y == 920:
                    cookie.y -= 20
                    shadow.y -= 20
                    milk.y -= 20
    if keyboard.q:
        shadow.y = cookie.y + 100
        if x == "front":
            shadow.image = "shadow"
            clock.schedule(down, 1)
        if x == "back":
            shadow.image = "shadow"
            clock.schedule(down, 1)
        if x == "right":
            shadow.image = "shadow"
            clock.schedule(down, 1)
        if x == "left":
            shadow.image = "shadow"
            clock.schedule(down, 1)
    if keyboard.w:
        if ammo == 0:
            click.play()
            bottle.image = "milk bottle"
            bottle.x = random.randint(20, 1380)
            bottle.y = random.randint(-40, 900)
            if bottle.y > 360:
                if bottle.y < -40:
                    bottle.y = 360
        else:
            milk.x = cookie.x
            if x == "front":
                milk.image = "milk-front2"
                squirt.play()
                clock.schedule(off, 1)
                milk.y = cookie.y + 230
            if x == "back":
                milk.image = "milk-back2"
                squirt.play()
                milk.y = cookie.y - 230
                clock.schedule(off, 1)
            if x == "left":
                milk.image = "milk-right2"
                squirt.play()
                milk.x = cookie.x - 190
                milk.y = cookie.y
                clock.schedule(off, 1)
            if x == "right":
                milk.image = "milk-left2"
                squirt.play()
                milk.x = cookie.x + 190
                milk.y = cookie.y
                clock.schedule(off, 1)
            if milk.colliderect(moldy_cookie):
                cookie_score += 10
                score.play()
    if cookie.colliderect(dirt):
        if not cookie.colliderect(stairs):
            if cookie.y < 360:
                cookie.y += 0
            if cookie.colliderect(grass):
                if cookie.y == 80:
                    cookie.y = 360
                    shadow.y = 360
                    milk.y = 360
                if cookie.y < -60:
                    cookie.y -= 20
                    shadow.y -= 20
                    milk.y -= 20
                else:
                    cookie.y += 0
    if switch == 1:
        shadow2.y = moldy_cookie.y + 100
        shadow2.x = moldy_cookie.x
        if mode == 1:
            point = x
            if point == "left":
                moldy_cookie.image = "moldy-cookie-left-2"
                moldy_cookie.x -= 20
                shadow2.x -= 20
                milk2.x = moldy_cookie.x - 150
                milk2.y = moldy_cookie.y + 20
                clock.schedule(left, 1)
                if moldy_cookie.colliderect(stairs) and moldy_cookie.y < 360:
                    if moldy_cookie.colliderect(stairside1):
                        moldy_cookie.x += 20
                if moldy_cookie.colliderect(bench):
                    if moldy_cookie.y < 580:
                        bench_back.image = "bench back"
                    else:
                        bench_back.image = "0"
                if moldy_cookie.colliderect(bench2):
                    if moldy_cookie.y < 580:
                        bench_back2.image = "bench back"
                    else:
                        bench_back2.image = "0"
                if moldy_cookie.x == 400:
                    if moldy_cookie.colliderect(bench_seat): 
                        moldy_cookie.x += 20
                if moldy_cookie.x == 1200:
                    if moldy_cookie.colliderect(bench_seat2): 
                        moldy_cookie.x += 20
                if moldy_cookie.x < 20:
                    point = "right"
                    moldy_cookie.x += 20
                    shadow2.x += 20
                    milk2.x += 20
                    point = "left"
            if point == "right":
                moldy_cookie.image = "moldy-cookie-right-2"
                moldy_cookie.x += 20
                shadow2.x += 20
                milk2.x = moldy_cookie.x + 150
                milk2.y = moldy_cookie.y + 20
                clock.schedule(right, 1)
                if moldy_cookie.colliderect(stairs) and moldy_cookie.y < 360:
                    if moldy_cookie.colliderect(stairside2):
                        moldy_cookie.x -= 20
                if moldy_cookie.colliderect(bench):
                    if moldy_cookie.y < 580:
                        bench_back.image = "bench back"
                    else:
                        bench_back.image = "0"
                if moldy_cookie.colliderect(bench2):
                    if moldy_cookie.y < 580:
                        bench_back2.image = "bench back"
                    else:
                        bench_back2.image = "0"
                if moldy_cookie.x == 200:
                    if moldy_cookie.colliderect(bench_seat): 
                        moldy_cookie.x -= 20
                if moldy_cookie.x == 1000:
                    if moldy_cookie.colliderect(bench_seat2): 
                        moldy_cookie.x -= 20
                if moldy_cookie.x > 1380:
                    moldy_cookie.x = 20
                if angry == True:
                    moldy_cookie.image = "moldy-cookie-right-2-angry"
                    moldy_cookie.x += 20
                    shadow2.x += 20
                    milk2.x = moldy_cookie.x + 150
                    milk2.y = moldy_cookie.y + 20
            if point == "back":
                moldy_cookie.image = "moldy-cookie-back-2"
                moldy_cookie.y -= 20
                shadow2.y -= 20
                milk2.y -= 20
                milk2.x = moldy_cookie.x 
                milk2.y = moldy_cookie.y - 200
                clock.schedule(up, 1)
                if moldy_cookie.y == 360:
                    if moldy_cookie.colliderect(stairs):
                        if moldy_cookie.x == 700:
                            moldy_cookie.y += 0
                        else:
                            moldy_cookie.y += 20
                    else:
                        moldy_cookie.y += 20
                if moldy_cookie.y < -60:
                    moldy_cookie.y += 20
                if cookie.y == 580:
                    if moldy_cookie.colliderect(bench_seat):
                        moldy_cookie.y += 20
                        shadow2.y += 20
                if moldy_cookie.y == 680:
                    if moldy_cookie.colliderect(bench_seat):
                        moldy_cookie.y += 20
                        moldy_cookie.y -= 20
                if moldy_cookie.y == 580:
                    if moldy_cookie.colliderect(bench_seat2):
                        moldy_cookie.y += 20
                if moldy_cookie.y == 680:
                    if moldy_cookie.colliderect(bench_seat2):
                        moldy_cookie.y += 20
            if point == "front":
                moldy_cookie.image = "moldy-cookie-front"
                moldy_cookie.y += 20
                shadow2.y += 20
                milk2.x = moldy_cookie.x 
                milk2.y = moldy_cookie.y + 200
                if moldy_cookie.y < 580:
                    bench_back.image = "bench back"
                    bench_back2.image = "bench back"
                else:
                    bench_back.image = "0"
                    bench_back2.image = "0"
                if moldy_cookie.y == 540:
                    if moldy_cookie.colliderect(bench):
                        moldy_cookie.y -= 20
                    if moldy_cookie.colliderect(bench2):
                        moldy_cookie.y -= 20
                if moldy_cookie.y == 920:
                    moldy_cookie.y -= 20
                    shadow2.y -= 20
                    point = "back"
        if milk2.colliderect(cookie):
            if switch == 1:
                if point == "left":
                    squirt.play()
                    milk2.image = "milk-left"
                    sugar -= 1
                    jackground.image = "lose"
                    moldy_cookie.pos = 980, 500
                    shadow2.pos = 980, moldy_cookie.y + 100
                    milk2.pos = 980, 600
                    main.stop()
                    clock.schedule(lose, 2.2)
                    clock.schedule(lose2, 2.4)
                    clock.schedule(lose3, 2.6)
                    clock.schedule(lose4, 2.8)
                    clock.schedule(lose5, 3)
                    clock.schedule(lose6, 3.2)
                    clock.schedule(lose7, 3.4)
                    clock.schedule(lose8, 3.6)
                    clock.schedule(lose9, 3.8)
                    clock.schedule(lose10, 4)
                    clock.schedule(lose11, 4.2)
                    clock.schedule(lose12, 4.4)
                    clock.schedule(lose13, 4.6)
                    if sugar > 0:
                        clock.schedule(lose14, 5)
                        milk2.image = "0"
                    if sugar == 0:
                        clock.schedule(lose15, 6)
                        clock.schedule(lose16, 9)
            if point == "right":
                squirt.play()
                milk2.image = "milk-right"
                sugar -= 1
                jackground.image = "lose"
                moldy_cookie.pos = 980, 500
                shadow2.pos = 980, moldy_cookie.y + 100
                milk2.pos = 980, 600
                main.stop()
                clock.schedule(lose, 2.2)
                clock.schedule(lose2, 2.4)
                clock.schedule(lose3, 2.6)
                clock.schedule(lose4, 2.8)
                clock.schedule(lose5, 3)
                clock.schedule(lose6, 3.2)
                clock.schedule(lose7, 3.4)
                clock.schedule(lose8, 3.6)
                clock.schedule(lose9, 3.8)
                clock.schedule(lose10, 4)
                clock.schedule(lose11, 4.2)
                clock.schedule(lose12, 4.4)
                clock.schedule(lose13, 4.6)
                if sugar > 0:
                    clock.schedule(lose14, 5)
                    milk2.image = "0"
                if sugar == 0:
                    clock.schedule(lose15, 6)
                    clock.schedule(lose16, 9)
            if point == "front":
                squirt.play()
                milk2.image = "milk-front"
                sugar -= 1
                jackground.image = "lose"
                moldy_cookie.pos = 980, 500
                shadow2.pos = 980, moldy_cookie.y + 100
                milk2.pos = 980, 600
                main.stop()
                clock.schedule(lose, 2.2)
                clock.schedule(lose2, 2.4)
                clock.schedule(lose3, 2.6)
                clock.schedule(lose4, 2.8)
                clock.schedule(lose5, 3)
                clock.schedule(lose6, 3.2)
                clock.schedule(lose7, 3.4)
                clock.schedule(lose8, 3.6)
                clock.schedule(lose9, 3.8)
                clock.schedule(lose10, 4)
                clock.schedule(lose11, 4.2)
                clock.schedule(lose12, 4.4)
                clock.schedule(lose13, 4.6)
                if sugar > 0:
                    clock.schedule(lose14, 5)
                    milk2.image = "0"
                if sugar == 0:
                    clock.schedule(lose15, 6)
                    clock.schedule(lose16, 9)
            if point == "back":
                squirt.play()
                milk2.image = "milk-back"
                sugar -= 1
                jackground.image = "lose"
                moldy_cookie.pos = 980, 500
                shadow2.pos = 980, moldy_cookie.y + 100
                milk2.pos = 980, 600
                main.stop()
                clock.schedule(lose, 2.2)
                clock.schedule(lose2, 2.4)
                clock.schedule(lose3, 2.6)
                clock.schedule(lose4, 2.8)
                clock.schedule(lose5, 3)
                clock.schedule(lose6, 3.2)
                clock.schedule(lose7, 3.4)
                clock.schedule(lose8, 3.6)
                clock.schedule(lose9, 3.8)
                clock.schedule(lose10, 4)
                clock.schedule(lose11, 4.2)
                clock.schedule(lose12, 4.4)
                clock.schedule(lose13, 4.6)
                if sugar > 0:
                    clock.schedule(lose14, 5)
                    milk2.image = "0"
                if sugar == 0:
                    clock.schedule(lose15, 6)
                    clock.schedule(lose16, 9)
                    milk2.image = "0"
    if cookie.colliderect(bottle):
        fill.play()
        ammo = 5
        bottle.pos = 10000, 10000
    if switch == 1:
        if not cow.x > 1380:
            cow.x += 10
            if cow.x == 0:
                moo.play()
            if number_of_updates == 1:
                run()
                number_of_updates = 0
            else:
                number_of_updates += 1
        else:
           cow.x = 100
           cow.y = randint(360, 900)
           number_of_updates = 0
        if cow.colliderect(bench_back):
            if cow.y >=580:
                bench_back.image = "bench back"
                benchs.image = "bench seat"
                if cow.x > 500:
                    bench_back.image = "0"
                    benchs.image = "0"
        if cow.colliderect(bench_back2):
            if cow.y >= 580:
                bench_back2.image = "bench back"
                benchs2.image = "bench seat"
                if cow.x > 900:
                    bench_back2.image = "0"
                    benchs2.image = "0"
        if cow.colliderect(cookie):
            if cookie.y < cow.y + 270:
                if cookie.y > cow.y - 150:
                    if cookie.x <= cow.x + 170:
                        sugar -= 1
                        jackground.image = "lose"
                        moldy_cookie.pos = 980, 500
                        shadow2.pos = 980, moldy_cookie.y + 100
                        milk2.pos = 980, 600
                        cow.y += 1000000
                        main.stop()
                        clock.schedule(lose, 2.2)
                        clock.schedule(lose2, 2.4)
                        clock.schedule(lose3, 2.6)
                        clock.schedule(lose4, 2.8)
                        clock.schedule(lose5, 3)
                        clock.schedule(lose6, 3.2)
                        clock.schedule(lose7, 3.4)
                        clock.schedule(lose8, 3.6)
                        clock.schedule(lose9, 3.8)
                        clock.schedule(lose10, 4)
                        clock.schedule(lose11, 4.2)
                        clock.schedule(lose12, 4.4)
                        clock.schedule(lose13, 4.6)
                        if sugar > 0:
                            clock.schedule(lose14, 5)
                        if sugar == 0:
                            clock.schedule(lose15, 6)
                            clock.schedule(lose16, 9)
    if keyboard.kp4:
        if switch == 1.5:
            moldy_cookie.image = "moldy-cookie-left-2"
            moldy_cookie.x -= 20
            shadow2.x -= 20
            milk2.x -= 20
            point = "left"
            if moldy_cookie.colliderect(stairs) and moldy_cookie.y < 360:
                if cookie.colliderect(stairside1):
                    moldy_cookie.x += 20
                    shadow2.x += 20
                    milk2.x += 20
            if moldy_cookie.colliderect(bench):
                if moldy_cookie.y < 580:
                    bench_back.image = "bench back"
                else:
                    bench_back.image = "0"
            if moldy_cookie.colliderect(bench2):
                if moldy_cookie.y < 580:
                    bench_back2.image = "bench back"
                else:
                    bench_back2.image = "0"
            if moldy_cookie.x == 400:
                if moldy_cookie.colliderect(bench_seat): 
                    if keyboard.kp6:
                        cookie.x += 20
                        shadow.x += 20
                        milk.x += 20
                    if keyboard.o:
                        cookie.x -= 20
                        shadow.x -= 20
                        milk.x -= 20
            if moldy_cookie.x == 1200:
                if moldy_cookie.colliderect(bench_seat2): 
                    if keyboard.kp4:
                        moldy_cookie.x += 20
                        shadow2.x += 20
    if not keyboard.kp4:
        if point == "left":
            moldy_cookie.image = "moldy-cookie-left"
    if keyboard.kp6:
        if switch == 1.5:
            moldy_cookie.image = "moldy-cookie-right-2"
            moldy_cookie.x += 20
            shadow2.x += 20
            milk2.x += 20
            point = "right"
            if moldy_cookie.colliderect(stairs) and moldy_cookie.y < 360:
                if moldy_cookie.colliderect(stairside2):
                    moldy_cookie.x -= 20
                    shadow2.x -= 20
                    milk2.x -= 20
            if moldy_cookie.colliderect(bench):
                if moldy_cookie.y < 580:
                    bench_back.image = "bench back"
                else:
                    bench_back.image = "0"
            if moldy_cookie.colliderect(bench2):
                if moldy_cookie.y < 580:
                    bench_back2.image = "bench back"
                else:
                    bench_back2.image = "0"
            if moldy_cookie.x == 200:
                if moldy_cookie.colliderect(bench_seat): 
                    if keyboard.kp6:
                        moldy_cookie.x -= 20
                        shadow2.x -= 20
                        milk2.x -= 20
                    if keyboard.o:
                        moldy_cookie.x += 20
                        shadow2.x += 20
                        milk2.x += 20
            if moldy_cookie.x == 1000:
                if moldy_cookie.colliderect(bench_seat2): 
                    if keyboard.kp6:
                        moldy_cookie.x -= 20
                        shadow2.x -= 20
                        milk2.x -= 20
                    if keyboard.o:
                        moldy_cookie.x += 20
                        shadow2.x += 20
                        milk2.x += 20
            if moldy_cookie.x > 1380:
                moldy_cookie.x -= 20
                milk2.x -= 20
                shadow2.x -= 20
    if not keyboard.kp6:
        if point == "right":
            moldy_cookie.image = "moldy-cookie-right"
    if keyboard.kp8:
        if switch == 1.5:
            moldy_cookie.y -= 20
            shadow2.y -= 20
            milk2.y -= 20
            moldy_cookie.image = "moldy-cookie-back-2"
            point = "back"
            if moldy_cookie.y == 360:
                if moldy_cookie.colliderect(stairs):
                    if moldy_cookie.x == 700:
                        moldy_cookie.y += 0
                        shadow2.y += 0
                        milk2.y += 0
                    else:
                        moldy_cookie.y += 20
                        shadow2.y += 20
                        milk2.y += 20
            if moldy_cookie.y < -60:
                moldy_cookie.y += 20
                shadow2.y += 20
                milk2.y += 20
            if moldy_cookie.y == 580:
                if moldy_cookie.colliderect(bench_seat):
                    moldy_cookie.y += 20
                    milk2.y += 20
                    shadow2.y += 20
            if moldy_cookie.y == 680:
                if moldy_cookie.colliderect(bench_seat):
                    moldy_cookie.y += 20
                    milk2.y += 20
                    shadow2.y += 20
                if keyboard.o:
                    moldy_cookie.y -= 20
                    milk2.y -= 20
                    shadow2.y -= 20
            if moldy_cookie.y == 580:
                if moldy_cookie.colliderect(bench_seat2):
                    moldy_cookie.y += 20
                    milk2.y += 20
                    shadow2.y += 20
            if moldy_cookie.y == 680:
                if moldy_cookie.colliderect(bench_seat2):
                   moldy_cookie.y += 20
                   milk2.y += 20
                   shadow2.y += 20
                if keyboard.o:
                    moldy_cookie.y -= 20
                    milk2.y -= 20
                    shadow2.y -= 20
    if not keyboard.kp8:
        if point == "back":
            moldy_cookie.image = "moldy-cookie-back"
    if keyboard.kp2:
        if switch == 1.5:
                moldy_cookie.y += 20
                shadow2.y += 20
                milk2.y += 20
                moldy_cookie.image = "cookie-front"
                x = "front"
                if moldy_cookie.y < 580:
                    bench_back.image = "bench back"
                    bench_back2.image = "bench back"
                else:
                    bench_back.image = "0"
                    bench_back2.image = "0"
                if moldy_cookie.y == 540:
                    if moldy_cookie.colliderect(bench):
                        moldy_cookie.y -= 20
                        milk2.y -= 20
                        shadow2.y -= 20
                    if moldy_cookie.colliderect(bench2):
                        moldy_cookie.y -= 20
                        milk2.y -= 20
                        shadow2.y -= 20
                if moldy_cookie.y == 920:
                    moldie_cookie.y -= 20
                    shadow2.y -= 20
                    milk2.y -= 20
    if keyboard.o:
        shadow2.y = moldy_cookie.y + 100
        if point == "front":
            shadow2.image = "shadow"
            clock.schedule(down2, 1)
        if point == "back":
            shadow2.image = "shadow"
            clock.schedule(down2, 1)
        if point == "right":
            shadow2.image = "shadow"
            clock.schedule(down2, 1)
        if point == "left":
            shadow2.image = "shadow"
            clock.schedule(down2, 1)
    if keyboard.p:
        if ammo2 == 0:
            click.play()
            bottle.image = "milk bottle"
            bottle.x = random.randint(20, 1380)
            bottle.y = random.randint(-40, 900)
            if bottle.y > 360:
                if bottle.y < -40:
                    bottle.y = 360
            if moldy_cookie.colliderect(bottle):
                bottle.pos = randint(20, 1380,) (360, 900)
                fill.play()
                ammo2 = 5
        else:
            milk2.x = moldy_cookie.x
            if point == "front":
                milk2.image = "milk-front2"
                squirt.play()
                clock.schedule(off2, 1)
                milk.y = cookie.y + 230
            if point == "back":
                milk2.image = "milk-back2"
                squirt.play()
                milk.y = moldy_cookie.y - 230
                clock.schedule(off2, 1)
            if point == "left":
                milk2.image = "milk-right2"
                squirt.play()
                milk2.x = moldy_cookie.x - 190
                milk2.y = moldy_cookie.y
                clock.schedule(off2, 1)
            if point == "right":
                milk2.image = "milk-left2"
                squirt.play()
                milk2.x = moldy_cookie.x + 190
                milk2.y = moldy_cookie.y
                clock.schedule(off2, 1)
            if milk2.colliderect(cookie):
                score2 += 10
                score.play()
    if switch == 1.5:
        if not times == 0:
            clock.schedule(timer, sec)
        else:
            times = 0
            main.stop()
            if cookie_score > score2:
                jackground.image = "win1"
                clap.play(4)
                clock.schedule(lose16, 13)
            if cookie_score < score2:
                jackground.image = "win2"
                clap.play(4)
                clock.schedule(lose16, 13)
            if cookie_score == score2:
                jackground.image = "draw"
                dra.play()
                clock.schedule(lose16, 13)
    if switch == 0:
        times = 200
    if keyboard.space:
        if switch == 3:
            controls.pos = 10000, 10000
            po1.x -= 2000
            po2.x -= 2000
            switch = 0
            con.x -= 2000            
def on_mouse_down(pos):
    global switch, mode, ammo2, time
    if po1.collidepoint(pos):
        global time, score2
        switch = 1
        mode = 1
        ammo2 = ""
        time = ""
        score2 = ""
        po1.x += 2000
        po2.x += 2000
        con.x += 2000
        background.image = "ground"
        cookie.image = "cookie-front"
        dirt.image = "dirt"
        stairs.image = "stairs"
        stairside1.image = "stair-side"
        stairside2.image = "stair-side"
        grass.image = "grass"
        bench.image = "bench back"  
        bench_seat.image = "bench seat"
        bench_side.image = "bench legs"
        bench2.image = "bench back"
        bench_seat2.image = "bench seat"
        bench_side2.image = "bench legs"
        moldy_cookie.image = "moldy-cookie-front"
        ammo_sign.image = "ammo"
        score_sign.image = "cookie score"
        sugar_sign.image = "sugar"
        jackground.image = "0"
        cow.image = "cow-left"
        milk2.image = "0"
        main.play(-1)
        start.stop()
    if po2.collidepoint(pos):
        global sugar
        switch = 1.5
        mode = 2
        po1.x += 2000
        po2.x += 2000
        con.x += 2000
        time = 200
        start.stop()
        main.play(-1)
        background.image = "ground"
        cookie.image = "cookie-front"
        dirt.image = "dirt"
        stairs.image = "stairs"
        stairside1.image = "stair-side"
        stairside2.image = "stair-side"
        grass.image = "grass"
        bench.image = "bench back"  
        bench_seat.image = "bench seat"
        bench_side.image = "bench legs"
        bench2.image = "bench back"
        bench_seat2.image = "bench seat"
        bench_side2.image = "bench legs"
        moldy_cookie.image = "moldy-cookie-front"
        ammo_sign.image = "ammo"
        score_sign.image = "cookie score"
        sugar_sign.image = "sugar"
        jackground.image = "0"
        milk2.image = "0"
        ammo_sign2.image = "ammo"
        score_sign2.image = "moldy cookie score"
        clok.image = "clock"
        cow.x += 10000
        sugar = ""
        sugar_sign.x += 2000
    if con.collidepoint(pos):
        start.stop()
        switch = 3
        controls.pos = 700, 400
        po1.x += 2000
        po2.x += 2000
        con.x += 2000
pgzrun.go()
