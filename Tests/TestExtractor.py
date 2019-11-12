import unittest
from core.extractors import MeteoExtractor



class TestExtractor(unittest.TestCase):
    obj = None

    def init(self):
        print('amin')
        a = MeteoExtractor('../Data/METEO/CABOWE','NL2',[])
        self.assertEqual(a.FName,'NL2')
        self.assertEqual('./Data/METEO/CABOWE',a.Path)

    def write(self):
        pass

    def load(self):
        pass

    def create_lookup(self):
        pass

if __name__ == '__main__':
    unittest.main()