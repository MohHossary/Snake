import keyboard

from keyboardhandler import KeyboardHandler


class LibkeyboardKeyboardHandler(KeyboardHandler):

    up: bool = False
    down: bool = False
    left: bool = False
    right: bool = False

    def __init__(self):
        keyboard.on_press_key('up', self.__set_up_flag)
        keyboard.on_press_key('down', self.__set_dn_flag)
        keyboard.on_press_key('left', self.__set_lt_flag)
        keyboard.on_press_key('right', self.__set_rt_flag)

    def __set_up_flag(self, _: keyboard.KeyboardEvent):
        self.up = True

    def __set_dn_flag(self, _: keyboard.KeyboardEvent):
        self.down = True

    def __set_lt_flag(self, _: keyboard.KeyboardEvent):
        self.left = True

    def __set_rt_flag(self, _: keyboard.KeyboardEvent):
        self.right = True

    def is_up_pressed(self):
        up = self.up
        self.up = False
        return up

    def is_down_pressed(self):
        dn = self.down
        self.down = False
        return dn

    def is_left_pressed(self):
        lt = self.left
        self.left = False
        return lt

    def is_right_pressed(self):
        rt = self.right
        self.right = False
        return rt

    def clear_flags(self) -> None:
        self.up = False
        self.down = False
        self.left = False
        self.right = False

