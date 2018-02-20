# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.



# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene garden



    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.

    m "hello there."

    c "who are you?"

    m "im the narrator of your life"

    c confused "gettadahere!"

    m "no"

    c feels "shit"

    c sexy "okay then. but is this a \"visual novel?\""

    c sexy "those are for pleps and i dont like pleps"

    m "no no..."

    menu:

        "It's a videogame.":
            jump game

        "It's an interactive book.":
            jump book
        "say it like it is":
            jump porn

    label game:

        m "It's a kind of videogame you can play on your computer or a console."

        jump m1

    label book:

        m "It's like an interactive book that you can read on a computer or a console."

        jump m2

    label porn:

        m "It's basicly an excuse to jerking the beef while getting some reaktion stimulus besides the jerking. and we will get so fucking rich bro"

        jump m3

    label m1:

        c sexy "i dunnow man... sounds like that hentai shit dem kids be shooting up in dem veins on the streets"

        m "alright it is. But that shits \"in\" these days man. plus we will get mad dough"
        c  "i like dough"
        "And so, we become a game creating duo."


        # This ends the game.
    label m2:
        c yeah "FUCKING HELL MAN!"
        c yeah "I FUCKING LOVE INTERACTION AND BOOKS!!!!!"
        m "well shit"
        "And so, we become a visual novel creating duo."


        # This ends the game.
    label m3:
        c "so you saying peps will pay us to let them jerk off to stuff we made??? sounds fishy"
        m "mad fishy indeed ma niglet"
        c "lets do this shit!"
        "And so, we become a porn creating duo."


    m "i hope this settles that"
    c confused "naw man. im fucking baked like a clam... if you know whata mean bby"
    return
        # This ends the game.
