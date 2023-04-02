import Targest2 # Imports the Gui.py file
import unittest
import docx
import re
class TestTags(unittest.TestCase):
    def test_tags(self):
        doc = docx.Document('testing_report.docx')
        fullText = ''
        for para in doc.paragraphs:
            fullText += para.text
            pattern = r'\[([^\]]+)\]'
            # pattern = r"\b[A-Z]+:\b\d+"
            matches = re.findall(pattern, fullText)
            self.assertGreater(len(matches), 0, "No tags found in the report")
            # self.assertEqual(Targest2.tags("test"), "test")
            self.assertDictEqual(Targest2.tags(fullText), matches)
def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(TestTags('test_tags'))
    runner = unittest.TextTestRunner()
    runner.run(suite)



if __name__ == "__main__" :
    
    Targest2.generateReport() # Calls the generateReport 
    Targest2.generateReport2() # Calls the generateReport2 function 
    # run_tests()


