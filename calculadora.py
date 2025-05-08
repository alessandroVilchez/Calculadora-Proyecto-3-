from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window
Window.size=(500,600)


kv_code="""
<Calculadora>:
    BoxLayout:
        orientation: "vertical"
        size: root.width, root.height

        TextInput:
            text:"0"
            halign: "right"
            font_size: 50
            size_hint: (1, 0.2)
            id:input            

        GridLayout:
            cols: 4
            rows: 5 
            size: root.width, root.height
            spacing: [5, 5]

                  
            Button:
                id: disminuir 
                size_hint: (0.1, 0.1)
                text: "<<"
                font_size: 30
                on_press: root.disminuir()
               
            Button:
                id: dividir
                text: "/"
                size_hint: (0.1, 0.1)
                font_size: 30
                on_press: root.dividir()

               
            Button:
                id: multiplicar
                text: "x"
                size_hint: (0.1, 0.1)
                font_size: 30
                on_press: root.multiplicar()

            
            Button:
                id: borrar
                size_hint: (0.1, 0.1)
                text: "DELETE"
                on_press: root.borrar()
                font_size: 23

            Button:
                size_hint: (0.1, 0.1)
                background_color: 
                text: "1"
                on_press:root.add(1)
                font_size: 30
                background_color: 0.529, 0.529, 0.529
                background_normal: ""

            Button:
                size_hint: (0.1, 0.1)
                text: "2"
                on_press:root.add(2)
                font_size: 30
                background_color: 0.529, 0.529, 0.529
                background_normal: ""

            Button:
                size_hint: (0.1, 0.1)
                text: "3"
                on_press:root.add(3)
                font_size: 30
                background_color: 0.529, 0.529, 0.529
                background_normal: ""

            Button:
                text: "+"
                size_hint: (0.1, 0.1)
                on_press:root.sum()
                font_size: 30

            Button:
                size_hint: (0.1, 0.1)
                text: "4"
                on_press:root.add(4)
                font_size: 30
                background_color: 0.529, 0.529, 0.529
                background_normal: ""

            Button:
                size_hint: (0.1, 0.1)
                text: "5"
                on_press:root.add(5)
                font_size: 30
                background_color: 0.529, 0.529, 0.529
                background_normal: ""
            
            Button:
                size_hint: (0.1, 0.1)
                text: "6"
                on_press:root.add(6)
                font_size: 30
                background_color: 0.529, 0.529, 0.529
                background_normal: ""
            
            Button:
                size_hint: (0.1, 0.1)
                text: "-"
                font_size: 30
                id: resta
                on_press:root.resta()
            
            Button:
                size_hint: (0.1, 0.1)
                text: "7"
                on_press:root.add(7)
                font_size: 30
                background_color: 0.529, 0.529, 0.529
                background_normal: ""
            
            Button:
                size_hint: (0.1, 0.1)
                text: "8"
                on_press:root.add(8)
                font_size: 30
                background_color: 0.529, 0.529, 0.529
                background_normal: ""

            Button:
                id:9
                size_hint: (0.1, 0.1)
                text: "9"
                on_press:root.add(9)
                font_size: 30
                background_color: 0.529, 0.529, 0.529
                background_normal: ""
            
            Button:
                size_hint: (0.1, 0.1)
                text: "="
                font_size: 30
                id: igual
                on_press: root.igual()

            Button:
                size_hint: (0.1, 0.1)
                text: "0"
                on_press:root.add(0)
                font_size: 30
                background_color: 0.529, 0.529, 0.529
                background_normal: ""
                

"""


class Calculadora(Widget):

    def disminuir(self):
        hay=self.ids.input.text
        self.ids.input.text=hay[:-1]
        if self.ids.input.text=="":
            self.ids.input.text=f"0"
            

    def dividir(self):
        hay=self.ids.input.text
        self.ids.input.text= f"{hay} / "
        conteo=self.ids.input.text.count("/")

        if conteo==2:
            cadena=self.ids.input.text
            preDiv=cadena[:cadena.find("/")]
            postDiv=cadena[cadena.find("/")+1:-2]
            numberpreDiv=int(preDiv)
            numberpostDiv=int(postDiv)
            self.ids.input.text=f"{int(numberpreDiv / numberpostDiv)}"

    
    
    def multiplicar(self):
        hay=self.ids.input.text
        self.ids.input.text= f"{hay} x "
        conteo=self.ids.input.text.count("x")
        
        if conteo==2:
            cadena=self.ids.input.text
            preDiv=cadena[:cadena.find("x")]
            postDiv=cadena[cadena.find("x")+1:-2]
            numberpreDiv=int(preDiv)
            numberpostDiv=int(postDiv)
            self.ids.input.text=f"{int(numberpreDiv * numberpostDiv)}"



    def borrar(self):
        self.ids.input.text="0"



    def sum(self):
        hay=self.ids.input.text
        self.ids.input.text= f"{hay} +"
        conteo=self.ids.input.text.count("+")
        
        if conteo==2:
            cadena=self.ids.input.text
            preMas=cadena[:cadena.find("+")]
            postMas=cadena[cadena.find("+")+1:-1]

            numberpreMas=int(preMas)
            numberpostMas=int(postMas)
            self.ids.input.text=f"{numberpostMas + numberpreMas}"

    
    def resta(self):
        hay=self.ids.input.text
        self.ids.input.text= f"{hay} - "
        conteo=self.ids.input.text.count("-")

        if conteo==2:
            cadena=self.ids.input.text
            preDiv=cadena[:cadena.find("-")]
            postDiv=cadena[cadena.find("-")+1:-2]
            numberpreDiv=int(preDiv)
            numberpostDiv=int(postDiv)
            self.ids.input.text=f"{int(numberpreDiv - numberpostDiv)}"

    def igual(self):
        hay=self.ids.input.text
    
        if "-" in hay: 
            cadena=self.ids.input.text
            preDiv=cadena[:cadena.find("-")]
            postDiv=cadena[cadena.find("-")+1:]
            numberpreDiv=int(preDiv)
            numberpostDiv=int(postDiv)
            self.ids.input.text=f"{int(numberpreDiv - numberpostDiv)}"

        elif "+" in hay:
            cadena=self.ids.input.text
            preDiv=cadena[:cadena.find("+")]
            postDiv=cadena[cadena.find("+")+1:]
            numberpreDiv=int(preDiv)
            numberpostDiv=int(postDiv)
            self.ids.input.text=f"{int(numberpreDiv + numberpostDiv)}"
        
        elif "x" in hay:
            cadena=self.ids.input.text
            preDiv=cadena[:cadena.find("x")]
            postDiv=cadena[cadena.find("x")+1:]
            numberpreDiv=int(preDiv)
            numberpostDiv=int(postDiv)
            self.ids.input.text=f"{int(numberpreDiv * numberpostDiv)}"
        
        elif "/" in hay: 
            
            cadena=self.ids.input.text
            preDiv=cadena[:cadena.find("/")]
            postDiv=cadena[cadena.find("/")+1:]
            numberpreDiv=int(preDiv)
            numberpostDiv=int(postDiv)
            self.ids.input.text=f"{int(numberpreDiv / numberpostDiv)}"

    def add(self, numero):
        hay=self.ids.input.text
        self.ids.input.text=f"{hay}{ numero}"


class My2(App):

    def build(self):
        Builder.load_string(kv_code)
        return Calculadora()

My2().run()






