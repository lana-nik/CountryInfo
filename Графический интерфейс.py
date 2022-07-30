
from tkinter import *
from countryinfo import CountryInfo

def Call():
    button1 = Label(ventana, font=("Arial Bold", 30))
    button1.place(x = 10, y = 10)
    button1["bg"] = "red"
    button1["fg"] ="yellow"
def Call():
    button2 = Label(ventana, font=("Arial Bold", 30))
    button2.place(x = 110, y = 10)
    button2["bg"] = "red"
    button2["fg"] ="yellow"
def Call():
    button3 = Label(ventana, font=("Arial Bold", 30))
    button3.place(x = 210, y = 10)
    button3["bg"] = "red"
    button3["fg"] ="yellow"
def Call():
    button4 = Label(ventana, font=("Arial Bold", 30))
    button4.place(x = 310, y = 10)
    button4["bg"] = "red"
    button4["fg"] ="yellow"
def Call():
    button5 = Label(ventana, ont=("Arial Bold", 30))
    button5.place(x = 10, y = 50)
    button5["bg"] = "red"
    button5["fg"] ="yellow"
def Call():
    button6 = Label(ventana, font=("Arial Bold", 30))
    button6.place(x = 110, y = 50)
    button6["bg"] = "red"
    button6["fg"] ="yellow"
def Call():
    button7 = Label(ventana, font=("Arial Bold", 30))
    button7.place(x = 210, y = 50)
    button7["bg"] = "red"
    button7["fg"] ="yellow"
ventana = Tk()
ventana.title("La ventana")
ventana.geometry("500x150")
ventana["bg"] = "black"
button1 = Button(text = "Espana",font=("Times New Roman", 10), command = lambda:[funcA()])
button1.place(x = 10, y = 10, width = 90, height = 35)
button2 = Button(text = "Italy",font=("Times New Roman", 10), command = lambda:[funcB()])
button2.place(x = 110, y = 10, width = 90, height = 35)
button3 = Button(text = "Hangria",font=("Times New Roman", 10), command = lambda:[funcC()])
button3.place(x = 210, y = 10, width = 90, height = 35)
button4 = Button(text = "Brazil",font=("Times New Roman", 10), command = lambda:[funcD()])
button4.place(x = 310, y = 10, width = 90, height = 35)
button5 = Button(text = "Portugal",font=("Times New Roman", 10), command = lambda:[funcE()])
button5.place(x = 10, y = 50, width = 90, height = 35)
button6 = Button(text = "Cuba",font=("Times New Roman", 10), command = lambda:[funcK()])
button6.place(x = 110, y = 50, width = 90, height = 35)
button7 = Button(text = "France",font=("Times New Roman", 10), command = lambda:[funcL()])
button7.place(x = 210, y = 50, width = 90, height = 35)
def funcA():
    country = CountryInfo('Spain')
    print('Espana')
    print('Численность населения:', country.population())
    print('Язык:', country.languages())
    print('Столица:', country.capital())
    print('Код страны:', country.calling_codes())
    print('Регион:', country.region())
    print('Часовой пояс:', country.timezones())
    print('На разных языках эта страна:', country.translations())
    print('Страничка в википедии:', country.wiki())
    print()
def funcB():
    country = CountryInfo('Italy')
    print('Italy')
    print('Численность населения:', country.population())
    print('Язык:', country.languages())
    print('Столица:', country.capital())
    print('Код страны:', country.calling_codes())
    print('Регион:', country.region())
    print('Часовой пояс:', country.timezones())
    print('На разных языках эта страна:', country.translations())
    print('Страничка в википедии:', country.wiki())
    print()
def funcC():
    country = CountryInfo('Hungary')
    print('Hangria')
    print('Численность населения:', country.population())
    print('Язык:', country.languages())
    print('Столица:', country.capital())
    print('Код страны:', country.calling_codes())
    print('Регион:', country.region())
    print('Часовой пояс:', country.timezones())
    print('На разных языках эта страна:', country.translations())
    print('Страничка в википедии:', country.wiki())
    print()
def funcD():
    country = CountryInfo('Brazil')
    print('Brazil')
    print('Численность населения:', country.population())
    print('Язык:', country.languages())
    print('Столица:', country.capital())
    print('Код страны:', country.calling_codes())
    print('Регион:', country.region())
    print('Часовой пояс:', country.timezones())
    print('На разных языках эта страна:', country.translations())
    print('Страничка в википедии:', country.wiki())
    print()
def funcE():
    country = CountryInfo('Portugal')
    print('Portugal')
    print('Численность населения:', country.population())
    print('Язык:', country.languages())
    print('Столица:', country.capital())
    print('Код страны:', country.calling_codes())
    print('Регион:', country.region())
    print('Часовой пояс:', country.timezones())
    print('На разных языках эта страна:', country.translations())
    print('Страничка в википедии:', country.wiki())
    print()
def funcK():
    country = CountryInfo('Cuba')
    print('Cuba')
    print('Численность населения:', country.population())
    print('Язык:', country.languages())
    print('Столица:', country.capital())
    print('Код страны:', country.calling_codes())
    print('Регион:', country.region())
    print('Часовой пояс:', country.timezones())
    print('На разных языках эта страна:', country.translations())
    print('Страничка в википедии:', country.wiki())
    print()
def funcL():
    country = CountryInfo('France')
    print('France')
    print('Численность населения:', country.population())
    print('Язык:', country.languages())
    print('Столица:', country.capital())
    print('Код страны:', country.calling_codes())
    print('Регион:', country.region())
    print('Часовой пояс:', country.timezones())
    print('На разных языках эта страна:', country.translations())
    print('Страничка в википедии:', country.wiki())
    print()
ventana.mainloop()
