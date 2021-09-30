#APK FILE > https://www.youtube.com/watch?v=IqPcO34tUj4&ab_channel=%D0%98%D0%B7%D1%83%D1%87%D0%B0%D0%B5%D0%BC%D0%BC%D0%B8%D1%80%D0%98%D0%A2%2F%D0%9E%D0%BB%D0%B5%D0%B3%D0%A8%D0%BF%D0%B0%D0%B3%D0%B8%D0%BD%2FWISEPLAT
#111
from kivy.lang import Builder

from kivymd.app import MDApp
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.icon_definitions import md_icons
from kivymd.font_definitions import fonts

KV = '''
MDBoxLayout:
    orientation: "vertical"

    MDToolbar:
        title: "ANALIZATOR WALLET ANALYZER"
        md_bg_color: 0, 0, 0, 1

    MDTabs:
        id: tabs
        background_color: 0.1, 0.1, 0.1, 1
'''


class Tab(MDFloatLayout, MDTabsBase):
    pass


class Example(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def on_start(self):
        icons_item_menu_tabs = {
            "calculator-variant": "Input",  # ab-testing
            "table-large": "Table",
            "chart-areaspline": "Graph",
            "chart-pie": "Chart",  # chart-arc
            "book-open-variant": "Sum",
        }

        #https://youtu.be/KLcHMJETg4A?t=578 - OTHER ICONS - ВЫБРАТЬ ДРУГИЕ ИКОНКИ
        #To auto generate tabs
        for icon_name, name_tab in icons_item_menu_tabs.items():
            self.root.ids.tabs.add_widget(
                Tab(
                    text=f"[size=20][font={fonts[-1]['fn_regular']}]{md_icons[icon_name]}[/size][/font] {name_tab}"
                )
            )


Example().run()