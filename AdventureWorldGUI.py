import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import Menu
from Game import Game
from datetime import datetime
from Character import King



class App():

    # Creates a Frame for the application and populates the GUI...
    def __init__(self, root):

        self.master = root
        menu = tk.Menu(self.master)
        self.game = Game(self)
        # Create menubar and assign exit and rules command to it
        Filemenu = Menu(menu, tearoff=0)
        menu.add_cascade(label='File', menu=Filemenu)
        Filemenu.add_command(label='rules', command=self.rules)
        Filemenu.add_command(label='exit', command=self.master.destroy)
        self.master.config(menu=menu)

        # Create two left and right frames
        # right frame is the parent frame of frame1,2,3 and 4
        # left frame is the parent frame of frame 5

        self.leftframe=tk.Frame(root,bg='gray',height=1000,width=280,borderwidth=2)
        self.leftframe.pack_propagate(0)
        self.rightframe = tk.Frame(root, bg='light gray', height=1000, width=1000, borderwidth=2)
        self.rightframe.pack_propagate(0)

        self.frame1 = tk.Frame(self.rightframe, bg='gray',width=600, height=300, borderwidth=2)
        self.frame1.pack_propagate(0)  # Prevents resizing
        self.frame2 = tk.Frame(self.rightframe,bg='light gray' ,width=600, height=300, borderwidth=2)
        self.frame2.grid_propagate(0)  # Prevents resizing
        self.frame3 = tk.Frame(self.rightframe,bg='light gray' ,width=600, height=300, borderwidth=2)
        self.frame4 = tk.Frame(self.rightframe,bg='light gray' ,width=800, height=300, borderwidth=2)
        self.frame5 = tk.Frame(self.leftframe, bg='white',width=600, height=300, borderwidth=2)

        # This packs all frames into the root window...
        self.leftframe.pack(side=LEFT, pady=1)
        self.rightframe.pack(side=RIGHT, pady=1)
        self.frame1.pack()
        self.frame2.pack()
        self.frame3.pack()
        self.frame4.pack()
        self.frame5.pack()

        self.action_list=[]
        self.string=''

        self.frame1.columnconfigure(0, pad=5)
        self.frame1.columnconfigure(1, pad=5)
        self.frame1.columnconfigure(2, pad=5)
        self.frame1.columnconfigure(3, pad=5)
        self.frame1.rowconfigure(0, pad=5)
        self.frame1.rowconfigure(1, pad=5)
        self.frame1.rowconfigure(2, pad=5)
        self.frame1.rowconfigure(3, pad=5)
        self.frame1.rowconfigure(4, pad=5)

        self.frame2.columnconfigure(0, pad=5)
        self.frame2.columnconfigure(1, pad=5)
        self.frame2.rowconfigure(0, pad=5)
        self.frame2.rowconfigure(1, pad=5)
        self.frame2.rowconfigure(2, pad=5)

        self.frame3.columnconfigure(0, pad=10)
        self.frame3.columnconfigure(1, pad=10)
        self.frame3.rowconfigure(0, pad=10)
        self.frame3.rowconfigure(1, pad=10)
        self.frame3.rowconfigure(2, pad=10)

        # create and pack hall label and assign it to frame 2
        self.lbl_hall = Label(self.frame2)
        self.lbl_hall.pack()
        # create and pack enemy label and assign it to frame 3
        self.lbl_enemy = Label(self.frame3)
        self.lbl_enemy.pack()
        # create and pack item label and assign it to frame 4
        self.lbl_item = Label(self.frame4)
        self.lbl_item.pack()

        # Now add some useful widgets...
        self.text_area1 = tk.Label(self.frame1, text='', borderwidth=2)
        self.text_area1.grid(row=0, column=2)

        self.build_GUI()

    def rules(self):
        """
                     perform RULES command in the menubar and Display some useful text about games' rule.
                     :return: None
                        """
        messagebox.showinfo('Rules', 'for travelling between halls you should defeat your enemy at your current hall.\n\n If you could not guess correct item, you should start from beginning.')

    def history(self,history):
        """
                    create and pack history label to frame 5 and perform recording
                :param history: string that add all record of the buttons(commands)
                :return: None
                """
        self.lbl_hisory=tk.Label(self.frame5)
        self.lbl_hisory.configure(text=history)
        self.lbl_hisory.pack()


        self.string += history+'\n'



    def download_file(self,action_list):
        """
                            perform logging
                        :param action_list: string
                        :return: None
                        """

        file_download=datetime.now()
        file_download_string=str(file_download)
        file_download_string=file_download_string.replace('-','')
        file_download_string=file_download_string.replace('','')
        file_download_string=file_download_string.replace(':','')
        file_download_string=file_download_string.replace('-','')
        file_name=file_download_string+'readme.txt'
        file=open(file_name,'w')
        file.write(str(action_list))




    def build_GUI(self):
        """
                          create GUI.
                      :return: None
                      """

        self.built_directions()

        self.text_area1.configure(text=self.game.print_welcome())

    def destroy_fight_button(self):
        """
                          reomve fight button.
                      :return: None
                      """
        try:
            self.button_fight.grid_forget()
        except:
            pass

    def create_fight_button(self):
        """
                    create fight button and assign it to frame 1.
                :return: None
                """
        try:
            self.button_fight.grid_forget()
        except:
            pass
        self.button_fight = Button(self.frame1, text='Fight', command=self.fight_enemy)
        self.button_fight.grid(row=2, column=2)

    def built_directions(self):
        """
                    create buttons of directions
                :return: None
                """
        self.goSouth = tk.Button(self.frame1, text='south', command=lambda: self.process_direction('south'))
        self.goSouth.grid(row=4, column=1)

        self.gowest = tk.Button(self.frame1, text='west', command=lambda: self.process_direction('west'))
        self.gowest.grid(row=3, column=1)

        self.goNorth = tk.Button(self.frame1, text='north', command=lambda: self.process_direction('north'))
        self.goNorth.grid(row=1, column=1)

        self.goEast = tk.Button(self.frame1, text='east', command=lambda: self.process_direction('east'))
        self.goEast.grid(row=2, column=1)

    def process_direction(self, direction):
        """
                    process the direction
                 :param direction: direction the player wishes to go
                :return: None
                """
        direction = direction.lower()
        x = self.game.do_go_command(direction)

        self.text_area1.configure(text=x)
        self.history(x)
        self.lbl_hall.configure(image=self.game.current_room.image)
        self.remove_fight_option()

        if self.game.current_room.get_character() is not None and isinstance is not (self.game.current_room.get_character(),King):
            self.create_fight_button()
        else:
            self.destroy_fight_button()

        try:
            self.lbl_enemy.configure(image=self.game.current_room.get_character().image)
        except:
            self.lbl_enemy.configure(image='')

        if self.game.current_room.description == 'Cage':

            self.final_step()

    def final_step(self):
        """
                    remove all the buttons in the cage room
                :return: None
                """
        self.text_area1.configure(text="Congratulations !!! You have saved the king ")
        self.destroy_fight_button()
        self.button_fight.grid_forget()
        self.last_room_dialog()
        self.gowest.grid_forget()
        self.goEast.grid_forget()
        self.goSouth.grid_forget()
        self.goNorth.grid_forget()

    def remove_fight_option(self):
        """
                            remove fight button for a hall
                        :return: None
                        """
        try:
            self.fight_options.pack_forget()
        except:
            pass

    def fight_enemy(self):
        """
                                   perform the fight button
                               :return: None
                               """
        self.remove_fight_option()
        if self.game.current_room.get_character() == None:
            self.text_area1.configure(text='There is no one to fight')
            return

        self.fight_options = Label(self.frame4)
        self.fight_options.pack()

        for index, item in enumerate(self.game.create_item()):
            self.fight_item = Button(self.fight_options, text=item.item_name,
                                     command=lambda action=item.item_name:
                                     self.text_area1.configure(text=self.game.do_fighting(action)))

            self.fight_item.configure(image=item.image)
            self.fight_item.pack(side=LEFT)


    def do_command(self):
        command = self.cmd_area.get()  # Returns a 2-tuple
        self.process_command(command)

    def get_command_string(self, input_line):
        """
            Fetches a command (borrowed from old TextUI).
        :return: a 2-tuple of the form (command_word, second_word)
        """
        word1 = None
        word2 = None
        if input_line != "":
            all_words = input_line.split()
            word1 = all_words[0]
            if len(all_words) > 1:
                word2 = all_words[1]
            else:
                word2 = None
            # Just ignore any other words
        return (word1, word2)

    def process_command(self, command):
        command_word, second_word = self.get_command_string(command)

        if command_word != None:
            command_word = command_word.upper()

            if command_word == "GO":
                self.text_area1.configure(text=self.game.do_go_command(second_word))


            elif command_word == 'FIGHT':
                self.text_area1.configure(text= self.game.do_fighting(second_word))
            else:
                # Unknown command...
                self.text_area1.configure(text="Don't know what you mean.")

    def last_room_dialog(self):
        """
                                           show message for ending game at last room
                                       :return: None
                                       """
        tk.messagebox.showinfo('Exit application','For exit please press ok')
        self.master.quit()

    def show_dialog(self):
        """
                                   show message for ending game when player guesses wrongly
                               :return: None
                               """
        tk.messagebox.showinfo('Exit Application', 'Sorry, Wrong hit\nGame over. Press Ok to exit')
        #self.download_file(self.history)

        self.master.quit()


def main():
    win = tk.Tk()  # Create a window
    win.title("Adventure World with GUI")  # Set window title
    win.geometry("800x800")  # Set window size
    win.resizable(False, False)  # Both x and y dimensions...

    # Create the GUI as a Frame and attach it to the window...
    App(win)

    # Call the GUI mainloop...
    win.mainloop()


if __name__ == "__main__":
    main()
