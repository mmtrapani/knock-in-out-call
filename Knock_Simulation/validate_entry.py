__author__ = 'Matt Trapani and Travis Estes'
from tkinter import*
from tkinter.ttk import*

# class ValidationException
class ValidationException(Exception):
    def __init__(self, value):
        self.value = str(value)
    def __str__(self):
        return self.value

# class validating entry
class ValidatingEntry(Entry):
    """
    ValidatingEntry is a generic class that provided validating services
    """
    def __init__(self, root, **options):
        # init super
        super().__init__(root, **options)

        # __text contains always the valid entry, before the text variable got changed
        # set it to '', in case the validation of the initial text fails
        self.__text = ''
        self.__text_variable = options['textvariable']
        self.__text_variable.trace('w', self.__callback)

        # note that by default Entry does not have an init parameter 'text' like labels do
        # if there is a text options, set the text variable to it, which in turn will display it
        # this will also already validate the text, if validation fails, the text variable will be set back to ''
        if 'text' in options:
            self.__text_variable.set(options['text'])
        self.config(textvariable=self.__text_variable)

    def __callback(self, *discard):
        """
        helper method that is the standard callback for text variable tracing,
        which calls the validation function internally and only applies changes
        if validation does not fail
        """

        # get the newly entered text from the textvariable
        new_text = self.__text_variable.get()

        # now do the validation
        if self.validate_callback(new_text):
            # only set __text to the new text, when validation is fine
            self.__text = new_text

        # set the textvariable's value. this would be the new text,
        # if validation is fine, or the old (unaltered text), if it failed
        # this does not lead to an unwanted recursion - after all,
        # we change the textvariable that is being traced (!)
        # tkinter seems to take care of it
        self.__text_variable.set(self.__text)

    def validate_callback(self, text):
        """
        Override this method in subclasses. Returns False if validation fails, True otherwise.
        """
        # just return True in this trivial implementation
        return True

# class FloatEntry
class FloatEntry(ValidatingEntry):
    """
    Entry that only accepts floating point numbers
    """
    def __init__(self, root, **options):
        super().__init__(root, **options)

    # overwriting validate_callback from super to check for float
    def validate_callback(self, text):
        try:
            if text:
                float(text)
            return True
        except ValueError:
            return False

# class IntEntry
class IntEntry(ValidatingEntry):
    """
    Entry only accepts integer numbers
    """
    def __init__(self, root, **options):
        super().__init__(root, **options)

    # overwriting validate_callback from super to check for int
    def validate_callback(self, text):
        try:
            if text:
                int(text)
            return True
        except ValueError:
            return False

# class CurrencyEntry
class CurrencyEntry(FloatEntry):

    def __init__(self, root, **options):
        super().__init__(root, **options)

    # overwriting validate_callback to check that it is first a float
    # secondly, split the float if there is a decimal, if the length after the decimal
    # exceeds 2, return False so the new_text is not set
    def validate_callback(self, text):
        if not super().validate_callback(text):
            return False

        if '.' in text:
            new_text = text.split('.')
            if len(new_text[1]) <= 2:
                return True
            else:
                return False
        else:
            return True

def main():
    root = Tk()
    root.title("lkjl;skj")
    root.geometry('300x30')

    currency_value = StringVar()
    entry = CurrencyEntry(root, text='123.00', textvariable=currency_value)
    entry.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
