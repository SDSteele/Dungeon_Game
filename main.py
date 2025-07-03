from time import sleep
import random
# add a section for wrappers so that I can put the sleep delay after every print function without typing it over and over
# add player levels, exp, skills
# add later: critical hits, weapons, armor, items (potions), and a shop
# add different enemies with different stats
# add a shop between fights where the player can buy items
# add a win and lose condition
# create a text based map for the player to explore. Include different rooms with different enemies and items.
    #make the dungeon randomly generated so that each playthrough is different.




print("Welcome to the Adventure Game!")

player_name = input("Enter your character's name: ")

#hero = player_name, hp = 25, attack = 10
player_stats = {
    "name": player_name.capitalize(),
    "hp": 100,
    "attack": 10
}

enemy = {
    "name": "Goblin",
    "hp": 50,
    "attack": 5
}

print(f"{player_stats['name']} has entered the dungeon. Current stats are: {player_stats['hp']} HP and {player_stats['attack']} attack power.")

sleep(1)

print("You step into the dungeon. Light from your torch flickers and dances on the stone walls. You hear scartching and gnawing of bone. It can be only one thing. Goblins.")

sleep(.5)

print("You take one step. Two. Further toward the sound. The gnawing stops. A chuckle erupts from behind you. I was a trap. Prepare to fight for you life")

sleep(.5)

#enemy = "Goblin", hp = 50 attack = 5
print(f"The {enemy['name']} stands before you. You draw your sword.")
sleep(.5)

# the combat loop will be turned based. The player can either attack or defend. Attacking will take their attack power and pick a random interger
#from 1 to 10 (the amount of their attack power) and subtract that from the enemy's hp.
# the hero can also defend, which will reduce the damage taken by half.
#the enemy will attack back after the player attacks or defends. the same rules apply to the enemy's attack.
# add a final screen that displays the player's final stats and whether they won or lost.

while player_stats['hp'] > 0 and enemy['hp'] > 0:
    action = input("Do you want to (A)ttack or (D)efend? ").strip().upper() #the .strip() method removes any leading or trailing whitespace, and .upper() converts the input to uppercase for consistency.
    #  the .upper() method is used to make the input case-insensitive, so the player can type 'a', 'A', 'd', or 'D'.
    
    if action == 'A': #the player chooses to attack
        damage = random.randint(1, player_stats['attack']) #the random.randint() function generates a random integer between 1 and the player's attack power.
        enemy['hp'] -= damage #the enemy's hp is reduced by the damage dealt by the player.
        print(f"You attack the {enemy['name']} for {damage} damage.")

    elif action == 'D': #the player chooses to defend
        damage = random.randint(1, enemy['attack']) // 2 #the damage taken is halved.
        player_stats['hp'] -= damage #the player's hp is reduced by the damage taken.
        print(f"You defend against the {enemy['name']}'s attack and take {damage} damage.")

    else: #the player enters an invalid action
        print("Invalid action. Please choose 'A' to attack or 'D' to defend.")
    # the enemy attacks back after the player attacks or defends

    if enemy['hp'] > 0: #if the enemy is still alive
        enemy_damage = random.randint(1, enemy['attack']) #the enemy's damage is calculated.
        player_stats['hp'] -= enemy_damage #the player's hp is reduced by the enemy's damage.
        print(f"The {enemy['name']} attacks you for {enemy_damage} damage.")

if enemy['hp'] <= 0: #if the enemy is defeated
    print(f"You have defeated the {enemy['name']}! You are victorious!")
    
if player_stats['hp'] <= 0: #if the player is defeated
    print("You have been defeated. Game over.")




