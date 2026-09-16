import random

"""
One on one fighting game. (Proper British Fight)
When the game starts:
The player will be asked
for the name of the character.
When the game begins, the player of the game will be asked
how many total hitpoints they have, what their min and max
attack strength will be. The person your fighting's properties
will be hard coded.

When the fight starts, you get to go first \\ turn based
only move currently will be attack
Make sure you are telling the player of the game everything
that is happening
Every time an action happens, tell the player the result
"You attacked opponent with an attack strength of 23
opponent now has 77 hitpoints remaining. Please press a and [ENTER]
to initiate the opponents attack."
"Opponent attacked you with an attack strength of 20. You now have
60 hitpoints remaining. Please press a and [ENTER] to attack"
Note I did not copy your code exactly and have decided to make the characters unique
and not ones that are tied to an actual game
"""
# opponent_name = "Kalythos"
# opponent_total_healthpoints = 100
# opponent_min_hitstrenghts = 10
# opponent_max_hitstrenghts = 20
# opponent_alive = True

opponent_1 = ["Kalythos", 100, 25, 50, True]
#opponent_2 = ["Name", HP, MAttack, Maxattack, True]
#opponent_2 = ["Name", HP, MAttack, Maxattack, True]
print("Welcome to Runeverse, a fighting game!")
player = [None, None, None, None, True]
player[0] = input("Please enter a name for your fighter ")
player[1] = int(input("please enter the total "
                               "number of hitpoints: "))
player[2] = int(input("please enter the "
                                "minimum number of hitstrenghts: "))
player[3] = int(input("please enter the "
                                "maximum number of hitstrenghts: "))






while True:

    player_attack_damage = random.randint(player[2],
                                          player[3])

    opponent_1[1] = (opponent_1[1] -
                                player_attack_damage)
    input(f"{player[0]}, you're up. Please press a and [ENTER] "
          f"to attack {opponent_1[0]}")
    if opponent_1[1] <= 0:
        print("You won! Good Game!")
        break
    print(f"You attacked {opponent_1[0]} with a strength"
      f" of {player_attack_damage}.\n"
      f"and now {opponent_1[0]} has {opponent_1[1]} "
      f"hitpoints remaining")
    opponent_attack_damage = random.randint(opponent_1[2],
                                            opponent_1[3])
    player[1] = (player[1] - opponent_attack_damage)

    input(f"It is {opponent_1[0]}'s turn. Please press a and [ENTER] to see what "
      f"{opponent_1[0]} does.")
    print(f"{opponent_1[0]} attacked you with a strength of {opponent_attack_damage},"
      f" you now have {player[1]} hitpoints remaining")
    if player[1] <= 0:
        print("You lost, Try Again!")
        break

print("Thank you for playing!")