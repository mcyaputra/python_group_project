import unittest
import pandas as pd
import os

from unittest.mock import patch
from io import StringIO
from core.visualization import load_data, plot_sentiment_vs_author, plot_sentiment_vs_title, plot_publish_date_vs_author, plot_publish_date_vs_title

class TestVisualizationModule(unittest.TestCase):

    def setUp(self):
        
        # Setting up a sample DataFrame for testing
        self.sample_data = StringIO(
            """author,title,sentiment,publish_date
            Author1,Title1,0.5,2023-05-01
            Author2,Title2,0.7,2023-05-02
            Author3,Title3,-0.1,2023-05-03"""
        )
        self.df = pd.read_csv(self.sample_data)

    def test_load_data_success(self):
        
        """
        Testing loading data from a CSV file successfully.
        """
        # Creating a temporary CSV file for testing load_data function
        temp_csv = 'temp_test_data.csv'
        self.df.to_csv(temp_csv, index=False)
        
        # Testing loading data
        loaded_df = load_data(temp_csv)
        pd.testing.assert_frame_equal(loaded_df, self.df)
        
        # Cleaning up
        os.remove(temp_csv)

    @patch('builtins.print')  # Suppressing print statements
    def test_load_data_file_not_found(self, mock_print):
        
        """
        Test handling for FileNotFoundError if the file does not exist.
        """
        with self.assertRaises(FileNotFoundError):
            load_data('non_existent_file.csv')

    @patch('matplotlib.pyplot.show')
    def test_plot_sentiment_vs_author(self, mock_show):
        
        """
        Test the plot_sentiment_vs_author function that ensures it runs without errors.
        """
        try:
            plot_sentiment_vs_author(self.df)
        except Exception as e:
            self.fail(f"plot_sentiment_vs_author raised an exception: {e}")

    @patch('matplotlib.pyplot.show')
    def test_plot_sentiment_vs_title(self, mock_show):
        
        """
        Test the plot_sentiment_vs_title function that ensures it runs without any errors.
        """
        try:
            plot_sentiment_vs_title(self.df)
        except Exception as e:
            self.fail(f"plot_sentiment_vs_title raised an exception: {e}")

    @patch('matplotlib.pyplot.show')
    def test_plot_publish_date_vs_author(self, mock_show):
        
        """
        Test the plot_publish_date_vs_author function that ensures it runs without any errors.
        """
        try:
            plot_publish_date_vs_author(self.df)
        except Exception as e:
            self.fail(f"plot_publish_date_vs_author raised an exception: {e}")

    @patch('matplotlib.pyplot.show')
    def test_plot_publish_date_vs_title(self, mock_show):
        
        """
        Test the plot_publish_date_vs_title function that ensures it runs without any errors.
        """
        try:
            plot_publish_date_vs_title(self.df)
        except Exception as e:
            self.fail(f"plot_publish_date_vs_title raised an exception: {e}")

if __name__ == '__main__':
    unittest.main()