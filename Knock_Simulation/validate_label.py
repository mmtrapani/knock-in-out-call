__author__ = 'Matt Trapani and Travis Estes'
from tkinter import *
from tkinter.ttk import *

# class FilteringLabel
class FilteringLabel(Label):
    """
    FilteringLabel takes a text variable (like any Label can do), but shows the value
    of that variable on its labels in a desired format. This is achieved by overriding the trivial implementation
    of method filter_callback() in subclasses
    """

    def __init__(self, root, **options):
        # call super
        super().__init__(root, **options)

        # remember text variable and start tracing
        self.__text_variable = options['textvariable']
        self.__text_variable.trace('w', self.__callback)
        # in case option 'text' is set, we already need to filter it
        if 'text' in options:
            self.__text_variable.set(options['text'])

    # this is fired whenever text variable gets altered
    def __callback(self, *args):
        original_text = self.__text_variable.get()
        try:
            filtered_text = self.filter_callback(original_text)
        except Exception as e:
            # here we have an exception because no valid input was passed in
            filtered_text = "INPUT ERROR '{}'".format(original_text)
            callback_string = str(self.filter_callback)
            name = callback_string.split()
            print("An error occurred in function '{}()' on input '{}': {}".format(name[2], original_text, e), flush=True)

        self.__text_variable.set(filtered_text)

    def filter_callback(self, text):
        """
        To be overwritten in subclasses.
        Would fire an exception on invalid input, or return some filtered text otherwise
        """
        return text

# class DollarLabel
class DollarLabel(FilteringLabel):

    def __init__(self, root, **options):
        super().__init__(root, **options)

    # overwriting filter_callback to if text can be converted to float
    # returns formatted text in typical currency format
    def filter_callback(self, text):
        try:
            if text:
                float(text)
        except ValueError:
            raise ValueError

        return "${0:.2f}".format(float(text))


def main():
    root = Tk()
    root.title("lksjl;ksd")

    textLabel = StringVar()
    display = DollarLabel(root, textvariable=textLabel, text='123')

    entryString = StringVar()
    entryString.set('')
    textField = Entry(root, textvariable = entryString)

    showButton = Button(root, text='Show',
                        command=lambda t1=textLabel, es=entryString: t1.set(es.get()))

    display.pack()
    textField.pack()
    showButton.pack()

    root.mainloop()

if __name__ == '__main__':
    main()
