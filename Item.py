import tkinter as tk

class Item():
    def __init__(self,item_name,file):
        """
               Constructor method.
                       :param item_name: name of item
                   """
        self.item_name=item_name
        try:
            self.image = tk.PhotoImage(file=file).subsample(6,6)
        except:
            pass

        self.depiction=None

    def get_name(self):
        """
                           Fetch a item.
                       :return: name of item
                       """
        return self.item_name

    def set(self,item_name):
        """
                        setting name of the item.
                       :return: None
                       """
        self.item_name=item_name

    def get_description(self):
        """
                    Fetch a  item description.
                :return: item description
                """
        return self.depiction

    def set_description(self,item_depiction):
        """
                    set a item description.
                :return: none
                """
        self.depiction=item_depiction

    def describe(self):
        """
                           describing item name and properties .
                       :return: none
                       """

        print('The ' + self.item_name +' must be used to' + self.depiction)