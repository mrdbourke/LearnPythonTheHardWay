from sys import exit
from random import randint

class Scene(object):

  def enter(self):
    print "This scene is not yet configured."
    exit(1)

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.open_scene()
        last_scene = self.scene_map.next_scene('finsihed')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        current_scene.enter()

class Death(Scene):
    quips = [
        "You died. You kinda suck at this.",
        "Your mom would be proud... if she were smarter.",
        "Such a luser.",
        "I have a small puppy that's better at this."
    ]

    def enter(self):
        print Death.quips[randint(0, len(self.quips)-1)]
        exit(1)

class CentralCorridor(Scene):

    def enter(self):
        print "You're on a spaceship hurtling through space."
        print "Your goal is to get to the laser weapon armory."
        print "Once here you'll have to find a better weapon to defend yourself through"
        print "the rest of the ship. There's aliens on board who will try to kill"
        print "you."
        print "Your mission is to reach the escape pods are on the other side of the ship."
        print "There's a goblin in front of you, what do you do?"

        action = raw_input("> ")

        if action == "shoot":
            print "You try and shoot the goblin but miss...."
            return 'death'

        if action == "throw grenade":
            print "The goblin catches the grenade before eating it and burping"
            print "the debris back at you."
            return 'death'

        if action == "give cupcake":
            print "You give the goblin a cupcake. He becomes your friend."
            return 'laser_weapon_armory'

        else:
            print "DOES NOT COMPUTE"
            return 'central_corridor'


class LaserWeaponArmory(Scene):

    def enter(self):
        print "You enter the weapons armory."
        print "There's a coded keypad on the weapons chest."
        print "The code changes every 30 seconds so hurry!"
        code = "%d%d%d" % (randint(1,9), randint(1,9), randint(1,9))
        print "Current code:" + code
        print "Enter the code before it changes, you've only got 1 try!"
        code_entry = raw_input("[keypad]> ")

        if code_entry == code:
            print "Code successful."
            print "You pick up the MAJOR LASER"
            return 'the_bridge'
        else:
            return 'death'

class TheBridge(Scene):

    def enter(self):
        print "You manage to make it to the bridge of the ship."
        print "There's a hoard of goblins at the far end of the bridge."
        print "They're dumb so they don't know you're there yet."
        print "If they see you, you're dead. What should you do?"

        action = raw_input("> ")

        if action == "shoot":
            print "You don't manage to shoot them all at once, they end up eating you."
            return 'death'

        if action == "use MAJOR LASER":
            print "You charge the MAJOR LASER......!"
            print "The goblins stupidly line up in a single file."
            print "BOOOOOOM headshot!"
            print "You fire the laser and get a five headshot collateral!!!"
            return 'escape_pod'

        else:
            print "Your actions are futile. The dumb goblins spot you and ravage"
            print "your puny body."
            return 'death'

class EscapePod(Scene):

    def enter(self):
        print "You see a whole bunch of escape pods in the room."
        print "There's three in front of you and 1 of them is damaged."
        print "If you pick the wrong one you're a goner...."
        print "Choose wisely!"

        action = int(raw_input("> "))
        damaged_pod = randint(1,3)

        if action == damaged_pod:
            print "You chose the damaged pod! Catch ya later...."
            return 'death'
        else:
            print "Good choice! You escape at the speed of light back to your home planet."
            print "Catch ya later!"
            return 'finished'

class Finished(Scene):

    def enter(self):
        print "Congratulations! You won the game!"
        return 'finished'


class Map(object):

    scenes = {
    'escape_pod' : EscapePod(),
    'finished' : Finished(),
    'the_bridge' : TheBridge(),
    'central_corridor' : CentralCorridor(),
    'laser_weapon_armory' : LaserWeaponArmory(),
    'death' : Death(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        self.scene_name = scene_name

    def open_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
