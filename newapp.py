import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import _textinput_list, TextInput
from kivy.uix.button import Button


def childapp():
    pass


class childapp(GridLayout):
    def __init__(self, **kwargs):
        super(childapp, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text = 'Student Name'))
        self.s_name = TextInput(multiline=False)
        self.add_widget(self.s_name)

        self.add_widget(Label(text='Student Marks'))
        self.s_marks = TextInput(multiline=False)
        self.add_widget(self.s_marks)

        self.add_widget(Label(text='Student Gender'))
        self.s_gender = TextInput(multiline=False)
        self.add_widget(self.s_gender)

        self.press = Button(text = 'Click me')
        self.press.bind(on_press = self.click_me)
        self.add_widget(self.press)

    def click_me(self, instance):
        print("Name of Student is "+self.s_name.text)
        print("Marks of Student is " + self.s_marks.text)
        print("Gender of Student is " + self.s_gender.text)

class parentApp(App):
    def build(self):
        return childapp()

if __name__ == "__main__":
     parentApp().run()


