
from PIL import Image,ImageTk
import tkinter as tk
from tkinter import *

"""
Create some characters that described. The 'described'
is something like the name and power of a character
"""
class Character:

    def __init__(self,character_name,character_power,file):
        """
        Constructor method.
                :param character_name: name of character
                :param character_power: power that character has
            """
        self.character_name=character_name
        self.character_power=character_power
        self.conversation=None
        try:
            self.image=tk.PhotoImage(file=file).subsample(3,3)
        except:
            pass


    def describe(self):
        """
                describe this character and its power.
                :return: none
                """
        print(self.character_name)
        print(self.character_power)

    def set_conversation(self,conversation):
        """
                    what this character going to say when it is talked to.
                :param conversation: words that character is going to say
                :return: None
                """
        self.conversation=conversation

    def speech_with(self):
        """
                    speech with this character.
                :return: None
                """
        if self.conversation is not None:
            return self.character_name + ' says :' + self.conversation
        else:
            return 'this hall does not has a creature'

    def fight(self,fight_item):
        """
                    Fight with this character
                :param fight_item: the tool character wants to use for fight
                :return: Boolean
                """
        return self.character_name
        return True

"""
        this class in subclass of character class
        therefore we wont repeat same attribute here
            """
class Enemy(Character):

    def __init__(self,character_name,character_power,file):
        super().__init__(character_name,character_power,file)
        self.weakness=None

    def set_weakness(self,enemy_weakness):
        """
                defining weakness for defeating enemy
                        :param enemy_weakness: weakness of enemy
                        :return: None
                    """
        self.weakness=enemy_weakness

    def get_weakness(self):
        """
                           Fetch a weakness.
                       :return: weakness of character
                       """
        return self.weakness

    def fight(self,fight_item):
        if fight_item==self.weakness:
            self.character_name + ' is killed by ' + fight_item
            return True
        else:
            'you could not kill ' +  self.character_name  + ' in this way'
            return False

class King(Character):
    def __init__(self, character_name, character_power,file):
        super().__init__(character_name, character_power,file)

    def saving(self):
        """
                        appreciation of king to hero
                                :return: None
                            """
        return (self.character_name + ' appreciates Rostam  saving his life')

