'''
This module implements an adventure game.
'''
import random
def display_player_status(player_health):
    """Display player's health status"""
    print(f"Your current health: {player_health}")

def handle_path_choice(player_health):
    """Player chooses a path"""
    path = random.choice(["left", "right"])
    if path == "left":
        print("You encounter a friendly gnome who heals you for 10 health points.")
        updated_player_health = min(100, player_health + 10)
    else:
        print("You fall into a pit and lose 15 health points.")
        updated_player_health = max(0, player_health - 15)
        if updated_player_health == 0:
            print("You are barely alive!")
    return updated_player_health

def player_attack(monster_health):
    """Player attacks the monster"""
    print("You strike the monster for 15 damage!")
    updated_monster_health = monster_health - 15
    return updated_monster_health

def monster_attack(player_health):
    """Monster attacks the player"""
    if random.random() < 0.5:
        print("The monster lands a critical hit for 20 damage!")
        updated_player_health = player_health - 20
    else:
        print("The monster hits you for 10 damage!")
        updated_player_health = player_health - 10
    return updated_player_health

def combat_encounter(player_health, monster_health, has_treasure):
    """Combat encounter between player and monster"""
    while player_health > 0 and monster_health > 0:
        monster_health = player_attack(monster_health)
        if monster_health <= 0:
            print("You defeated the monster!")
            return has_treasure
        player_health = monster_attack(player_health)
        display_player_status(player_health)
        if player_health <= 0:
            print("Game Over!")
            return False
    return has_treasure

def check_for_treasure(has_treasure):
    """Check if player has the treasure"""
    if has_treasure:
        print("You found the hidden treasure! You win!")
    else:
        print("The monster did not have the treasure. You continue your journey.")

def acquire_item(inventory,item):
    """Add items to the inventory"""
    inventory.append(item)
    print(f"You acquired a {item}!")
    updated_inventory_list = [item]
    return updated_inventory_list

def display_inventory(inventory):
    """Displays the player's current inventory"""
    if inventory == []:
        print("Your inventory is empty")
    else:
        for item in inventory:
            print(item)

def enter_dungeon(player_health, inventory, dungeon_rooms):
    """Simulates the player exploring the dungeon rooms"""
    for room in dungeon_rooms:
        room_description, item, challenge_type, challenge_outcome = room
        print(room_description)
        if item != None:
            acquire_item(inventory,item)
        if challenge_type == "puzzle":
            print("You encounter a puzzle!")
            choice = input("Do you want to solve or skip the puzzle?")
            if choice == "solve":
                success = random.choice([True,False])
                print(challenge_outcome[0])
                if not success:
                    print(challenge_outcome[1])
                    player_health += challenge_outcome[2]
        elif challenge_type == "trap":
            print("You see a potential trap!")
            choice = input("disarm or bypass the trap?")
            if choice == "disarm":
                success = random.choice([True,False])
                print(challenge_outcome[0])
                if not success:
                    print(challenge_outcome[1])
                    player_health += challenge_outcome[2]
        else:
            print("There doesn't seem to be a challenge in this room. You move on.")
        if player_health <= 0:
            player_health = 0
            print("You are barely alive!")
        display_inventory(inventory)
    updated_player_health = print(player_health)
    return updated_player_health, inventory

def main():
    """Main function"""
    player_health = 100
    monster_health = 70
    has_treasure = random.choice([True, False])
    player_health = handle_path_choice(player_health)
    treasure_obtained_in_combat = combat_encounter(player_health, monster_health, has_treasure)
    check_for_treasure(treasure_obtained_in_combat)
    inventory = []
    dungeon_rooms = [("A dusty old library", "key", "puzzle", ("You solved the puzzle!", "The puzzle remains unsolved.", -5)), ("A narrow passage with a creaky floor", None, "trap", ("You skillfully avoid the trap!", "You triggered a trap!", -10)), ("A grand hall with a shimmering pool", "healing potion", "none", None), ("A small room with a locked chest", "treasure", "puzzle", ("You cracked the code!", "The chest remains stubbornly locked.", -5))]
    enter_dungeon(player_health, inventory, dungeon_rooms)
if __name__ == "__main__":
    main()
