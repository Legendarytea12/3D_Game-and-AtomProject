from ursina import *
import webbrowser
from ursina.prefabs.first_person_controller import FirstPersonController
import random as rd
url = 'https://youtu.be/dQw4w9WgXcQ?si=qS-P7vK4PIgsjDdo'



x1 =10
x2 = 10
x3 = 10
x4 = 10
x5 = 10
x6 = 10
x7 =10
x8 = 10
x9 = 10
x10 = 10
x11 = 10
lay_y = 0
bk_y1 = 0
bk_y2 = 19.5

app = Ursina()

hole_speed = 0.05
died = False

ships = []
layouts = []
portalsbk1 = []
portalsbk2 = []

hole = Entity(model="sphere", position=(-305,12.5,0), color=rgb(255,255,255), scale=(500,500,500), collider="sphere", texture=("fire.png"))

last_lay = Entity(model='cube', position=(5000,5000,0), color=rgb(120,120,120), scale=(130,1,130), collider='box', texture=('rick-astley.png'))

portal1 = Entity(model='sphere', position=(125,0.1,0), color=rgb(0,0,0), scale=(3.7,0.1,3.7), collider='box')
portal2 = Entity(model='sphere', position=(-10,19.4,0), color=rgb(0,0,0), scale=(3.7,0.1,3.7), collider='box')
portal3 = Entity(model='sphere', position=(125,10.1,0), color=rgb(0,0,0), scale=(3.7,0.1,3.7), collider='box')
portal4 = Entity(model='sphere', position=(-10,29.4,0), color=rgb(0,0,0), scale=(3.7,0.1,3.7), collider='box')
portal5 = Entity(model='sphere', position=(125,20.1,0), color=rgb(0,0,0), scale=(3.7,0.1,3.7), collider='box')
portal6 = Entity(model='sphere', position=(-10,39.4,0), color=rgb(0,0,0), scale=(3.7,0.1,3.7), collider='box')
portal7 = Entity(model='sphere', position=(125,30.1,0), color=rgb(0,0,0), scale=(3.7,0.1,3.7), collider='box')
portal8 = Entity(model='sphere', position=(-10,49.4,0), color=rgb(0,0,0), scale=(3.7,0.1,3.7), collider='box')
portal9 = Entity(model='sphere', position=(125,40.1,0), color=rgb(0,0,0), scale=(3.7,0.1,3.7), collider='box')
portal10 = Entity(model='sphere', position=(-10,59.4,0), color=rgb(0,0,0), scale=(3.7,0.1,3.7), collider='box')
portal11 = Entity(model='sphere', position=(125,50.1,0), color=rgb(0,0,0), scale=(3.7,0.1,3.7), collider='box')
portal12 = Entity(model='sphere', position=(-10,69.4,0), color=rgb(0,0,0), scale=(3.7,0.1,3.7), collider='box')
portal13 = Entity(model='sphere', position=(125,60.1,0), color=rgb(0,0,0), scale=(3.7,0.1,3.7), collider='box')
portal14 = Entity(model='sphere', position=(-10,79.4,0), color=rgb(0,0,0), scale=(3.7,0.1,3.7), collider='box')
portal15 = Entity(model='sphere', position=(125,70.1,0), color=rgb(0,0,0), scale=(3.7,0.1,3.7), collider='box')
portal16 = Entity(model='sphere', position=(-10,89.4,0), color=rgb(0,0,0), scale=(3.7,0.1,3.7), collider='box')
portal17 = Entity(model='sphere', position=(125,80.1,0), color=rgb(0,0,0), scale=(3.7,0.1,3.7), collider='box')
portal18 = Entity(model='sphere', position=(-10,99.4,0), color=rgb(0,0,0), scale=(3.7,0.1,3.7), collider='box')
portal19 = Entity(model='sphere', position=(125,90.1,0), color=rgb(0,0,0), scale=(3.7,0.1,3.7), collider='box')
portal20 = Entity(model='sphere', position=(-10,109.4,0), color=rgb(0,0,0), scale=(3.7,0.1,3.7), collider='box')
portal21 = Entity(model='sphere', position=(125,100.1,0), color=rgb(0,0,0), scale=(3.7,0.1,3.7), collider='box')


room_block1 = Entity(model='cube', position=(5000,500,5000), color=rgb(255,255,255), scale=(20,1,20), collider='box')
room_block2 = Entity(model='cube', position=(5000,510,5010), color=rgb(255,255,255), scale=(20,20,1), collider='box')
room_block3 = Entity(model='cube', position=(5010,510,5000), color=rgb(255,255,255), scale=(1,20,20), collider='box', texture="vrataraya.png")
room_block4 = Entity(model='cube', position=(4990,510,5000), color=rgb(255,255,255), scale=(1,20,20), collider='box')
room_block5 = Entity(model='cube', position=(5000,510,4990), color=rgb(255,255,255), scale=(20,20,1), collider='box')
room_block1 = Entity(model='cube', position=(5000,520,5000), color=rgb(255,255,255), scale=(20,1,20), collider='box')


#ship = Entity(model='cube', position=(10,0.5,0), color=rgb(255,0,0), scale=(0.5,0.2,2), collider='box')

for i in range(17):
    ship1 = Entity(model='cube', position=(x1,0.5,0), color=rgb(255,0,0), scale=(0.5,0.2,2), collider='box', texture=("fire.png"))
    x1 += rd.randint(4,8)
    ships.append(ship1)
for i in range(17):
    ship2 = Entity(model='cube', position=(x2,10.5,0), color=rgb(255,0,0), scale=(0.5,0.2,2), collider='box', texture=("fire.png"))
    x2 += rd.randint(4,8)
    ships.append(ship2)
for i in range(17):
    ship3 = Entity(model='cube', position=(x3,20.5,0), color=rgb(255,0,0), scale=(0.5,0.2,2), collider='box', texture=("fire.png"))
    x3 += rd.randint(4,8)
    ships.append(ship3)
for i in range(17):
    ship4 = Entity(model='cube', position=(x4,30.5,0), color=rgb(255,0,0), scale=(0.5,0.2,2), collider='box', texture=("fire.png"))
    x4 += rd.randint(4,8)
    ships.append(ship4)
for i in range(17):
    ship5 = Entity(model='cube', position=(x5,40.5,0), color=rgb(255,0,0), scale=(0.5,0.2,2), collider='box', texture=("fire.png"))
    x5 += rd.randint(4,8)
    ships.append(ship5)
for i in range(17):
    ship6 = Entity(model='cube', position=(x6,50.5,0), color=rgb(255,0,0), scale=(0.5,0.2,2), collider='box', texture=("fire.png"))
    x6 += rd.randint(4,8)
    ships.append(ship6)
for i in range(17):
    ship7 = Entity(model='cube', position=(x7,60.5,0), color=rgb(255,0,0), scale=(0.5,0.2,2), collider='box', texture=("fire.png"))
    x7 += rd.randint(4,8)
    ships.append(ship7)
for i in range(17):
    ship8 = Entity(model='cube', position=(x8,70.5,0), color=rgb(255,0,0), scale=(0.5,0.2,2), collider='box', texture=("fire.png"))
    x8 += rd.randint(4,8)
    ships.append(ship8)
for i in range(17):
    ship9 = Entity(model='cube', position=(x9,80.5,0), color=rgb(255,0,0), scale=(0.5,0.2,2), collider='box', texture=("fire.png"))
    x9 += rd.randint(4,8)
    ships.append(ship9)
for i in range(17):
    ship10 = Entity(model='cube', position=(x10,90.5,0), color=rgb(255,0,0), scale=(0.5,0.2,2), collider='box', texture=("fire.png"))
    x10 += rd.randint(4,8)
    ships.append(ship10)
for i in range(17):
    ship11 = Entity(model='cube', position=(x11,100.5,0), color=rgb(255,0,0), scale=(0.5,0.2,2), collider='box', texture=("fire.png"))
    x11 += rd.randint(4,8)
    ships.append(ship11)


for i in range(11):
    portalbk1 = Entity(model='sphere', position=(125,bk_y1,0), color=rgb(1,1,200), scale=(4,0.2,4), collider='box')
    bk_y1 += 10
    portalsbk1.append(portalbk1)
for i in range(10):
    portalbk2 = Entity(model='sphere', position=(-10,bk_y2,0), color=rgb(255,89,0), scale=(4,0.2,4), collider='box')
    bk_y2 += 10
    portalsbk2.append(portalbk2)


for i in range(11):
    layout1 = Entity(model='cube', position=(55,lay_y,0), color=rgb(120,120,120), scale=(130,1,2), collider='box', )
    lay_y += 10
    layouts.append(layout1)


def update():
    #print(player.y)
    global hole_speed
    hole.x += hole_speed
    hole_speed += 0.00001
    if player.y <= -40:
        if died == True:
            player.y = 510
            player.x = 5000
            player.z = 5000
        if died == False:
            player.y += 150
            player.z = 0
    for ship in ships:
        if died == True:
            if player.intersects(ship).hit:
                player.y = 510
                player.x = 5000
                player.z = 5000
            if player.intersects(hole).hit:
                player.y = 510
                player.x = 5000
                player.z = 5000

    if player.intersects(portal1).hit:
        hole.x = -305
        hole.y = player.y
        player.x = portal2.x
        player.z = portal2.z
        player.y = portal2.y - 3
    if player.intersects(portal3).hit:
        hole.x = -305
        hole.y = player.y
        player.x = portal4.x
        player.z = portal4.z
        player.y = portal4.y - 3
    if player.intersects(portal5).hit:
        hole.x = -305
        hole.y = player.y
        player.x = portal6.x
        player.z = portal6.z
        player.y = portal6.y - 3
    if player.intersects(portal7).hit:
        hole.x = -305
        hole.y = player.y
        player.x = portal8.x
        player.z = portal8.z
        player.y = portal8.y - 3
    if player.intersects(portal9).hit:
        hole.x = -305
        hole.y = player.y
        player.x = portal10.x
        player.z = portal10.z
        player.y = portal10.y - 3
    if player.intersects(portal11).hit:
        hole.x = -305
        hole.y = player.y
        player.x = portal12.x
        player.z = portal12.z
        player.y = portal12.y - 3
    if player.intersects(portal13).hit:
        hole.x = -305
        hole.y = player.y
        player.x = portal14.x
        player.z = portal14.z
        player.y = portal14.y - 3
    if player.intersects(portal15).hit:
        hole.x = -305
        hole.y = player.y
        player.x = portal16.x
        player.z = portal16.z
        player.y = portal16.y - 3
    if player.intersects(portal17).hit:
        hole.x = -305
        hole.y = player.y
        player.x = portal18.x
        player.z = portal18.z
        player.y = portal18.y - 3
    if player.intersects(portal19).hit:
        hole.x = -305
        hole.y = player.y
        player.x = portal20.x
        player.z = portal20.z
        player.y = portal20.y - 3
    if player.intersects(portal21).hit:
        webbrowser.open_new(url)
        webbrowser.open_new(url)
        webbrowser.open_new(url)
        webbrowser.open_new(url)
        player.y = 5010
        player.x = 5000
#EditorCamera()  # add camera controls for orbiting and moving the camera
player = FirstPersonController(collider='box',position=(0,5,0), scale=(1,1,1))
player.speed = 10
player.gravity = 0.5
Sky(texture='sky_sunset')
app.run()