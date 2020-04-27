from kivy_table_widget import Table
from kivy.app import App
...
table = Table()
table.cols = 2
table.add_button_row('123','456')
table.add_row([Button, {'text':'button2',
                        'color_widget': [0, 0, .5, 1],
                        'color_click': [0, 1, 0, 1]
                       }], 
              [TextInput, {'text':'textinput2',
                           'color_click': [1, 0, .5, 1]
                          }])
table.choose_row(3)
table.del_row(5)
table.grid.color = [1, 0, 0, 1]
table.grid.cells[1][1].text = 'edited textinput text'
table.grid.cells[3][0].height = 100
table.label_panel.labels[1].text = 'New name'

class MyApp(App):
    def build(self):
        return table

MyApp().run()
