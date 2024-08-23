class Document:
    def __init__(self, printer):
        self.printer = printer

    def print_document(self, text):
        return self.printer.print_page(text)


class InkjetPrinter:
    @staticmethod
    def print_page(text):
        return f'Inkjet printer printing: {text}'


class LaserPrinter:
    @staticmethod
    def print_page(text):
        return f'Laser printer printing: {text}'


if __name__ == '__main__':
    
    text_to_print = input('Enter the text to print it: ')
    
    document = Document(LaserPrinter())
    print(document.print_document(text_to_print))
    
    document = Document(InkjetPrinter())
    print(document.print_document(text_to_print))
