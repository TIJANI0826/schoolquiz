from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.lang import Builder

# Automating the builder function to load all
# Add as many .data file in the data folder and they will automatically be loaded by Builder
from os import listdir

kv_path = './data/'
for kv in listdir(kv_path):
    Builder.load_file(kv_path + kv)


class AddButton(Button):
    pass


class SubtractButton(Button):
    pass


class Container(GridLayout):
    display = ObjectProperty()

    def add_one(self):
        value = int(self.display.text)
        self.display.text = str(value + 1)

    def subtract_one(self):
        value = int(self.display.text)
        self.display.text = str(value - 1)


class MainApp(App):

    def build(self):
        self.title = 'Awesome app!!!'
        return Container()


if __name__ == "__main__":
    app = MainApp()
    app.run()
