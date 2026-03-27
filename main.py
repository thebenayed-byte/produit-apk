from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class ProduitApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        self.entree1 = TextInput(hint_text="Nombre 1", multiline=False)
        self.entree2 = TextInput(hint_text="Nombre 2", multiline=False)
        self.resultat = Label(text="Résultat : ")

        btn = Button(text="Calculer")
        btn.bind(on_press=self.calculer)

        layout.add_widget(self.entree1)
        layout.add_widget(self.entree2)
        layout.add_widget(btn)
        layout.add_widget(self.resultat)

        return layout

    def calculer(self, instance):
        try:
            a = float(self.entree1.text)
            b = float(self.entree2.text)
            self.resultat.text = f"Résultat : {a * b}"
        except:
            self.resultat.text = "Erreur"

ProduitApp().run()