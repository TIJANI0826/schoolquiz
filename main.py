from kivy.app import App
from kivy.properties import StringProperty, BooleanProperty
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
import os
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivymd.dialog import MDDialog
from kivymd.label import MDLabel
from kivy.uix.popup import Popup
from kivymd.textfields import MDTextField
from kivymd.theming import ThemeManager
import sqlite3
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import ObjectProperty, StringProperty, ListProperty, AliasProperty, DictProperty, NumericProperty, \
    BooleanProperty
from kivy.uix.image import Image
from kivy.uix.scrollview import ScrollView
from kivymd.list import MDList, OneLineListItem, OneLineAvatarListItem, OneLineIconListItem, ThreeLineListItem, \
    TwoLineListItem
from kivymd.bottomsheet import MDListBottomSheet, MDGridBottomSheet
from kivymd.button import MDIconButton
from kivymd.date_picker import MDDatePicker
from kivymd.list import ILeftBody, ILeftBodyTouch, IRightBodyTouch, BaseListItem
from kivymd.material_resources import DEVICE_TYPE
from kivymd.navigationdrawer import MDNavigationDrawer, NavigationDrawerHeaderBase
from kivymd.selectioncontrols import MDCheckbox
from kivymd.snackbar import Snackbar
from kivymd.time_picker import MDTimePicker
from kivy.uix.image import Image
from kivy.loader import Loader
from time import time
from os.path import dirname, join
from kivy.clock import Clock
from kivy.animation import Animation


class MainApp(App):
    theme_cls = ThemeManager()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.minimum_height = None
        self.ids = None
        self.conn = sqlite3.connect('SCHOOL.db')
        self.c = self.conn.cursor()
        self.all_students = self.c.execute('SELECT * FROM STUDENTS')
        self.all_subjects = self.c.execute('SELECT * FROM SUBJECTS')
        self.get_courses = self.c.execute('SELECT * FROM COURSES')

    def database_creations(self):
        self.conn = sqlite3.connect('SCHOOL.db')
        self.c = self.conn.cursor()
        # creating student

        self.c.execute('''CREATE TABLE STUDENTS(
                        STUDENT_ID INT NOT NULL, 
                        STUDENT_NAME VARCHAR (250),
                        STUDENT_COURSE VARCHAR (250), 
                        STUDENT_CLASS_NAME VARCHAR (250),
                        PRIMARY KEY (STUDENT_ID));''')
        self.conn.commit()
        content = MDLabel(font_style='Body1',
                          theme_text_color='Secondary',
                          text="T"
                               "PERFECT TABLE CREATED!",
                          size_hint_y=None,
                          valign='top')
        content.bind(texture_size=content.setter('size'))
        self.dialog = MDDialog(title="SUCCESSFUL",
                               content=content,
                               size_hint=(.8, None),
                               height=dp(200),
                               auto_dismiss=False)
        self.dialog.add_action_button("Dismiss",
                                      action=lambda *x: self.dialog.dismiss())
        self.dialog.open()
        print("committed")

    def get_student(self, value):

        sv = ScrollView()
        ml = MDList()
        sv.add_widget(ml)
        get_student = self.c.execute('SELECT * FROM STUDENTS WHERE STUDENT_CLASS_NAME = ?', (value,))
        for row in get_student:
            ml.add_widget(
                OneLineListItem(
                    text=str(row[1])
                )
            )
        sv.do_scroll_y = True
        sv.do_scroll_x = False
        r = GridLayout(cols=1, rows=1)
        r.add_widget(sv)
        p = Popup(title='STUDENTS', size_hint=(.7, 0.7), background_color=(0, 0, .9, .5), auto_dismiss=True)
        p.add_widget(r)
        p.open()

    def list_course(self):
        box = BoxLayout()
        sv = ScrollView()
        ml = MDList()
        self.get_courses = self.c.execute('SELECT * FROM COURSES')

        for row in sorted(self.get_courses):
            ml.add_widget(
                OneLineListItem(
                    text=str(row[1])
                )
            )
        sv.do_scroll_y = True
        sv.do_scroll_x = False
        sv.add_widget(ml)
        self.root.ids.courses.add_widget(sv)
        self.root.ids.screen_manager.current = str(self.root.ids.courses.name)

    def subjects(self):
        self.conn = sqlite3.connect('SCHOOL.db')
        self.c = self.conn.cursor()
        self.all_subjects = self.c.execute('SELECT * FROM STUDENTS')
        sv = ScrollView()
        ml = MDList()
        for row in sorted(self.all_subjects):
            ml.add_widget(
                ThreeLineListItem(
                    text=str(row[1]),
                    secondary_text="id: " + str(row[0]) + '\n' 'under : ' + row[2]
                )
            )
        sv.do_scroll_y = True
        sv.do_scroll_x = False
        sv.add_widget(ml)
        self.root.ids.subjects.add_widget(sv)
        self.root.ids.screen_manager.current = str(self.root.ids.subjects.name)

    def teachers(self):
        sv = ScrollView()
        ml = MDList()
        rows = self.c.execute('SELECT * FROM TEACHERS')
        for row in sorted(rows):
            ml.add_widget(
                ThreeLineListItem(
                    text=str(row[1]),
                    secondary_text="id: " + str(row[0]) + '\n' 'under : ' + row[2]
                )
            )
        sv.do_scroll_y = True
        sv.do_scroll_x = False
        sv.add_widget(ml)
        self.root.ids.teachers.add_widget(sv)
        self.root.ids.screen_manager.current = str(self.root.ids.teachers.name)

    def all_student(self):
        self.conn = sqlite3.connect('SCHOOL.db')
        self.c = self.conn.cursor()
        self.all_students = self.c.execute('SELECT * FROM STUDENTS')

        gris = GridLayout(rows=2,
                          # row_default_height=(self.width - self.cols * self.spacing[0]) / self.cols,
                          # row_force_default=True,
                          # size_hint_y=None,
                          # height=self.minimum_height,
                          padding=(dp(1), dp(1)),
                          spacing=dp(1))
        sv = ScrollView()
        ml = MDList()
        for row in self.all_students:
            ml.add_widget(
                ThreeLineListItem(
                    text=str(row[1]),
                    secondary_text=row[2] + '\n' + row[3]
                )
            )
        sv.do_scroll_y = True
        sv.do_scroll_x = False
        sv.add_widget(ml)
        gris.add_widget(MDTextField(hint_text="Helper text on focus",
                                    helper_text="This will disappear when you click off",
                                    helper_text_mode="on_focus"
                                    )
                        )
        gris.add_widget(sv)
        self.root.ids.students.add_widget(gris)
        self.root.ids.screen_manager.current = str(self.root.ids.students.name)

MainApp().run()
