__author__ = 'Matt Trapani and Travis Estes'
from tkinter import *
from validate_entry import *
from validate_label import *
from compute import *

class OptionsSimulation(Frame):
    def __init__(self, root, **options):
        # call the super constructor
        super().__init__()

        # set general config
        self.root = root
        if 'title' in options:
            self.root.title(options['title'])
        if 'geometry' in options:
            self.root.geometry(options['geometry'])
        self.root.resizable(0,0)
        self.option_add('*Font', 'Verdana 12')
        self.grid(column=0, row=0, sticky='nesw')

        # init data attributes
        self.risk_free_r = StringVar()
        self.delta = StringVar()
        self.volatility = StringVar()
        self.initial_price = StringVar()
        self.barrier = StringVar()
        self.time_to_expire = StringVar()
        self.steps = StringVar()
        self.premium = StringVar()
        self.strike = StringVar()
        self.knock_tuple = ("in", "out")
        self.knock = StringVar()
        self.knock.set(self.knock_tuple[0])

        # instantiate widgets
        risk_free_label = Label(self, text="Risk Free Rate")
        delta_label = Label(self, text="Continuous Dividend Rate")
        volatility_label = Label(self, text="Volatility")
        initial_price_label = Label(self, text="Initial Stock Price")
        barrier_label = Label(self, text="Barrier Price")
        strike_label = Label(self, text="Strike Price")
        expiration_label = Label(self, text="Time until expiration")
        steps_label = Label(self, text="Steps in simulation")
        knock_label = Label(self, text="Knock: 'In' or 'Out'")
        risk_free_entry = FloatEntry(self, textvariable=self.risk_free_r, justify=RIGHT)
        delta_entry = FloatEntry(self, textvariable=self.delta, justify=RIGHT)
        volatility_entry = FloatEntry(self, textvariable=self.volatility, justify=RIGHT)
        initial_price_entry = CurrencyEntry(self, textvariable=self.initial_price, justify=RIGHT)
        barrier_entry = CurrencyEntry(self, textvariable=self.barrier, justify=RIGHT)
        strike_entry = FloatEntry(self, textvariable=self.strike, justify=RIGHT)
        expiration_entry = FloatEntry(self, textvariable=self.time_to_expire, justify=RIGHT)
        steps_entry = IntEntry(self, textvariable=self.steps, justify=RIGHT)
        knock_menu = OptionMenu(self, self.knock, *self.knock_tuple)
        compute_button = Button(self, text='Compute', command=self.evaluate)
        premium_label = Label(self, text='Premium')
        premium_compute_label = DollarLabel(self, textvariable=self.premium, anchor=E, text="0.00")
        quit_button = Button(self, text="Quit", command=self.root.destroy)

        # position widgets
        risk_free_label.grid(row=0, column=0, sticky='w')
        risk_free_entry.grid(row=0, column=1, sticky='e')
        delta_label.grid(row=1, column=0, sticky='w')
        delta_entry.grid(row=1, column=1, sticky='e')
        volatility_label.grid(row=2, column=0, sticky='w')
        volatility_entry.grid(row=2, column=1, sticky='e')
        initial_price_label.grid(row=3, column=0, sticky='w')
        initial_price_entry.grid(row=3, column=1, sticky='e')
        barrier_label.grid(row=4, column=0, sticky='w')
        barrier_entry.grid(row=4, column=1, sticky='e')
        strike_label.grid(row=5, column=0, sticky='w')
        strike_entry.grid(row=5, column=1, sticky='e')
        expiration_label.grid(row=6, column=0, sticky='w')
        expiration_entry.grid(row=6, column=1, sticky='e')
        steps_label.grid(row=7, column=0, sticky='w')
        steps_entry.grid(row=7, column=1, sticky='e')
        knock_label.grid(row=8, column=0, sticky='w')
        knock_menu.grid(row=8, column=1, sticky='ew')
        compute_button.grid(row=9, column=0, columnspan=2, sticky='ew')
        premium_label.grid(row=10, column=0, sticky='w')
        premium_compute_label.grid(row=10, column=1, sticky='e')
        quit_button.grid(row=11, column=0, columnspan=2, sticky='ew')

    def evaluate(self):
        try:
            self.premium.set(compute(self.risk_free_r.get(), self.delta.get(), self.volatility.get(),
                                     self.initial_price.get(), self.barrier.get(), self.strike.get() , self.time_to_expire.get(),
                                     self.steps.get(),self.knock.get()))
        except ValueError:
            self.premium.set("0.00")
def main():
    root = Tk()
    OptionsSimulation(root, title="Knock In/Out Call Simulation")
    root.mainloop()

if __name__ == "__main__":
    main()
