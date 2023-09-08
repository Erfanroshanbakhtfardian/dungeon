import random
from conf import *

from game.utils.func import(
    clear_screen,
    move_down,
    move_left,
    move_right,
    move_up,
    is_door_nearby,
    distance,
    get_dragon_hear_direction,
    get_dragon_smell_direction,
    show_error
)

from game.helper.const import(
    RUNNING,
    GRID,
    DOOR_POSITION,
    DUNGEON_POSITION
)

from game.helper.exception import(
    DirectionNameError,
)

''' The execution function of the program '''
def main():
    print("Welcome to Dungeon and Dragon Game!")
    print("Find the dungeon or the door position to win the game.")
    
    # Prompt user to enter player position
    while True:
        try:
            player_x = int(input("Enter the x coordinate of your starting position (0-7): "))
            player_y = int(input("Enter the y coordinate of your starting position (0-7): "))

            if player_x < 0 or player_x > 7 or player_y < 0 or player_y > 7:
                raise ValueError()
            break
        except ValueError as e:
            logger.warning(" User invalid coordinates ...")
            print("-------------------")
            print("Invalid coordinates! Please Enter correct values 'JUST' between 0 and 7.")
            print("-------------------")

    player_position = (player_x, player_y)
    dragon_position = (0, 0)


    ''' The loop corresponding to the player's position,dragon's position,
    dungeon's position,door's position'''
    while RUNNING:
        for row in GRID:
            for cell in row:
                if cell == player_position:
                    print("X", end="  ")
                elif cell == dragon_position:
                    print("D", end="  ")
                elif is_door_nearby(player_position, DOOR_POSITION) and cell == DOOR_POSITION:
                    print("?", end="  ")    
                elif cell == DUNGEON_POSITION:
                    print("O", end=" ")    
                else:
                    print(".", end="  ")
            print()

        if player_position == dragon_position:
            print("Game over, you have been defeated by the dragon!")
            break
        elif player_position == DUNGEON_POSITION:
            print("Congratulations, you have reached the dungeon and won the game!")
            break   
        elif player_position == DOOR_POSITION:
            print("Congratulations, you have reached the door and won the game!")
            break
            
        direction = input("Enter a direction (up /down /left / right): ")
        clear_screen()

        ''' Call the appropriate move function based on the user's input '''
        try:
            if direction == "up":
                player_position = move_up(player_position)
            elif direction == "down":
                player_position = move_down(player_position)
            elif direction == "left":
                player_position = move_left(player_position)
            elif direction == "right":
                player_position = move_right(player_position)
            else:
                raise DirectionNameError()
        except DirectionNameError as e:
            logger.warning("User write invalid direction")
            show_error("please Enter correct direction! ")
            
        '''Check if the dragon can smell the player 3cells to player,
        and with 30% chance '''
        dragon_smell_direction = get_dragon_smell_direction(dragon_position, player_position)
        if dragon_smell_direction != "unknown":
            dragon_smell_distance = abs(dragon_position[0] - player_position[0]) + abs(dragon_position[1] - player_position[1])
            if dragon_smell_distance <= 3:
                print("The dragon smells you from the", dragon_smell_direction)

                
                # With a 30% probability, move towards the player immediately
                if random.random() <= 0.3:
                    if dragon_smell_direction == "up":
                        dragon_position = move_up(dragon_position)
                    elif dragon_smell_direction == "down":
                        dragon_position = move_down(dragon_position)
                    elif dragon_smell_direction == "left":
                        dragon_position = move_left(dragon_position)
                    elif dragon_smell_direction == "right":
                        dragon_position = move_right(dragon_position)
                    print("The dragon moves towards you!")
            else:
                print("The dragon doesn't smell anything")
        else:
            print("The dragon doesn't smell anything")

        ''' Check if the dragon can hear the player and with 90% chance move to player '''
        dragon_hear_direction = get_dragon_hear_direction(dragon_position, player_position)
        if dragon_hear_direction != "unknown":
            print("The dragon hears you from the", dragon_hear_direction)

            ''' With a 90% probability, move towards the player immediately '''
            if random.random() <= 0.9:
                if dragon_hear_direction == "up":
                    dragon_position = move_up(dragon_position)
                elif dragon_hear_direction == "down":
                    dragon_position = move_down(dragon_position)
                elif dragon_hear_direction == "left":
                    dragon_position = move_left(dragon_position)
                elif dragon_hear_direction == "right":
                    dragon_position = move_right(dragon_position)
                print("The dragon moves towards you!")
        else:
            print("The dragon doesn't hear anything")
            ''' Calculate the distance between the player's position and the dragon's position '''
            if distance(player_position, dragon_position) == 1:
                print("The dragon is in one of the adjacent cells")
            else:
                print("The dragon is not in one of the adjacent cells")
