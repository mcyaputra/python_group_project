import unittest
from core.visualization import VisualizeWords

class TestVisualization(unittest.TestCase):

    def setUp(self):
        self.visual = VisualizeWords()
        self.text = 'Cannes 2024: Megalopolis movie review – Francis Ford Coppola’s wildly ambitious project comes to fruition'
        self.token_result = self.visual.tokenize_words(self.text)

    def test_tokenize_words(self):
        
        expected_result = ['cannes',
                            '2024',
                            ':',
                            'megalopolis',
                            'movie',
                            'review',
                            '–',
                            'francis',
                            'ford',
                            'coppola',
                            '’',
                            's',
                            'wildly',
                            'ambitious',
                            'project',
                            'comes',
                            'to',
                            'fruition']
        
        result = self.visual.tokenize_words(self.text)

        self.assertEqual(result, expected_result)

    def test_remove_stop_words(self):

        expected_result = ['cannes',
                            '2024',
                            'megalopolis',
                            'movie',
                            'review',
                            '–',
                            'francis',
                            'ford',
                            'coppola',
                            '’',
                            'wildly',
                            'ambitious',
                            'project',
                            'comes',
                            'fruition']
        
        self.stop_words_result = self.visual.remove_stop_words(self.token_result)

        self.assertEqual(self.stop_words_result, expected_result)


if __name__ == '__main__':
    unittest.main()