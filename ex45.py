# Exercise 45: Make Your Own Game

# For this exercise you are meant to design your own game in the style
# of Exercise 43. I am going to work on developing a Pokemon-type
# game. I don't know how much I will develop the narrative, but I will
# spend the most time creating a relatively rounded combat system
# because this is where I stand to learn the most about how classes,
# objects, and inheritance function. I'll also have to develop
# a way to automate the the opponent's actions

# Use a random system to assign the likelihood of dodging and other AI actions

from random import randint

# So Pokemon will be dictionaries that store all relevant information
# in keys

Charizard = {'name': 'Charizard',
             'health': 220,
             'dodge': 25,
             'attack1': 50,
             'attack2': 15,
             'type': 'Fire',
             'weakness': 'Water'
             }
Blastoise = {'name': 'Blastoise',
             'health': 230,
             'dodge': 15,
             'attack1': 30,
             'attack2': 10,
             'type': 'Water',
             'weakness': 'Thunder'
             }
Venusaur = {'name': 'Venusaur',
            'health': 240,
            'dodge': 10,
            'attack1': 40,
            'attack2': 10,
            'type': 'Grass',
            'weakness': 'Fire'
            }

pokemon = []
pokemon.append(Charizard)
pokemon.append(Blastoise)
pokemon.append(Venusaur)

pokemon_names = []
pokemon_names.append(Charizard['name'])
pokemon_names.append(Blastoise['name'])
pokemon_names.append(Venusaur['name'])

number_of_pokemon = len(pokemon_names)

attack1_turns = 5
rand_attack1_turns = 5

class SelectPokemon(object):

    def play(self):

        print ''
        print "[string cues]"
        print ''
        print "*" * 34
        print "* SOMETIME IN THE NEAR FUTURE... *"
        print "*" * 34

    # first scene where you select a pokemon
        print ''
        print "You enter into the building. Immediately you are greeted by a man"
        print "In a white lab coat."
        print "\'Welcome to the Pokemon lab! My name is Professor Elm."
        print "Here you can select your Pokemon.\'"
        print "\'We have the following Pokemon available for you:\'"

        index = 0

        for monster in pokemon:
            print ""
            print "Name: %s" % monster['name']
            print "Type: %s" % monster['type']
            print "Health: %s" % monster['health']
            print "Dodge: %s" % monster['dodge']
            print "Main attack: %s" % monster['attack1']
            print "Secondary attack: %s" % monster['attack2']
            print "Weakness: %s" % monster['weakness']
            print ""
        # this increases the index variable each time it cycles through
        # a pokemon
            index += 1
        # this condition stops looping through once you reach the last pokemon
        # based on the specific index
            if index < len(pokemon):
                raw_input("See next Pokemon? ")

        print "The professor smiles at you. 'So, which Pokemon would you like to"
        print "select?\'"
        print ''
        print "You can select:"
        print ""
        for poke in pokemon_names:
            print poke

        print ""

        choice = raw_input('Type the name of the Pokemon you wish to select. ')
    # as long as the player's choice is not amongst the selectable pokemon_names
    # it will prompt them to reenter the name
        while choice not in pokemon_names:
            print ""
            print "Sorry, I didn't get that."
            print ""
            choice = raw_input('Type the name of the Pokemon you wish to select. ')
        else:
            print ""
            print "You have selected %s!" % choice
            print ""

        for monster in pokemon:
            if choice == monster['name']:
                your_pokemon = monster['name']
                your_type = monster['type']
                your_health = monster['health']
                your_dodge = monster['dodge']
                your_attack1 = monster['attack1']
                your_attack2 = monster['attack2']
                your_weakness = monster['weakness']
                print "As a reminder, here are the stats of your Pokemon: "
                print "Name: %s" % monster['name']
                print "Type: %s" % monster['type']
                print "Health: %s" % monster['health']
                print "Dodge: %s" % monster['dodge']
                print "Main attack: %s" % monster['attack1']
                print "Secondary attack: %s" % monster['attack2']
                print "Weakness: %s" % monster['weakness']
                print ""

    # Now I define an __init__ so that I can call these attributes in the
    # battle scene. The battle scene will have composition from this.
    # The idea is that the battle has-a pokemon.
        def __init__(self, your_pokemon, your_type, your_dodge,
                     your_attack1, your_attack2, your_weakness):
            self.your_pokemon = your_pokemon
            self.your_type = your_type
            self.your_dodge = your_dodge
            self.your_attack1 = your_attack1
            self.your_attack2 = your_attack2
            self.your_weakness = your_weakness

        print "\'Very good! You are ready to set out there on your own and"
        print "become the best trainer in all the land!\'"
        print ""
        print "The professor opens the door and you embark on your journey."
        print ""
        print "*" * 25
        print "* QUINN'S POKEMON QUEST *"
        print '*' * 25

        return 'battle'

class Battle(object):
    # Use composition to get pokemon into this class
    def __init__(self):
        self.pokemon = SelectPokemon()

    def play(self):

        global your_pokemon
        global your_type
        global your_health
        global your_weakness
        global your_dodge
        global your_attack1
        global your_attack2

        random_number = randint(0,(number_of_pokemon-1))
        rand_pokemon = pokemon_names[random_number]
        for monster in pokemon:
            if rand_pokemon == monster['name']:
                rand_type = monster['type']
                rand_health = monster['health']
                rand_dodge = monster['dodge']
                rand_attack1 = monster['attack1']
                rand_attack2 = monster['attack2']
                rand_weakness = monster['weakness']

        global rand_pokemon
        global rand_type
        global rand_health
        global rand_dodge
        global rand_attack1
        global rand_attack2
        global rand_weakness

        print ""
        print "As you wander through the wilderness, you take in the natural"
        print "wonder presented to you. What a life to be living!"
        print "Suddenly, you stop. You hear a rustle in the nearby bushes."
        print ""
        print "A wild %s appears!" % rand_pokemon
        print "[energetic music starts]"

        global rand_attack1_turns

        attack()

class Journey(object):

    def play(self):
        print "cool"


class End(object):

    def play(self):
        print ""
        print "Uh oh! Your Pokemon fainted!."
        print "welp"
        print ""

class Map(object):

    scenes = {
    'select': SelectPokemon(),
    'battle': Battle(),
    'onward': Journey(),
    'end': End()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

class Engine(object):
    def __init__(self, scene_map):
        self.scene_map = scene_map

    def playthrough(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('end')

        while current_scene != last_scene:
            next_scene_name = current_scene.play()
            current_scene = self.scene_map.next_scene(next_scene_name)

        current_scene.playthrough()

def attack():

    global attack1_turns
    global rand_health
    global your_health

    print ""
    print "Which attack do you choose?"
    print "You can use Attack 1 another %s times." % attack1_turns
    print ""
    attack_choice = raw_input('Attack 1 or Attack 2? ')
    print ""
    if your_health <= 0:
        return 'end'
    elif rand_health <= 0:
        return 'onward'
    elif attack_choice == "Attack 1" and attack1_turns != 0:
        if rand_dodge >= randint(1,100):
            print "The wild %s dodged your attack!" % rand_pokemon
            print ""
            attack1_turns -= 1
            opponent_attack()
        else:
            if rand_weakness == your_type:
                rand_health -= (your_attack1)*1.2
                print "Your attack is super effective!"
                attack1_turns -= 1
                print "%s's health is now %s" % (rand_pokemon, rand_health)
                print ""
                opponent_attack()
            else:
                rand_health -= (your_attack1)
                attack1_turns -= 1
                print "Direct hit!"
                print "%s's health is now %s" % (rand_pokemon, rand_health)
                print ""
                opponent_attack()
    elif attack_choice == "Attack 2":
        if rand_dodge >= randint(1,100):
            print "Your attack missed!"
            print ""
            opponent_attack()
        else:
            if rand_weakness == your_type:
                rand_health -= (your_attack2)*1.2
                print "Your attack is super effective!"
                print "%s's health is now %s" % (rand_pokemon, rand_health)
                print ""
                opponent_attack()
            else:
                rand_health -= (your_attack2)
                print "Direct hit!"
                print "%s's health is now %s" % (rand_pokemon, rand_health)
                print ""
                opponent_attack()
    elif attack_choice == 'Attack 1' and attack1_turns == 0:
        print "Oops! You can't use Attack 1 anymore."
        print ""
        attack()
    else:
        print "Sorry, I didn't get that."
        print "Which attack do you choose?"
        attack()

def opponent_attack():

    global rand_attack1_turns
    global your_health
    global rand_health

    if your_health <= 0:
        return 'end'
    elif rand_health <= 0:
        return 'onward'
    elif randint(1,2) == 1 and rand_attack1_turns != 0:
        if your_dodge >= randint(1,100):
            print "%s used Attack 1!" % rand_pokemon
            print "%s's attack missed!" % rand_pokemon
            rand_attack1_turns -= 1
            attack()
        else:
            if your_weakness == rand_type:
                your_health -= (rand_attack1) * 1.2
                print "%s used Attack 1!" % rand_pokemon
                print "%s's attack is super effective!" % rand_pokemon
                print "Your Pokemon's health is now %s" % your_health
                rand_attack1_turns -= 1
                attack()
            else:
                your_health -= rand_attack1
                print "%s used Attack 1!" % rand_pokemon
                print "Direct hit!"
                print "Your Pokemon's health is now %s" % your_health
                rand_attack1_turns -= 1
                attack()

    else:
        if your_dodge >= randint(1,100):
            print "%s used Attack 2!" % rand_pokemon
            print "%s's attack missed!" % rand_pokemon
            attack()
        else:
            if your_weakness == rand_type:
                your_health -= (rand_attack2) * 1.2
                print "%s used Attack 2!" % rand_pokemon
                print "%s's attack is super effective!" % rand_pokemon
                print "Your Pokemon's health is now %s" % your_health
                attack()

            else:
                your_health -= rand_attack1
                print "%s used Attack 2!" % rand_pokemon
                print "Direct hit!"
                print "Your Pokemon's health is now %s" % your_health
                attack()


# Beginning the game.
the_map = Map('select')
a_game = Engine(the_map)
a_game.playthrough()
