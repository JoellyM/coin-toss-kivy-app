from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from random import randrange

class CoinTossGame(BoxLayout):

	def flip_coin(self):
		result = None
		head = 1
		tail = 0
		result = randrange(2)
		if result == self.head:
			return "head"
		if result == self.tail:
			return "tail"

	def win_lose(self, choice):
		if choice == flip_coin():
			self.ids.result_label.text = "You guessed correctly {}".format(choice)
		else:
			self.ids.result_label.text = "It was actually {}, you lose!".format(choice)



class TestApp(App):

	def build(self):
		rootwidget = CoinTossGame()
		return rootwidget

if __name__ == '__main__':
	TestApp().run()
