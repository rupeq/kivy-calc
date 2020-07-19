from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

fields = [
    ["1", "2", "3"],
    ["4", "5", "6"],
    ["7", "8", "9"],
    ["0", "+", "-"],
    [".", "C", "="]
]

class MyApp(App):
    def build(self):
        self.label = Label(text="")
        main_layout = BoxLayout(orientation='vertical')
        main_layout.add_widget(self.label)
        for row in fields:
            row_layaut = BoxLayout(orientation="horizontal")
            for item in row:
                btn = Button(text = f"{item}", on_press=self.press)
                row_layaut.add_widget(btn)
            main_layout.add_widget(row_layaut)
        return main_layout
    
    def press(self, instance):
        if instance.text == "C":
            self.label.text = ""
        elif instance.text == "=":
            self.label.text = str(eval(self.label.text))
        else:
            if self.label.text and self.label.text[-1] == "0" and instance.text != ".":
                if instance.text in [str(i) for i in range(1,  10)]:
                    self.label.text = self.label.text[:-1] + instance.text
            else:
                self.label.text += instance.text

MyApp().run()
