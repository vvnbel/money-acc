#APK FILE > https://www.youtube.com/watch?v=IqPcO34tUj4&ab_channel=%D0%98%D0%B7%D1%83%D1%87%D0%B0%D0%B5%D0%BC%D0%BC%D0%B8%D1%80%D0%98%D0%A2%2F%D0%9E%D0%BB%D0%B5%D0%B3%D0%A8%D0%BF%D0%B0%D0%B3%D0%B8%D0%BD%2FWISEPLAT
#1111111111555

#pip install kivy
#pip install kivymd
#pip install https://github.com/kivymd/KivyMD/archive/3274d62.zip
#остановился на том что нужно занести в функцию калктэйбл, точнее передать переменную с полей вводаNEW


from kivy.lang import Builder
from kivy.properties import StringProperty, ListProperty
from kivymd.theming import ThemableBehavior
from kivymd.uix.list import OneLineIconListItem, MDList

from kivymd.app import MDApp
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.icon_definitions import md_icons


from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivymd.font_definitions import fonts


from kivymd.uix.label import MDLabel
from kivymd.uix.menu import MDDropdownMenu
from kivy.clock import Clock
from kivy.metrics import dp

from kivymd.uix.picker import MDDatePicker
import datetime

#для сохранения информации
from kivy.storage.jsonstore import JsonStore
from kivy.base import runTouchApp
from kivy.properties import ObjectProperty

store = JsonStore('hello.json')

# put some values
store.put('tito', name='Mathieu', org='kivy')
store.put('tshirtman', name='Gabriel', age=27)

# using the same index key erases all previously added key-value pairs
store.put('tito', name='Mathieu', age=30)

# get a value using a index key and key
print('tito is', store.get('tito')['age'])

# or guess the key/entry for a part of the key
for item in store.find(name='Gabriel'):
    print('tshirtmans index key is', item[0])
    print('his key value pairs are', str(item[1]))



KV = '''
#https://stackoverflow.com/questions/65698145/kivymd-tab-name-containing-icons-and-text
# this import will prevent disappear tabs through some clicks on them)))
#:import md_icons kivymd.icon_definitions.md_icons
#:import fonts kivymd.font_definitions.fonts



Screen:

    MDNavigationLayout:

        ScreenManager:

            Screen:

                BoxLayout:
                    orientation: 'vertical'

                    MDToolbar:
                        title: app.title
                        elevation: 10
                        md_bg_color: 0, 0, 0, 1

                    MDTabs:
                        id: tabs
                        on_tab_switch: app.on_tab_switch(*args)
                        height: "48dp"
                        tab_indicator_anim: False
                        background_color: 0.1, 0.1, 0.1, 1

                        Tab:
                            id: tab1
                            name: 'tab1'
                            text: f"[size=20][font={fonts[-1]['fn_regular']}]{md_icons['calculator-variant']}[/size][/font] Занести новую покупку"
                        
                            BoxLayout:
                                orientation: 'vertical'
                                padding: "10dp"   
                                
                                BoxLayout:
                                    orientation: 'horizontal'                               
                                    
                                    MDIconButton:
                                        icon: "calendar-month"
                                        
                                    MDTextField:
                                        id: start_date
                                        hint_text: "Дата покупки"
                                        on_focus: if self.focus: app.date_dialog.open()
                                
                                BoxLayout:
                                    orientation: 'horizontal'                         
                                    
                                    MDIconButton:
                                        icon: "cash"
                                        
                                    MDTextField:
                                        id: spend
                                        hint_text: "Сколько потрачено"
                                    

                                    
                                BoxLayout:
                                    orientation: 'horizontal'                                 
                                    
                                    MDIconButton:
                                        icon: "bank"
                                    
                                    MDTextField:
                                        id: payment_type
                                        hint_text: "Выбрать тип расхода"
                                        on_focus: if self.focus: app.menu.open()
                                    
                                MDSeparator:
                                    height: "1dp"
                                    
                                
                                BoxLayout:
                                    orientation: 'horizontal'
                                    
                                    AnchorLayout:
                                        anchor_x: 'center'
                                
                                        MDRectangleFlatIconButton:
                                            icon: "android"
                                            text: "ЗАНЕСТИ"
                                            theme_text_color: "Custom"
                                            text_color: 1, 0, 1, 1
                                            line_color: 0, 0, 0, 1
                                            icon_color: 1, 0, 0, 1
                                            md_bg_color: 0.1, 0.1, 0.1, 1
                                            adaptive_width: True
                                            on_release: app.calc_table(*args)
                                            background_color: (0.1, 0.1, 0.1, 1.0)
                                            size_hint_y: .5
                                    

                                 
                        Tab:
                            id: tab2
                            name: 'tab2'
                            text: f"[size=20][font={fonts[-1]['fn_regular']}]{md_icons['table-large']}[/size][/font] Таблица"
                        
                        Tab:
                            id: tab3
                            name: 'tab3'
                            text: f"[size=20][font={fonts[-1]['fn_regular']}]{md_icons['chart-areaspline']}[/size][/font] График"
                        
                        Tab:
                            id: tab4
                            name: 'tab4'
                            text: f"[size=20][font={fonts[-1]['fn_regular']}]{md_icons['chart-pie']}[/size][/font] Информация"
                        
         


        MDNavigationDrawer:
            id: nav_drawer

            ContentNavigationDrawer:
                id: content_drawer
'''

class ContentNavigationDrawer(BoxLayout):
    pass


class ItemDrawer(OneLineIconListItem):
    icon = StringProperty()
    text_color = ListProperty((0, 0, 0, 1))


class DrawerList(ThemableBehavior, MDList):
    def set_color_item(self, instance_item):
        """Called when tap on a menu item."""

        # Set the color of the icon and text for the menu item.
        for item in self.children:
            if item.text_color == self.theme_cls.primary_color:
                item.text_color = self.theme_cls.text_color
                break
        instance_item.text_color = self.theme_cls.primary_color


class Tab(MDFloatLayout, MDTabsBase):
    pass


class AnalyzatorApp(MDApp):
    title = "АНАЛИЗАТОР РАСХОДОВ"
    by_who = "cockradio"


    def __init__(self, **kwargs):
        #добавлено 2 снизу
        self._data = {}
        self._is_changed = True

        super().__init__(**kwargs)
        self.screen = Builder.load_string(KV)
        # https://kivymd.readthedocs.io/en/latest/components/menu/?highlight=MDDropDownItem#center-position
        # menu_items = [{"icon": "git", "text": f"Item {i}"} for i in range(5)]
        menu_items = [{"icon": "format-text-rotation-angle-up", "text": "продукты"},
                      {"icon": "format-text-rotation-angle-down", "text": "бытовая химия"},
                      {"icon": "format-text-rotation-angle-up", "text": "здоровье"},
                      {"icon": "format-text-rotation-angle-up", "text": "автомобиль"},
                      {"icon": "format-text-rotation-angle-up", "text": "проезд"},
                      {"icon": "format-text-rotation-angle-up", "text": "подарки"},
                      {"icon": "format-text-rotation-angle-up", "text": "развлечения"},
                      {"icon": "format-text-rotation-angle-up", "text": "домашние животные"},
                      {"icon": "format-text-rotation-angle-up", "text": "путешествие"},
                      {"icon": "format-text-rotation-angle-up", "text": "прочее"},]

        def store_put(self, key, value):
            self._data[key] = value
            self._is_changed = True
            return True
        self.menu = MDDropdownMenu(
            caller=self.screen.ids.payment_type,
            items=menu_items,
            position="auto",
            width_mult=4,
        )
        self.menu.bind(on_release=self.set_item)

        # https://kivymd.readthedocs.io/en/latest/components/pickers/?highlight=date%20picker#
        self.date_dialog = MDDatePicker(
            callback=self.get_date,
            background_color=(0.2, 0.4, 0.1, 1.0),
        )


    def set_item(self, instance_menu, instance_menu_item):
        def set_item(interval):
            self.screen.ids.payment_type.text = instance_menu_item.text
            instance_menu.dismiss()

        Clock.schedule_once(set_item, 0.2)


    def get_date(self, date):
        '''
        :type date: <class 'datetime.date'>
        '''
        print(date)
        self.screen.ids.start_date.text = date.strftime("%d-%m-%Y")  # str(date)


    def build(self):
        return self.screen


    def on_start(self):
        self.screen.ids.start_date.text = datetime.date.today().strftime("%d-%m-%Y")
        self.screen.ids.spend.text = "0"
        self.screen.ids.payment_type.text = "не выбрано"

        # icons names you can get here: https://materialdesignicons.com/

        icons_item_menu_tabs = {
            "calculator-variant": "TEST",  #ab-testing
            "table-large": "Table",
            "chart-areaspline": "Graph",
            "chart-pie": "Chart",  # chart-arc
            "book-open-variant": "Sum",
        }


        #for icon_name, name_tab in icons_item_menu_tabs.items():
        #    self.root.ids.tabs.add_widget(
        #        Tab(
        #            text=f"[size=20][font={fonts[-1]['fn_regular']}]{md_icons[icon_name]}[/size][/font] {name_tab}"
        #        )
        #    )

    def on_tab_switch(self, instance_tabs, instance_tab, instance_tab_label, tab_text):
        '''Called when switching tabs.

        :type instance_tabs: <kivymd.uix.tab.MDTabs object>;
        :param instance_tab: <__main__.Tab object>;
        :param instance_tab_label: <kivymd.uix.tab.MDTabsLabel object>;
        :param tab_text: text or name icon of tab;
        '''

        print("tab clicked! " + tab_text)

    def on_star_click(self):
        print("star clicked!")


    def calc_table(self, *args):
        print("button1 pressed")
        start_date = self.screen.ids.start_date.text

        payment_type = self.screen.ids.payment_type.text
        spend = self.screen.ids.spend.text

        if store.exists('cockradio'):
            print('tite exists:', store.get('tito2'))
            store.put('new')


        store.put('new', payment_type=payment_type, date=start_date, spend=spend)
        self.screen.ids.start_date.text = datetime.date.today().strftime("%d-%m-%Y")
        self.screen.ids.spend.text = "0"
        self.screen.ids.payment_type.text = "не выбрано"


        pass


AnalyzatorApp().run()