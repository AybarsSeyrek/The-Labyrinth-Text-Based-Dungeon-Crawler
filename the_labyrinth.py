import random

# This game is a simple text-based dungeon crawler.
# The player picks a character, explores The Labyrinth,
# fights monsters, avoids traps, finds treasure, and tries to defeat the final boss.

MAX_STAT = 6
MAX_LIVES = 5


# -----------------------------
# Opening story
# -----------------------------

def show_intro_story():
    # Opening story before character selection.
    # The narrator knows this is a game, but the characters inside the world do not.

    print("====================================")
    print("THE LABYRINTH")
    print("====================================\n")

    print("In the borderlands, far from the capital and farther still from mercy,")
    print("there was a village built beside an old stone well.")
    print("The villagers called it a blessing.")
    print("The old adventurers called it a mistake.\n")

    print("For many years, the well gave clean water.")
    print("Then, one winter night, it gave back a hand.")
    print("Small. Green. Clawed.")
    print("After that, children went missing.")
    print("Then goats.")
    print("Then the men who went looking for them.\n")

    print("The village elder sent word to the guild.")
    print("The request was simple:")
    print("\"Goblins in the lower tunnels. Please send help.\"")
    print("The reward was poor, so most adventurers ignored it.")
    print("That is how these things usually begin.\n")

    print("But The Labyrinth does not care about reward money.")
    print("A goblin's knife does not care about courage.")
    print("A trap does not care if the one stepping on it had good intentions.\n")

    print("Somewhere beyond the eyes of the characters, dice are waiting to fall.")
    print("A good warrior may live because a small number appears.")
    print("A careful scout may die because fate lands badly on the table.")
    print("The adventurer does not know this.")
    print("To them, it is only darkness, breath, blood, and the next step forward.\n")

    print("So now, one soul stands at the mouth of The Labyrinth.")
    print("Lantern in hand.")
    print("Weapon ready.")
    print("Five chances between life and death.")
    print("Below, the goblins are hungry.")
    print("Deeper still, something worse is watching.\n")

    print("Choose who descends.\n")


# -----------------------------
# Character data
# -----------------------------

characters = {
    "1": {
        "name": "Human Adventurer",
        "attack": 5,
        "defense": 4,
        "perception": 4,
        "inventory": {
            "Healing Herb": 0,
            "Old Shield": 0,
            "Torch": 0
        }
    },
    "2": {
        "name": "Elf Archer",
        "attack": 4,
        "defense": 3,
        "perception": 6,
        "inventory": {
            "Healing Herb": 0,
            "Old Shield": 0,
            "Torch": 0
        }
    },
    "3": {
        "name": "Dwarf Shaman",
        "attack": 3,
        "defense": 5,
        "perception": 2,
        "inventory": {
            "Healing Herb": 0,
            "Old Shield": 0,
            "Torch": 0
        }
    },
    "4": {
        "name": "Test",
        "attack": 6,
        "defense": 6,
        "perception": 6,
        "inventory": {
            "Healing Herb": 0,
            "Old Shield": 0,
            "Torch": 0
        }
    }
}


# -----------------------------
# Enemy data
# -----------------------------

enemies = {
    "goblin": {
        "name": "Goblin",
        "attack": 1,
        "defense": 1
    },
    "hobgoblin": {
        "name": "Hobgoblin",
        "attack": 2,
        "defense": 2
    },
    "orc": {
        "name": "Orc",
        "attack": 3,
        "defense": 3
    },
    "beholder": {
        "name": "Beholder",
        "attack": 5,
        "defense": 5
    }
}


# -----------------------------
# Score data
# -----------------------------

def create_score():
    # This keeps track of what the player did.
    return {
        "rooms_explored": 0,
        "enemies_slain": 0,
        "traps_disarmed": 0,
        "traps_triggered": 0,
        "gold": 0,
        "items_found": 0,
        "floors_cleared": 0,
        "path": [],
        "ending": "Unknown"
    }


# -----------------------------
# Dungeon room flavor
# -----------------------------

floor_room_fluff = {
    1: [
        "The floor is muddy with small footprints. Something dragged a sack through here recently.",
        "The walls are scratched by tiny blades and dirty fingernails.",
        "A sour goblin smell hangs in the air like spoiled meat.",
        "Broken arrows and cracked bowls are scattered across the stones.",
        "You hear distant giggling, but it stops when you listen closely.",
        "A small cooking fire has burned out, leaving black ash and animal bones.",
        "The ceiling is low here. It feels like the tunnel was made for smaller creatures.",
        "Someone painted crude symbols on the wall using old blood."
    ],
    2: [
        "The room smells like boiled roots, monster fat, and old smoke.",
        "Hooks hang from the ceiling, but most of them are empty.",
        "Strange mushrooms grow from cracks in the wall, glowing softly.",
        "A broken butcher table leans against the stone like a defeated beast.",
        "You hear water dripping into a metal pot somewhere in the dark.",
        "Bones are sorted into piles, almost like ingredients.",
        "The floor is sticky. You decide not to think about why.",
        "A torn recipe page lies on the ground, written in a language you cannot read."
    ],
    3: [
        "The stone here is older and colder than the floors above.",
        "Your lantern flame bends sideways, even though there is no wind.",
        "A carved eye watches from the ceiling.",
        "The walls are covered in ancient warnings, but the words have faded.",
        "Broken shields rest against the wall, all facing the same direction.",
        "The silence here feels alive.",
        "You hear something massive shift far below your feet.",
        "The air tastes like dust, iron, and old magic."
    ]
}


enemy_hints = [
    "You hear wet claws scraping somewhere to the {direction}.",
    "A foul monster stench leaks from the {direction} passage.",
    "You see small footprints leading {direction}.",
    "Something breathes slowly in the dark to the {direction}.",
    "You hear the clatter of bones from the {direction}, but it quickly fades."
]

trap_hints = [
    "A thin wire glints in the dust near the {direction} path.",
    "The stones on the {direction} look too clean.",
    "You notice small holes in the wall near the {direction} passage.",
    "The dust near the {direction} path has been strangely disturbed.",
    "Something about the {direction} passage feels carefully arranged."
]

empty_hints = [
    "The {direction} path is quiet, except for dripping water.",
    "The air from the {direction} smells damp, but not dangerous.",
    "You notice old bones near the {direction}, but no fresh tracks.",
    "The {direction} passage feels still and abandoned.",
    "A faint smell of mushrooms comes from the {direction}."
]

treasure_hints = [
    "Something small shines in the dark to the {direction}.",
    "You see old adventurer markings near the {direction} path.",
    "The {direction} passage smells faintly of oil, leather, and old packs.",
    "A broken chest mark is carved into the stone near the {direction}.",
    "You hear coins shift softly somewhere to the {direction}."
]


def show_room_fluff(floor_number):
    # Every room gets flavor text, even if it has an enemy, trap, or treasure.
    print("\nRoom atmosphere:")
    print(random.choice(floor_room_fluff[floor_number]))


# -----------------------------
# Basic dice roll functions
# -----------------------------

def roll_dice():
    # Rolls a 6-sided die.
    return random.randint(1, 6)


def check_success(stat):
    # This makes sure stats never go above 6.
    # Since we only roll a 6-sided die, 6 is the highest useful stat.
    stat = min(MAX_STAT, stat)

    roll = roll_dice()
    success = roll <= stat
    return roll, success


# -----------------------------
# Character selection
# -----------------------------

def choose_character():
    print("====================================")
    print("THE LABYRINTH")
    print("====================================")
    print("Choose your adventurer:\n")

    print("1. Human Adventurer")
    print("   Attack: 5 | Defense: 4 | Perception: 4")
    print("   Moves: Attack, Skip Turn\n")

    print("2. Elf Archer")
    print("   Attack: 4 | Defense: 3 | Perception: 6")
    print("   Moves: Attack, Skip Turn\n")

    print("3. Dwarf Shaman")
    print("   Attack: 3 | Defense: 5 | Perception: 2")
    print("   Moves: Attack, Skip Turn\n")

    print("4. Test")
    print("   Attack: 6 | Defense: 6 | Perception: 6")
    print("   Moves: Attack, Skip Turn\n")

    while True:
        choice = input("Enter 1, 2, 3, 4, or character name: ").strip().lower()

        if choice in characters:
            return characters[choice]

        if choice in ["human", "human adventurer"]:
            return characters["1"]

        if choice in ["elf", "elf archer"]:
            return characters["2"]

        if choice in ["dwarf", "dwarf shaman"]:
            return characters["3"]

        if choice == "test":
            return characters["4"]

        print("Invalid character choice. Please try again.\n")


# -----------------------------
# Inventory system
# -----------------------------

def show_inventory(player):
    print("\nInventory:")
    print(f"Healing Herb: {player['inventory']['Healing Herb']}")
    print(f"Old Shield: {player['inventory']['Old Shield']}")
    print(f"Torch: {player['inventory']['Torch']}")


def use_healing_herb(player, lives):
    # Healing herb restores 1 life, but lives cannot go above 5.
    if player["inventory"]["Healing Herb"] <= 0:
        print("You do not have a Healing Herb.")
        return lives

    if lives >= MAX_LIVES:
        print("Your lives are already full.")
        return lives

    player["inventory"]["Healing Herb"] -= 1
    lives = min(MAX_LIVES, lives + 1)

    print("You use a Healing Herb.")
    print(f"Lives left: {lives}")

    return lives


def use_torch(player):
    # Torch gives +1 perception, but perception cannot go above 6.
    if player["inventory"]["Torch"] <= 0:
        print("You do not have a Torch.")
        return

    if player["perception"] >= MAX_STAT:
        print("Your perception is already at the maximum of 6.")
        return

    player["inventory"]["Torch"] -= 1
    player["perception"] = min(MAX_STAT, player["perception"] + 1)

    print("You light a Torch.")
    print(f"Your perception is now {player['perception']}.")


def open_inventory_menu(player, lives):
    # This lets the player use items without breaking movement.
    # Old Shield is only used at the start of combat, so it is not used here.

    while True:
        show_inventory(player)
        print("\nWhat do you want to use?")
        print("1. Healing Herb")
        print("2. Torch")
        print("3. Leave inventory")

        choice = input("Choose 1, 2, or 3: ").strip().lower()

        if choice in ["1", "healing herb", "herb"]:
            lives = use_healing_herb(player, lives)

        elif choice in ["2", "torch"]:
            use_torch(player)

        elif choice in ["3", "leave", "exit", "back"]:
            return lives

        else:
            print("Invalid command. Please try again.")


def ask_use_old_shield(player):
    # Old Shield gives +1 defense for one fight only.
    # It still cannot make defense go above 6.

    if player["inventory"]["Old Shield"] <= 0:
        return 0

    if player["defense"] >= MAX_STAT:
        print("\nYou have an Old Shield, but your defense is already 6.")
        return 0

    while True:
        choice = input("\nUse Old Shield for +1 defense this fight? Y/N: ").strip().lower()

        if choice == "y":
            player["inventory"]["Old Shield"] -= 1
            print("You raise the Old Shield. It may not survive the fight.")
            return 1

        if choice == "n":
            return 0

        print("Invalid command. Please type Y or N.")


# -----------------------------
# Treasure system
# -----------------------------

def handle_treasure_room(player, score):
    # Treasure rooms give random gold and maybe an item.

    print("\nYou find a small treasure stash.")
    print("It looks like it belonged to an adventurer who did not make it back.")

    gold_found = random.randint(5, 25)
    score["gold"] += gold_found

    print(f"You found {gold_found} gold.")

    possible_items = ["Healing Herb", "Old Shield", "Torch", "nothing"]
    item_found = random.choice(possible_items)

    if item_found == "nothing":
        print("There are no useful items left.")
        return

    player["inventory"][item_found] += 1
    score["items_found"] += 1

    print(f"You found an item: {item_found}")

    if item_found == "Healing Herb":
        print("Healing Herb can restore 1 life, up to 5 lives.")

    elif item_found == "Old Shield":
        print("Old Shield can give +1 defense for one fight, up to 6 defense.")

    elif item_found == "Torch":
        print("Torch can give +1 perception, up to 6 perception.")


# -----------------------------
# Combat system
# -----------------------------

def enemy_attack_player(enemy, player, lives, temporary_defense_bonus):
    # This handles the enemy attacking the player.
    # It returns the updated number of lives.

    print(f"\nThe {enemy['name']} attacks!")

    enemy_roll, enemy_hits = check_success(enemy["attack"])
    print(f"{enemy['name']} attack roll: {enemy_roll}")

    if not enemy_hits:
        print(f"The {enemy['name']} missed!")
        return lives

    current_defense = min(MAX_STAT, player["defense"] + temporary_defense_bonus)

    defense_roll, defended = check_success(current_defense)
    print(f"{player['name']} defense roll: {defense_roll}")
    print(f"Current defense used: {current_defense}")

    if defended:
        print("You dodged or blocked the attack!")
    else:
        lives -= 1
        print("The attack hits you!")
        print(f"Lives left: {lives}")

    return lives


def fight_enemy(enemy, player, lives, score):
    # Main fight loop.
    # Enemies do not have HP.
    # If the player lands an attack and the enemy fails defense, the enemy dies.

    print("\nA hostile creature appears!")
    print(f"You face a {enemy['name']}!")
    print(f"{enemy['name']} stats: Attack {enemy['attack']} | Defense {enemy['defense']}")

    temporary_defense_bonus = ask_use_old_shield(player)

    if temporary_defense_bonus > 0:
        current_defense = min(MAX_STAT, player["defense"] + temporary_defense_bonus)
        print(f"Your defense for this fight is {current_defense}.")

    enemy_alive = True

    while enemy_alive and lives > 0:
        print("\nYour moves: attack / skip / inventory")

        move = input("Choose your move: ").strip().lower()

        if move == "inventory":
            lives = open_inventory_menu(player, lives)
            continue

        if move not in ["attack", "skip", "skip turn"]:
            print("Invalid command. Please type attack, skip, or inventory.")
            continue

        # Player always goes first.
        if move == "attack":
            attack_roll, player_hits = check_success(player["attack"])
            print(f"\nYour attack roll: {attack_roll}")

            if player_hits:
                enemy_defense_roll, enemy_defends = check_success(enemy["defense"])
                print(f"{enemy['name']} defense roll: {enemy_defense_roll}")

                if enemy_defends:
                    print(f"The {enemy['name']} dodged!")
                else:
                    print(f"The {enemy['name']} was slain!")
                    score["enemies_slain"] += 1
                    enemy_alive = False
                    break
            else:
                print("You missed!")

        else:
            print("You skip your turn and watch the shadows carefully.")

        # If the enemy survived the player's turn, it attacks.
        if enemy_alive:
            lives = enemy_attack_player(enemy, player, lives, temporary_defense_bonus)

            if lives <= 0:
                print("\nYOU DIED")
                return lives, False

    return lives, True


# -----------------------------
# Trap system
# -----------------------------

def trigger_trap(player, lives, score):
    # This handles a light trap.
    # The trap attacks only one time, then it disappears.

    print("\nA hidden light trap snaps into motion!")

    score["traps_triggered"] += 1

    trap_attack = 1
    trap_roll, trap_hits = check_success(trap_attack)
    print(f"Trap attack roll: {trap_roll}")

    if not trap_hits:
        print("The trap failed!")
        print("The mechanism breaks after triggering.")
        return lives

    defense_roll, defended = check_success(player["defense"])
    print(f"{player['name']} defense roll: {defense_roll}")

    if defended:
        print("You avoid the trap!")
    else:
        lives -= 1
        print("The trap hits you!")
        print(f"Lives left: {lives}")

    print("The trap breaks after triggering.")
    return lives


# -----------------------------
# Room generation
# -----------------------------

def create_room_options(floor_number):
    # Creates the left and right room choices.
    # Each room can be empty, trap, enemy, or treasure.

    if floor_number == 1:
        enemy_type = "goblin"
        possible_rooms = ["empty", "empty", "trap", "enemy", "treasure"]

    elif floor_number == 2:
        enemy_type = "hobgoblin"
        possible_rooms = ["empty", "trap", "enemy", "enemy", "treasure"]

    else:
        enemy_type = "orc"
        possible_rooms = ["empty", "trap", "enemy", "enemy", "treasure"]

    left_room_type = random.choice(possible_rooms)
    right_room_type = random.choice(possible_rooms)

    left_room = {
        "type": left_room_type,
        "enemy": enemy_type if left_room_type == "enemy" else None
    }

    right_room = {
        "type": right_room_type,
        "enemy": enemy_type if right_room_type == "enemy" else None
    }

    return {
        "left": left_room,
        "right": right_room
    }


def get_room_hint(room, direction):
    # Gives a cryptic hint for a room.
    # It does not directly say if the room has an enemy, trap, treasure, or nothing.

    if room["type"] == "enemy":
        hint = random.choice(enemy_hints)

    elif room["type"] == "trap":
        hint = random.choice(trap_hints)

    elif room["type"] == "treasure":
        hint = random.choice(treasure_hints)

    else:
        hint = random.choice(empty_hints)

    return hint.format(direction=direction)


def handle_room(room, player, lives, perception_success, floor_number, score):
    # Resolves what happens inside a room.
    # Every room gets flavor text first.

    score["rooms_explored"] += 1

    show_room_fluff(floor_number)

    if room["type"] == "empty":
        print("\nThe room is empty.")
        print("Nothing attacks you, but the place still feels wrong.")
        return lives, True

    if room["type"] == "treasure":
        handle_treasure_room(player, score)
        return lives, True

    if room["type"] == "trap":
        if perception_success:
            print("\nYou notice the trap before stepping fully into the room.")
            print("You carefully disarm it.")
            score["traps_disarmed"] += 1
            return lives, True
        else:
            lives = trigger_trap(player, lives, score)

            if lives <= 0:
                print("\nYOU DIED")
                return lives, False

            return lives, True

    if room["type"] == "enemy":
        enemy = enemies[room["enemy"]]
        lives, survived = fight_enemy(enemy, player, lives, score)
        return lives, survived

    return lives, True


# -----------------------------
# Floor system
# -----------------------------

def ask_descend():
    # Asks the player if they want to go to the next floor.
    # It keeps asking if the input is invalid.

    while True:
        choice = input("\nDo you want to descend further? Y/N: ").strip().lower()

        if choice == "y":
            return True

        if choice == "n":
            return False

        print("Invalid command. Please type Y or N.")


def play_floor(floor_number, player, lives, score):
    # Plays one full dungeon floor.
    # Each floor has 8 rooms, then the floor ends.

    print("\n====================================")
    print(f"THE LABYRINTH - FLOOR {floor_number}")
    print("====================================")

    if floor_number == 1:
        print("You enter a goblin nest beneath an abandoned cellar.")
        print("The stones smell of smoke, blood, and old meals.")
        print("Small footprints vanish into cracks in the wall.")

    elif floor_number == 2:
        print("You descend into monster kitchen ruins.")
        print("Bones hang from hooks, and strange herbs grow from cracked walls.")
        print("Something once used this place to cook whatever wandered too deep.")

    else:
        print("You step into an ancient cursed part of The Labyrinth.")
        print("The air feels heavy, as if the dungeon itself is watching you.")
        print("The stones are older here. So are the things that wait between them.")

    # The player visits 8 rooms per floor.
    for room_number in range(1, 9):
        print("\n------------------------------------")
        print(f"Floor {floor_number}, Rooms Visited {room_number}/8")
        print("------------------------------------")

        room_options = create_room_options(floor_number)

        print("Two passages open before you: left and right.")
        print("You may also type inventory before choosing a direction.")

        perception_roll, perception_success = check_success(player["perception"])
        print(f"\nPerception roll: {perception_roll}")

        if perception_success:
            print("Perception check succeeded.")
            print("You study the nearby passages.")
            print("Left:", get_room_hint(room_options["left"], "left"))
            print("Right:", get_room_hint(room_options["right"], "right"))
        else:
            print("Perception check failed.")

        while True:
            direction = input("\nGo left or right: ").strip().lower()

            if direction == "inventory":
                lives = open_inventory_menu(player, lives)
                continue

            if direction in ["left", "right"]:
                break

            print("Invalid command. Please type left or right.")

        score["path"].append(f"Floor {floor_number}, Room {room_number}: {direction}")

        chosen_room = room_options[direction]
        print(f"\nYou go {direction}.")

        lives, survived = handle_room(chosen_room, player, lives, perception_success, floor_number, score)

        if not survived:
            return lives, False

    score["floors_cleared"] += 1
    print("\nYou reach the end of this floor of The Labyrinth.")
    return lives, True


# -----------------------------
# Final boss
# -----------------------------

def fight_final_boss(player, lives, score):
    print("\n====================================")
    print("THE HEART OF THE LABYRINTH")
    print("====================================")
    print("A round chamber opens beneath the dungeon.")
    print("Broken shields, empty helmets, and half-eaten monster bones cover the floor.")
    print("Above them floats a terrible Beholder, its central eye turning toward you.")
    print("The Labyrinth waits for the final roll.")

    boss = enemies["beholder"]

    lives, survived = fight_enemy(boss, player, lives, score)

    if survived and lives > 0:
        print("\nYou conquered The Labyrinth.")
        score["ending"] = "You conquered The Labyrinth."
        return True

    score["ending"] = "You died in the heart of The Labyrinth."
    return False


# -----------------------------
# End score screen
# -----------------------------

def show_final_score(player, lives, score):
    print("\n====================================")
    print("FINAL SCORE")
    print("====================================")

    print(f"Character: {player['name']}")
    print(f"Lives left: {lives}")
    print(f"Gold collected: {score['gold']}")
    print(f"Rooms explored: {score['rooms_explored']}")
    print(f"Enemies slain: {score['enemies_slain']}")
    print(f"Traps disarmed: {score['traps_disarmed']}")
    print(f"Traps triggered: {score['traps_triggered']}")
    print(f"Items found: {score['items_found']}")
    print(f"Floors cleared: {score['floors_cleared']}")
    print(f"Ending: {score['ending']}")

    print("\nFinal Stats:")
    print(f"Attack: {player['attack']}")
    print(f"Defense: {player['defense']}")
    print(f"Perception: {player['perception']}")

    print("\nFinal Inventory:")
    print(f"Healing Herb: {player['inventory']['Healing Herb']}")
    print(f"Old Shield: {player['inventory']['Old Shield']}")
    print(f"Torch: {player['inventory']['Torch']}")

    print("\nYour Path:")
    if len(score["path"]) == 0:
        print("No path recorded.")
    else:
        for step in score["path"]:
            print("-", step)

    print("====================================")


# -----------------------------
# Main game
# -----------------------------

def main():
    show_intro_story()

    player = choose_character()
    lives = MAX_LIVES
    score = create_score()

    print("\nYou chose:", player["name"])
    print(f"Attack: {player['attack']} | Defense: {player['defense']} | Perception: {player['perception']}")
    print(f"Lives: {lives}")

    print("\nYour lantern burns low as you step into The Labyrinth.")
    print("Some adventurers come here for treasure.")
    print("Others come because something hungry has started climbing upward.")

    # Floor 1
    lives, survived = play_floor(1, player, lives, score)

    if not survived:
        score["ending"] = "You died in The Labyrinth."
        show_final_score(player, lives, score)
        return

    if not ask_descend():
        score["ending"] = "You left The Labyrinth after Floor 1."
        print("\nYou leave The Labyrinth before the darkness swallows you.")
        print("You survived, but The Labyrinth remains unconquered.")
        show_final_score(player, lives, score)
        return

    # Floor 2
    lives, survived = play_floor(2, player, lives, score)

    if not survived:
        score["ending"] = "You died in The Labyrinth."
        show_final_score(player, lives, score)
        return

    if not ask_descend():
        score["ending"] = "You left The Labyrinth after Floor 2."
        print("\nYou leave The Labyrinth with your remaining lives.")
        print("Something below still waits in the dark.")
        show_final_score(player, lives, score)
        return

    # Floor 3
    lives, survived = play_floor(3, player, lives, score)

    if not survived:
        score["ending"] = "You died in The Labyrinth."
        show_final_score(player, lives, score)
        return

    # Final boss appears after the 8 room choices on Floor 3.
    fight_final_boss(player, lives, score)

    show_final_score(player, lives, score)


# This makes sure the game starts when we run the file.
main()
