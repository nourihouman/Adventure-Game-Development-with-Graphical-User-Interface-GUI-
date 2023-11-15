
import unittest as ut
from Game import Game
from Room import Room
from AdventureWorldGUI import App
from Character import Enemy
from Item import Item


class UnitTest (ut.TestCase):
    UI: App = App
    game: Game = Game(UI)

    hall_test1 = Room("hall_room1",'')
    hall_test2 = Room("hall_room2",'')

    enemy_test=Enemy('enemy_1',None,'')
    enemy_test2=Enemy('enemy_2',None,'')

    item_test=Item('item_1','')
    item_test2=Item('item_2','')

    hall_test1.set_character(enemy_test)
    hall_test2.set_character(enemy_test2)

    hall_test1.set_item(item_test)
    hall_test2.set_item(hall_test2)

    game.current_room = hall_test1
    hall_test1.set_exit("west", hall_test2)
    hall_test2.set_exit("east", hall_test1)

    def test_go(self):
        go_command = ( 'west')
        self.game.do_go_command(go_command)
        self.assertEqual(self.game.current_room, self.hall_test1, 'Test pass because due to the lock current room remains same')


    def test_exit(self):
        self.assertEqual(self.hall_test1, self.hall_test2.exits["east"], "Test failed, exit goes to different hall")

    def test_enemy(self):
        self.assertNotEquals(self.hall_test1.character_name,self.hall_test2.character_name,'Test failed,enemy is in two hall are same')

    def test_item(self):
        self.assertNotEquals(self.hall_test1.item_name,self.hall_test2.item_name,'Test failed,item in two hall are same')


if __name__ == "__main__":
    UnitTest.main()