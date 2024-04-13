from ursina import *

app = Ursina()
atom1 = Entity(model="atom.obj",position=(0,0,0),color=rgb(0,0,255))
atom2 = Entity(model="atom2.obj",position=(0,0,0),color=rgb(100,100,100))
atom3 = Entity(model="atom3.obj",position=(0,0,0),color=rgb(100,100,100))
atom4 = Entity(model="atom4.obj",position=(0,0,0),color=rgb(100,100,100))

def update():
    atom2.rotation_x += 90 * time.dt
    atom2.rotation_y += 90 * time.dt
    atom2.rotation_z += 90 * time.dt
    atom3.rotation_y += 90 * time.dt
    atom3.rotation_z += 90 * time.dt
    atom4.rotation_x += 90 * time.dt
    atom4.rotation_z += 90 * time.dt
EditorCamera(positon=(0,0,0))
Sky(texture='sky_sunset')
app.run()