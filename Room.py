import tkinter as tk
"""
    Create a room described "description". Initially, it has
    no exits. The 'description' is something like 'kitchen' or
    'an open court yard'.
"""

class Room:

    def __init__(self, description,file):
        """
            Constructor method.
        :param description: Text description for this room
        """
        self.description = description
        self.exits = {}  # Dictionary
        self.character_name = None


        self.is_locked = True

        self.item_name = None
        try:
            self.image = tk.PhotoImage(file=file).subsample(2,2)
        except:
            pass

    def set_character(self,character_name):
        """
                    adds a character in room.
                :param character_name: name of character in a room
                :return: None
                """
        self.character_name=character_name

    def get_character(self):
        """
                    Fetch a character.
                :return: name of character in the room
                """
        return self.character_name

    def get_item(self):
        return self.item_name


    def set_item(self, item_name):
        """
                            adds an item in room.
                        :param item_name: name of item in a room
                        :return: None
                        """
        self.item_name = item_name

    def set_exit(self, direction, neighbour):
        """
            Adds an exit for a room. The exit is stored as a dictionary
            entry of the (key, value) pair (direction, room).
        :param direction: The direction leading out of this room
        :param neighbour: The room that this direction takes you to
        :return: None
        """
        self.exits[direction] = neighbour

    def get_short_description(self):
        """
            Fetch a short text description.
        :return: text description
        """
        return self.description

    def get_long_description(self):
        """
            Fetch a longer description including available exits.
        :return: text description
        """
        return f'Location: {self.description}, Exits: {self.get_exits()}.'

    def get_exits(self):
        """
            Fetch all available exits as a list.
        :return: list of all available exits
        """
        all_exits = list(self.exits.keys())
        return all_exits

    def get_exit(self, direction):
        """
            Fetch an exit in a specified direction.
        :param direction: The direction that the player wishes to travel
        :return: Room object that this direction leads to, None if one does not exist
        """
        if direction in self.exits:
            return self.exits[direction]
        else:
            return None
