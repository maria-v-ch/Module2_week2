from builtins import isinstance


class Printer:
    @staticmethod
    def __init__():
        pass

    def print_page(self):
        pass


class InkjetPrinter(Printer):
    def __init__(self):
        super().__init__()

    def print_page(self):
        print('Inkjet printer printing ...')


class LaserPrinter(Printer):
    def __init__(self):
        super().__init__()

    def print_page(self):
        print('Laser printer printing ...')


class Document:
    def __init__(self, printer=None):
        if printer is None:
            self.printer = InkjetPrinter()
        if isinstance(printer, InkjetPrinter):
            self.printer = printer
        elif isinstance(printer, LaserPrinter):
            self.printer = printer

    def print_document(self):
        self.printer.print_page()


printer_ink = InkjetPrinter()
printer_laser = LaserPrinter()
doc1 = Document()
doc1.print_document()
doc2 = Document(printer_ink)
doc2.print_document()
doc3 = Document(printer_laser)
doc3.print_document()
