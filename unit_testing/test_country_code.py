import unittest
from core.country_code import country_code


class TestCountryCode(unittest.TestCase):
    
    """
    Unit test class that tests the country_code function.
    """

    def test_country_code_dictionary(self):
        
        """
        This code tests if the country_code function returns a dictionary and that it is not empty.
        """
        codes = country_code()
        self.assertIsInstance(codes, dict)  # Checking if the result is a dictionary
        self.assertGreater(len(codes), 0)  # Ensuring the dictionary is not empty

    def test_specific_country_codes(self):
        
        """
        It tests specific country codes to ensure they are correct.
        """
        codes = country_code()
        self.assertEqual(codes.get('India'), 'in') # This tests the country code for India
        self.assertEqual(codes.get('United States Of America'), 'us') #It tests the country code for USA
        self.assertEqual(codes.get('United Kingdom'), 'gb') #It tests the country code for UK
        self.assertEqual(codes.get('Canada'), 'ca')  #It tests the country code for Canada
        self.assertEqual(codes.get('Australia'), 'au')  #It tests the country code for Australia

    def test_country_code_not_found(self):
        
        """
        This tests that a fictional country code returns None.
        """
        codes = country_code()
        self.assertIsNone(codes.get('Atlantis'))  # Atlantis is a fictional country
    



if __name__ == '__main__':
    unittest.main()
