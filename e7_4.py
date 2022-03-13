import kivy.uix.boxlayout
import kivy.uix.textinput
import kivy.uix.label
import kivy.uix.button
from kivy.app import App


class SimpleApp(App):

    def build(self):
        self.t = kivy.uix.textinput.TextInput()
        self.l = kivy.uix.label.Label(text="Your Message.")
        self.button = kivy.uix.button.Button(text="Click Me.")
        self.button.bind(on_press=self.displayMessage)
        self.boxLayout = kivy.uix.boxlayout.BoxLayout(orientation="vertical")
        self.boxLayout.add_widget(self.t)
        self.boxLayout.add_widget(self.l)
        self.boxLayout.add_widget(self.button)
        return self.boxLayout

    def displayMessage(self, btn):
        self.l.text = self.t.text

if __name__ == "__main__":
    simpleApp = SimpleApp()
    simpleApp.run()
