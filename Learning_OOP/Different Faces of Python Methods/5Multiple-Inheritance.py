                                #### MULTIPLE INHERITANCE ####

# When you plan to implement a multiple inheritance from abstract classes, 
# remember that an effective subclass should override all abstract methods inherited from its super classes.

# Note to self
    # This is quite possibly the single worst example possible for abstract class use cases
    # I have no Idea how anybody learns to use this in proper code from this course.

import abc

class Scanner(abc.ABC):
    def scan_document(self):
        return 'Scanning Document'

    @abc.abstractmethod
    def get_scanner_status(self):
        pass

class Printer(abc.ABC):
    def print_document(self):
        return 'Printing Document'

    @abc.abstractmethod
    def get_printer_status(self):
        pass


class MFD1(Scanner, Printer):
    def __init__(self):
        print('MFD1 object initiated')

    def get_scanner_status(self):
        return 'Scanner Status: poor'
    
    def get_printer_status(self):
        return 'Printer Status: poor'


class MFD2(Scanner, Printer):
    def __init__(self):
        print('MFD2 object initiated')

    def get_scanner_status(self):
        return 'Scanner Status: Good'
    
    def get_printer_status(self):
        return 'Printer Status: Good'

    def get_op_history(self):
        return 'Printing Operation History'


class MFD3(Scanner, Printer):
    def __init__(self):
        print('MFD3 object initiated')

    def get_scanner_status(self):
        return 'Scanner Status: Excellent'
    
    def get_printer_status(self):
        return 'Printer Status: Excellent'

    def get_op_history(self):
        return 'Printing Operation History'

    def extra_functionality(self):
        return 'Extra functionailty...'

mfd1 = MFD1()
print(mfd1.print_document())
print(mfd1.get_printer_status())
mfd2 = MFD2()
print(mfd2.print_document())
print(mfd2.get_printer_status())
mfd3 = MFD3()
print(mfd3.print_document())
print(mfd3.get_printer_status())