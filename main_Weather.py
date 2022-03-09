from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy. import ObjectProperty


class AddLocationForm(BoxLayout):
    search_input =
    def search_location(self):
        print("The user searched for '{}'".format(self.search_input.text))


class WeatherApp(App):
    pass


if __name__ == '__main__':
    WeatherApp().run()