import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout

from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.config import Config

# 0 being off 1 being on as in true / false
# you can use 0 or 1 && True or False
Config.set('graphics', 'resizable', True)

# Make an app by deriving from the kivy provided app class
class PopupExample(App):
	# override the build method and return the root widget of this App

	def build(self):
		# Define a grid layout for this App
		self.layout = GridLayout(cols = 1, padding = 10)


		# Add a button
		self.button = Button(text ="Click for pop-up")
		self.layout.add_widget(self.button)

		# Attach a callback for the button press event
		self.button.bind(on_press = self.onButtonPress)
		
		return self.layout

	# On button press - Create a popup dialog with a label and a close button
	def onButtonPress(self, button):
		
		layout = GridLayout(cols = 1, padding = 10)

		popupLabel = Label(text = "Click for pop-up")
		closeButton = Button(text = "Close the pop-up")

		layout.add_widget(popupLabel)
		layout.add_widget(closeButton)	

		# Instantiate the modal popup and display
		popup = Popup(title ='Demo Popup',
					content = layout,
					size_hint =(None, None), size =(200, 200))
		popup.open()

		# Attach close button press with popup.dismiss action
		closeButton.bind(on_press = popup.dismiss)

# Run the app
if __name__ == '__main__':
	PopupExample().run()
