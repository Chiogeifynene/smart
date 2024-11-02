from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.properties import NumericProperty

Window.size = (600, 400)


class HelloGame(Widget):

    score = NumericProperty(0)

    def __init__(self, **kwargs):
        super(HelloGame, self).__init__(**kwargs)

    def increase(self):
        self.score += 1

class MainApp(App):
    def build(self):
        game = HelloGame()
        return game


if __name__ == "__main__":
    MainApp().run()