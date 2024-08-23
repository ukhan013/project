from kivymd.app import MDApp  # type: ignore
from kivymd.uix.label import MDLabel  # type: ignore

class MainApp(MDApp):
    def build(self):
        return MDLabel(text="Welcome to my First App", halign="center")

if __name__ == '__main__':
    MainApp().run()
