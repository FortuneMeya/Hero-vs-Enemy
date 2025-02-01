from map import Map
from enemy import Enemy
from hero import Hero
import check_input
import random



def main():
    user_name = str(input("What is your name, traveler? "))
    user = Hero(user_name)
    dungeon = Map()
    dungeon.reveal(user.loc)


    while user.hp > 0:
        print(user)
        dungeon.show_map(user.loc)

        direction = check_input.get_int_range('\n1. Go North\n2. Go South\n3. Go East\n4. Go West\n5. Quit\nEnter choice:  ', 1, 5)
        if direction == 1:
            map_char = user.go_north()
        elif direction == 2:
            map_char = user.go_south()
        elif direction == 3:
            map_char = user.go_east()
        elif direction == 4:
            map_char = user.go_west()
        else:
            return
       
        print(f'map char: {map_char}')

        
        if map_char == 'm':
            monster = Enemy()
            print(f'You encounter a {monster}')
            fight = True
            while fight:
                attack_or_run = check_input.get_int_range(f'1. Attack {monster.name}\n2. Run Away\nEnter choice: ', 1, 2)

                if attack_or_run == 1:
                    user.attack(monster)
                    if monster.hp > 0:
                        monster.attack(user)
                    elif monster.hp == 0:
                        print(f'You have slain a {monster.name}')
                        dungeon.remove_at_loc(user.loc)
                        fight = False
                else:
                    print('You ran away!')
                    moved = False 
                    while not moved:
                        direction = random.randint(1, 4)
                        if direction == 1:
                            map_char_rand =user.go_north()
                        elif direction == 2:
                            map_char_rand = user.go_south()
                        elif direction == 3:
                            map_char_rand = user.go_east()
                        else:
                            map_char_rand = user.go_west()

                        if map_char_rand != 'o':
                            moved = True
                    fight = False
        elif map_char == 'o':
            print('You cannot go that way...')
        elif map_char == 'n':
            print('There is nothing here...')
        elif map_char == 'i':
            print('You found a Health potion! You drink it to restore your health.')
            user.heal()
            dungeon.remove_at_loc(user.loc)
        elif map_char == 's':
            print('You come back to the start')
        elif map_char == 'f':
            print('Congratulations! You found the exit.\nGame Over')
            return
        
        dungeon.reveal(user.loc)
        print("")
    print('You died\nGame Over')

main()


