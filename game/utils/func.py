import random
import os
from conf import *

from game.helper.exception import (
    DirectionLimitError,
)

from game.helper.const import(
    DRAGON_POSITION,
    PLAYER_POSITION
)


def move_up(position):
    try:
        x, y = position
        if y == 0:
            logger.info("User is in the top row. cannot move up.")
            show_error("You are in the top row. You cannot move up.")
            return position
        else:
            return (x, y - 1)
    except DirectionLimitError:
        logger.error("Invalid position")
    except Exception as e:
        logger.critical("Error 500! Please contact site support team.")

def move_down(position):
    try:
        x, y = position
        if y == 7:
            logger.info("User is in the bottom row. cannot move down.")
            show_error("You are in the bottom row. You cannot move down.")
            return position
        else:
            return (x, y + 1)
    except DirectionLimitError:
        logger.error("Invalid position")
        return None
    except Exception as e:
        logger.critical("Error 500! Please contact site support team.")

def move_right(position):
    try:
        x, y = position
        if x == 7:
            logger.info("User is in the rightmost column. cannot move right.")
            show_error("You are in the rightmost column. You cannot move right.")
            return position
        else:
            return (x + 1, y)
    except DirectionLimitError:
        logger.error("Invalid position")
        return None
    except Exception as e:
        logger.critical("Error 500! Please contact site support team.")

def move_left(position):
    try:
        x, y = position
        if x == 0:
            logger.info("User is in the leftmost column. cannot move left.")
            show_error("You are in the leftmost column. You cannot move left.")
            return position
        else:
            return (x - 1, y)
    except DirectionLimitError:
        logger.error("Invalid position")
        return None
    except Exception as e:
        logger.critical("Error 500! Please contact site support team.")

# Pythagoras = base * height /2 = s triangle
def distance(position1, position2):
    if position1 is None or position2 is None:
        return float('inf')
    else:
        (x1, y1) = position1
        (x2, y2) = position2
        return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

# Define the function to get the smell direction from the dragon to the player
def get_dragon_smell_direction(dragon_position, player_position):
    """Returns the direction of the player relative to the dragon based on smell"""
    try:
        if player_position[0] == dragon_position[0]:
            if player_position[1] < dragon_position[1]:
                return "up"
            else:
                return "down"
        elif player_position[1] == dragon_position[1]:
            if player_position[0] < dragon_position[0]:
                return "left"
            else:
                return "right"
        else:
            return "unknown"
    except TypeError:
        # handle case where player_position or dragon_position is None or not iterable
        return "unknown"
    
# # Define the function to get the hear direction from the dragon to the player when 2 cells left for the player
def get_dragon_hear_direction(dragon_position, player_position):
    """Returns the direction of the player relative to the dragon based on sound"""
    try:
        if (abs(player_position[0] - dragon_position[0]) <= 2) and (abs(player_position[1] - dragon_position[1]) <= 2):
            if player_position[0] == dragon_position[0]:
                if player_position[1] < dragon_position[1]:
                    return "up"
            else:
                return "down"
        elif player_position[1] == dragon_position[1]:
            if player_position[0] < dragon_position[0]:
                return "left"
            else:
                return "right"
        else:
            return "unknown"
    except TypeError:
        return "unknown"

# Define a function to check if the door is nearby
def is_door_nearby(player_position, door_position):
    if distance(player_position, door_position) <= 2:
        return True
    else:
        return False

def clear_screen():
    return os.system('cls' if os.name == 'nt' else 'clear')

def show_error(message):
    print(f"Error: {message}!")


def detect_dragon_smell(dragon_position, player_position):
    direction = get_dragon_smell_direction(dragon_position, player_position)
    if direction != "unknown":
        distance = abs(dragon_position[0] - player_position[0]) + abs(dragon_position[1] - player_position[1])
        if distance <= 3:
            return f"The dragon smells you from the {direction}."
    return None
#usage
# DRAGON_POSITION = (0, 0)
# PLAYER_POSITION = (6, 8)
result = detect_dragon_smell(DRAGON_POSITION, PLAYER_POSITION)
if result is not None:
    print(result)


def move_dragon_towards_player(dragon_position, player_position, dragon_smell_direction):
    if random.random() <= 0.3 and dragon_smell_direction != "unknown":
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
    return dragon_position
# Usage:
# DRAGON_POSITION = (0, 0)
# PLAYER_POSITION = (6, 8)
dragon_smell_direction = "up"
DRAGON_POSITION = move_dragon_towards_player(DRAGON_POSITION, PLAYER_POSITION, dragon_smell_direction)


def move_dragon_towards_player_if_heard(dragon_position, player_position):
    dragon_hear_direction = get_dragon_hear_direction(dragon_position, player_position)
    if dragon_hear_direction != "unknown":
        print("The dragon hears you from the", dragon_hear_direction)
        # With a 90% probability, move towards the player immediately
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
    return dragon_position
# Usage:
# DRAGON_POSITION = (0, 0)
# PLAYER_POSITION = (6, 8)
# DRAGON_POSITION = move_dragon_towards_player_if_heard(DRAGON_POSITION, PLAYER_POSITION)

def get_valid_player_position_input():
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
    return (player_x, player_y)
# Usage:
PLAYER_POSITION = (6, 8)
DRAGON_POSITION = (0, 0)
