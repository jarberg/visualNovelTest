screen planets: #Preparing the imagemap
    imagemap:
        ground "map.png"
        hover "folleman_sexy.PNG"

    imagemap:
        ground "map2.png"
        hover "folleman_sexy.PNG"
        xpos 300
        ypos 250
        hotspot (0, 0, 200, 200) clicked Jump("home")





init python:
    earth_destroyed = False

# The game starts here.
label start:
    "This is an imagemap tutorial."
    jump solar_system

label solar_system:
    call screen planets #Displaying the imagemap

label home:
    scene home
    "this is home"
    jump dialogScript
