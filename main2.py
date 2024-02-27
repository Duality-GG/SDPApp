from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class FirstScreen(Screen):
    pass  # Your code here

class SecondScreen(Screen):
    pass  # Here you would add your Presets-specific widgets

class ThirdScreen(Screen):
    pass  # Here you would add your Freelook-specific widgets

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')

        # Background before the text can be set here
        self.background = 'path/to/background/image.png'

        # Buttons to switch screens
        btn_constellation = Button(text='Constellation')
        btn_constellation.bind(on_press=self.change_to_constellation)
        btn_presets = Button(text='Presets')
        btn_presets.bind(on_press=self.change_to_presets)
        btn_freelook = Button(text='Freelook')
        btn_freelook.bind(on_press=self.change_to_freelook)

        layout.add_widget(btn_constellation)
        layout.add_widget(btn_presets)
        layout.add_widget(btn_freelook)

        self.add_widget(layout)

    def change_to_constellation(self, *args):
        self.manager.current = 'constellation'

    def change_to_presets(self, *args):
        self.manager.current = 'presets'

    def change_to_freelook(self, *args):
        self.manager.current = 'freelook'

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(FirstScreen(name='constellation'))
        sm.add_widget(SecondScreen(name='presets'))
        sm.add_widget(ThirdScreen(name='freelook'))
        return sm

if __name__ == '__main__':
    MyApp().run()