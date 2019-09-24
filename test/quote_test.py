import unittest
from models import quotes
Quote = Quote.quotes

class QuoteTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the quote class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_quote = Quote(1234,'','','',8.5,129993)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_quote,Quote))


if __name__ == '__main__':
    unittest.main()