#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

# Example module
# Copyright (C) 2014 Musikhin Andrey <melomansegfault@gmail.com>
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import kivy
from kivy.config import Config
Config.set("input", "mouse", "mouse, disable_multitouch")
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from table import Table



class MainScreen(BoxLayout):
    """docstring for MainScreen"""
    def __init__(self):
        super(MainScreen, self).__init__()
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_keyboard_down)
        self.my_table = Table()
        self.my_table.cols = 2
        self.my_table.add_button_row('123', '456')
        for i in range(110):
            self.my_table.add_row([Button, {'text': 'button%s' % i,
                                            'color_widget': [0, 0, 0.5, 1],
                                            'color_click': [0, 1, 0, 1]
                                            }], 
                                  [TextInput, {'text': 'textinput%s' % i,
                                               'color_click': [1, 0, .5, 1]
                                               }])
        self.my_table.label_panel.visible = False
        self.my_table.label_panel.height_widget = 50
        self.my_table.number_panel.auto_width = False
        self.my_table.number_panel.width_widget = 100
        self.my_table.number_panel.visible = False
        self.my_table.choose_row(3)
        self.my_table.del_row(5)
        self.my_table.grid.color = [1, 0, 0, 1]
        self.my_table.label_panel.color = [0, 1, 0, 1]
        self.my_table.number_panel.color = [0, 0, 1, 1]
        self.my_table.scroll_view.bar_width = 10
        self.my_table.scroll_view.scroll_type = ['bars']
        self.my_table.grid.cells[0][0].text = 'edited button text'
        self.my_table.grid.cells[1][1].text = 'edited textinput text'
        self.my_table.grid.cells[3][0].height = 100
        self.my_table.label_panel.labels[1].text = 'New name'
        print ("ROW COUNT:", self.my_table.row_count)
        self.add_widget(self.my_table)

    def _keyboard_closed(self):
        pass

    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        """ Method of pressing keyboard  """
        if keycode[0] == 273:   # UP
            print (keycode)
            self.my_table.scroll_view.up()
        if keycode[0] == 274:   # DOWN
            print (keycode)
            self.my_table.scroll_view.down()
        if keycode[0] == 281:   # PageDown
            print (keycode)
            self.my_table.scroll_view.pgdn()
        if keycode[0] == 280:   # PageUp
            print (keycode)
            self.my_table.scroll_view.pgup()
        if keycode[0] == 278:   # Home
            print (keycode)
            self.my_table.scroll_view.home()
        if keycode[0] == 279:   # End
            print (keycode)
            self.my_table.scroll_view.end()



class TestApp(App):
    """ App class """
    def build(self):
        return MainScreen()

    def on_pause(self):
        return True



if __name__ in ('__main__', '__android__'):
    TestApp().run()