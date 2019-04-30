from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.properties import ObjectProperty

Window.clearcolor = (0,0,0,1)
Window.size = (400, 600)

class DemoApp(App):
    def build(self):
        return DemoLayout()

class DemoLayout(BoxLayout):
    def switch_on(self, switch, value):
        if value:
            print("switch on")
            Window.clearcolor = (1, 1, 1, 1)
            self.switch_text.color = (0,0,0,1)
        else:
            print("switch off")
            Window.clearcolor = (0, 0, 0, 1)
            self.switch_text.color = (1,1,1,1)

    def slider_change(self, slider, value):
        self.slider_text.color = (value, value, value, 1)

if __name__ == "__main__":
    demo = DemoApp()
    demo.run()