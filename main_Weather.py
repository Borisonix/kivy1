from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class AddLocationForm(BoxLayout):
    def search_location(self):
        print("Явное лучше, чем неявное.")

class WeatherApp(App):
    pass

if __name__ == '__main__':
    WeatherApp().run()