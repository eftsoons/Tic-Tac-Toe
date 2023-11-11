from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.uix.label import Label

Window.size = (500, 500)

main_menu = BoxLayout(orientation='vertical')

crosses_0_squares = GridLayout(cols=3)

score = [0, 0]

label = Label(text="X: " + str(score[0]) + " O: " + str(score[1]), size_hint = [1, 0.25], font_size = 30)

tablsquare = []

class crosses_0(App):

	def build(self):

		self.title = "Крестики-нолики"

		self.motion = "X"
		self.block = False

		for x in range(9):
			#tabltest.append()
			tablsquare.append(Button(text="",font_size = 30, on_press = self.btn_click ))
			crosses_0_squares.add_widget(tablsquare[x])

		main_menu.add_widget(crosses_0_squares)

		main_menu.add_widget(Button(text="Restart", font_size = 30, size_hint = [1, 0.25], on_press = self.reset, background_color = [0, 0, 1, 1]) )

		main_menu.add_widget(label)

		return main_menu

	def reset(self, instance):
		for x in tablsquare:
			x.text = ""
			x.background_color = [1, 1, 1, 1]
		
		label.text = "X: " + str(score[0]) + " O: " + str(score[1])
		self.block = False
		self.motion = "X"

	def finish(self, ivin, namevin, x, y, z):
		score[ivin] += 1
		label.text = "Победил: " + namevin
		tablsquare[x].background_color = [0, 1, 0, 1]
		tablsquare[y].background_color = [0, 1, 0, 1]
		tablsquare[z].background_color = [0, 1, 0, 1]
		self.block = True
		for x in tablsquare:
			if not x.background_color == [0, 1, 0, 1]:
				x.background_color = [1, 0, 0, 1]


	#disabled and color
	def btn_click(self, instance):
		if not self.block:
			if instance.text == "":

				instance.text = self.motion

				if self.motion == "X":
					self.motion = "O"
				else:
					self.motion = "X"

			for index, x1 in enumerate(["X", "O"]): # Математика - cool
				for x in range(0, 3):
					if tablsquare[0 + (x * 3)].text == x1 and tablsquare[1 + (x * 3)].text == x1 and tablsquare[2 + (x * 3)].text == x1: #доделать
						self.finish(index, x1, 0 + (x * 3), 1 + (x * 3), 2 + (x * 3))
						break

					if tablsquare[0 + x].text == x1 and tablsquare[3 + x].text == x1 and tablsquare[6 + x].text == x1: #доделать
						self.finish(index, x1, 0 + x, 3 + x, 6 + x)
						break

					if tablsquare[0 + x].text == x1 and tablsquare[4].text == x1 and tablsquare[8 - x].text == x1: #доделать
						self.finish(index, x1, 0 + x, 4, 8 - x)
						break
		
		else:
			self.reset("")

if __name__ == "__main__":
	crosses_0().run()