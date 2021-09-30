
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

    MDTabs:
        id: tabs
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


        #To auto generate tabs
        for icon_name, name_tab in icons_item_menu_tabs.items():
            self.root.ids.tabs.add_widget(
                Tab(
                    text=f"[size=20][font={fonts[-1]['fn_regular']}]{md_icons[icon_name]}[/size][/font] {name_tab}"
                )
            )


Example().run()