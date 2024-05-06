class Document:
    def __init__(self, printer):
        self.printer = printer

    def print_document(self):
        return self.printer.print_page()


class InkjetPrinter:
    @staticmethod
    def print_page():
        return 'Inkjet printer printing ...'


class LaserPrinter:
    @staticmethod
    def print_page():
        return 'Laser printer printing ...'


if __name__ == '__main__':
    document = Document(LaserPrinter())
    print(document.print_document())
    document = Document(InkjetPrinter())
    print(document.print_document())