""" A simple calculator module. """
from calc import add


def main():
    """Main function to test functions."""
    test_add()

def test_add():
    """Test the add function."""
    assert add(1.0, 2.0) == 3.0 , "Test failed: add(1.0, 2.0) did not return 3.0" 


if __name__ == "__main__":
    main()