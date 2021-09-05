from kivymd.app import MDApp
from kivymd.uix.label import MDLabel


class MoneyAccountApp(MDApp):
    def build(self):
        return MDLabel(text="HELO0", halign="center")

#123
MoneyAccountApp().run()