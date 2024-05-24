import unittest

def create_test_suite():
    loader = unittest.TestLoader()
    test_suite = loader.discover(start_dir='unit_testing', pattern='test*.py')
    return test_suite

def main():
    test_suite = create_test_suite()
    runner = unittest.TextTestRunner()
    result = runner.run(test_suite)
    return len(result.errors) + len(result.failures)

if __name__ == "__main__":
    exit_code = main()
    exit(exit_code)
