from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.clock import Clock
from player import Player
from country_ranking import CountryRanking

class PopCatGame(BoxLayout):
    def __init__(self, **kwargs):
        super(PopCatGame, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.player = Player('USA')  # Assume the player is from USA
        self.country_ranking = CountryRanking()
        self.score_label = Label(text='Score: 0')
        self.add_widget(self.score_label)
        self.popcat_button = Button(text='PopCat')
        self.popcat_button.bind(on_press=self.on_button_press)
        self.add_widget(self.popcat_button)
        Clock.schedule_interval(self.update, 1.0)

    def on_button_press(self, instance):
        self.player.score += 1
        self.country_ranking.add_score(self.player.country, 1)

    def update(self, dt):
        self.score_label.text = 'Score: ' + str(self.player.score)

class PopCatApp(App):
    def build(self):
        return PopCatGame()

if __name__ == '__main__':
    PopCatApp().run()
