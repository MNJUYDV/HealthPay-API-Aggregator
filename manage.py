import os
import sys

def setup_python_path():
    project_root = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(project_root)

def main():
    """Main entry point of the application."""
    # Set up Python path
    setup_python_path()

    import unittest
    loader = unittest.TestLoader()
    suite = loader.discover('tests')
    runner = unittest.TextTestRunner()
    result = runner.run(suite)

if __name__ == "__main__":
    main()

