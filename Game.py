from PIL import Image, ImageTk
import tkinter as tk
from tkinter import *
from Room import Room

from Character import Enemy
from Character import King
from Item import Item
from pathlib import Path
import sys


class Game:

    def __init__(self, root):
        """
        Initialises the game.
        """
        self.root = root
        self.create_rooms()
        self.current_room = self.hall_1
        self.create_enemy()
        self.create_item()
        self.set_character()
        self.set_item()
        self.dweller = self.current_room.get_character()
        self.current_item = self.current_room.get_item()


    def create_rooms(self):
        """
            Sets up all room assets.
        :return: list
        """
        self.hall_1 = Room("Perspolis Hall", str(Path().absolute()) + '\\hall images\\hall 1.PNG')
        self.hall_2 = Room("Apadana Hall", str(Path().absolute()) + '\\hall images\\hall 2.PNG')
        self.hall_3 = Room("Gate of all nations", str(Path().absolute()) + '\\hall images\\hall 3.PNG')
        self.hall_4 = Room(" Throne hall", str(Path().absolute()) + '\\hall images\\hall 4.PNG')
        self.hall_5 = Room('Tachara Hall', str(Path().absolute()) + '\\hall images\\hall 5.PNG')
        self.hall_6 = Room('Atousa Hall', str(Path().absolute()) + '\\hall images\\hall 6.PNG')
        self.hall_7 = Room('Babylon Hall', str(Path().absolute()) + '\\hall images\\hall 7.PNG')
        self.corridor = Room('Cage', str(Path().absolute()) + '\\hall images\\corridor.PNG')

        self.hall_1.set_exit("west", self.hall_2)
        self.hall_2.set_exit("east", self.hall_1)
        self.hall_2.set_exit("north", self.hall_3)
        self.hall_3.set_exit("south", self.hall_2)
        self.hall_3.set_exit('east', self.hall_4)
        self.hall_4.set_exit('west', self.hall_3)
        self.hall_4.set_exit('north', self.hall_5)
        self.hall_5.set_exit('south', self.hall_4)
        self.hall_5.set_exit('west', self.hall_6)
        self.hall_6.set_exit('east', self.hall_5)
        self.hall_6.set_exit('north', self.hall_7)
        self.hall_7.set_exit('south', self.hall_6)
        self.corridor.set_exit('west', self.hall_7)
        self.hall_7.set_exit('east', self.corridor)

        return [self.hall_1, self.hall_2, self.hall_3, self.hall_4, self.hall_5, self.hall_6, self.hall_7,
                self.corridor]

    def create_enemy(self):
        """
                   Sets up all enemy assets.
               :return: list of enemies and king
               """
        self.lion = Enemy('Lion', 'Big savage one', str(Path().absolute()) + '\\enemy images\\lion.PNG')
        self.lion.set_conversation('Where is the Rostam')
        self.lion.set_weakness('bite')
        self.dragon = Enemy('Dragon', 'Flame from his mouth could turn everything to ash', str(Path().absolute()) + '\\enemy images\\dragon.PNG')
        self.dragon.set_conversation('Rostam, you must atone for killing my friend lion')
        self.dragon.set_weakness('sword')
        self.wizard = Enemy('Wizard', 'manipulating Rostam to kill Rakhs', str(Path().absolute()) + '\\enemy images\\wizard.PNG')
        self.wizard.set_conversation('This room will be your grave')
        self.wizard.set_weakness('coconutcannon')
        self.king = Enemy('King', 'He is invulnerable', str(Path().absolute()) + '\\enemy images\\king.PNG')
        self.king.set_conversation('With the help of Zerosht, I will defeat you')
        self.king.set_weakness('punch')
        self.monster = Enemy('Black Monster', 'He has two head', str(Path().absolute()) + '\\enemy images\\black monster.PNG')
        self.monster.set_conversation('Uaaa....Yuhaaaaa')
        self.monster.set_weakness('ax')

        self.w_monster = Enemy('White Monster', 'He has three head', str(Path().absolute()) + '\\enemy images\\white monster.PNG')
        self.w_monster.set_conversation('Uaaa....Yuhaaaaa')
        self.w_monster.set_weakness('venom')

        self.persian_king = King('Keykavos', 'Persian empire', str(Path().absolute()) + "\\king of persia.PNG")

        return [self.lion, self.dragon, self.wizard, self.king, self.monster, self.w_monster]

    def set_character(self):
        """
                   assign characters to rooms.
               :return: None
               """
        self.hall_1.set_character(self.lion)
        self.hall_3.set_character(self.dragon)
        self.hall_4.set_character(self.wizard)
        self.hall_5.set_character(self.king)
        self.hall_6.set_character(self.monster)
        self.hall_7.set_character(self.w_monster)
        self.corridor.set_character(self.persian_king)

    def create_item(self):
        """
                   Sets up all item assets.
               :return: list of items
               """
        self.bite = Item('bite', str(Path().absolute()) +'\\item images\\bite.PNG')
        self.bite.set_description('It is the only you could kill lion')
        self.sword = Item('sword', str(Path().absolute()) + '\\item images\\sword.PNG')
        self.sword.set_description(' It is build in Perspolis and located in the Satrap district')
        self.coconutcannon = Item('coconutcannon', str(Path().absolute()) + '\\item images\\coconut.PNG')
        self.coconutcannon.set_description(' This deadly machine was made in Roman empire and imported in persia')
        self.punch = Item('punch', str(Path().absolute()) + '\\item images\\punch.PNG')
        self.punch.set_description('hand of Rostam are deadly')
        self.ax = Item('ax', str(Path().absolute()) + '\\item images\\ax.PNG')
        self.ax.set_description('It is the only way you could kill black monster')
        self.venom = Item('venom', str(Path().absolute()) + '\\item images\\venom.PNG')
        self.venom.set_description('When he sleeps use this poison to kill it')

        return [self.bite, self.sword, self.coconutcannon, self.punch, self.ax, self.venom]

    def set_item(self):
        """
                          assign items to rooms.
                      :return: None
                      """
        self.hall_1.set_item(self.bite)
        self.hall_3.set_item(self.sword)
        self.hall_4.set_item(self.coconutcannon)
        self.hall_5.set_item(self.punch)
        self.hall_6.set_item(self.ax)
        self.hall_7.set_item(self.venom)

    def print_welcome(self):
        """
        Return the welcome message as a string.
        :return: string
        """
        self.msg = \
            f'You are in the persian land \n \
        Help Rostam to find his king. \n\n \
        for game rules and exit use menubar. \n\
        Your command words are: {self.show_command_words()}.'
        return self.msg

    def show_command_words(self):
        """
            Show a list of available commands.
        :return: list of commands as a string
        """
        return [ 'go', 'fight', 'rule','exit']



    def do_go_command(self, second_word):
        """
                            Performs the go command.
                        :param second_word: the direction player wishes to go
                        :return: description of hall that player enters
                        """

        if self.current_room.get_character() is None:
            self.current_room.is_locked = False

        if self.current_room.is_locked:
            return f"Hall is locked  \n \
                   First fight with enemy"

        if second_word == None:
            return 'Go where?'

        next_room = self.current_room.get_exit(second_word)

        if next_room == None:
            return 'There is no door!'
        else:
            self.current_room = next_room

            if self.current_room == self.corridor:
                return "cage"

            return f'{self.current_room.get_long_description()}'



    def do_fighting(self, command):
        """
                            Performs the FIGHT command.
                        :param command: the tool that player chooses to fight with the enemy
                        :return: message
                        """

        if self.dweller is not None and isinstance(self.dweller, Enemy):
            second_word = command

            if self.current_room.get_character().fight(second_word) == True:
                self.msg = \
                    f'Good job, Nice shot\n \
                     You win and you can continue to the next hall'
                self.root.history(self.msg)
                self.current_room.is_locked = False

                if self.hall_7 == self.current_room:
                   self.msg='Congratulation You killed all the devils. for saving king just continue to the next room '
                   self.root.history( self.msg)
                   return self.msg
                else:
                    return self.msg
            else:

                self.msg = \
                    f"Sorry, Wrong hit\nGame over"
                self.root.history(self.msg)
                self.root.download_file(self.root.string)

                self.root.show_dialog()

                return self.msg


        else:
            self.current_room.is_locked = False
            return 'There is no enemy in this Hall'
