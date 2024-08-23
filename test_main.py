import unittest
from main import Document, InkjetPrinter, LaserPrinter


class TestDocumentPrinting(unittest.TestCase):
    def setUp(self):
        self.laser_printer = LaserPrinter()
        self.inkjet_printer = InkjetPrinter()
        self.document_laser = Document(self.laser_printer)
        self.document_inkjet = Document(self.inkjet_printer)

    def test_laser_printer_print(self):
        text = 'Hello, Laser!'
        expected_output = 'Laser printer printing: Hello, Laser!'
        self.assertEqual(self.document_laser.print_document(text), expected_output)

    def test_inkjet_printer_print(self):
        text = 'Hello, Inkjet!'
        expected_output = 'Inkjet printer printing: Hello, Inkjet!'
        self.assertEqual(self.document_inkjet.print_document(text), expected_output)

    def test_empty_text_laser_printer(self):
        text = ''
        expected_output = 'Laser printer printing: '
        self.assertEqual(self.document_laser.print_document(text), expected_output)

    def test_empty_text_inkjet_printer(self):
        text = ''
        expected_output = 'Inkjet printer printing: '
        self.assertEqual(self.document_inkjet.print_document(text), expected_output)

    def test_none_text_laser_printer(self):
        text = None
        expected_output = 'Laser printer printing: None'
        self.assertEqual(self.document_laser.print_document(text), expected_output)

    def test_none_text_inkjet_printer(self):
        text = None
        expected_output = 'Inkjet printer printing: None'
        self.assertEqual(self.document_inkjet.print_document(text), expected_output)


if __name__ == '__main__':
    unittest.main()
