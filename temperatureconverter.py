from breezypythongui import EasyFrame

class TemperatureConverter(EasyFrame):
    def __init__(self):
        super().__init__(title = "Temperature Converter")

        self.addLabel(text = "Fahrenheit", row = 0, column = 0)
        self.addLabel(text = "Celsius", row = 0, column = 1)

        self.fahrenheitField = self.addFloatField(value = 32.0, row = 1, column = 0)
        self.celsiusField = self.addFloatField(value = 0.0, row = 1, column = 1)

        self.addButton(text = ">>>", row = 2, column = 0, command = self.f_to_c)
        self.addButton(text = "<<<", row = 2, column = 1, command = self.c_to_f)

    def f_to_c(self):
        f = self.fahrenheitField.getNumber()
        c = (f - 32) * 5 / 9
        self.celsiusField.setNumber(c)

    def c_to_f(self):
        c = self.celsiusField.getNumber()
        f = c * 9 / 5 + 32
        self.fahrenheitField.setNumber(f)

def main():
    TemperatureConverter().mainloop()

if __name__ == "__main__":
    main()
