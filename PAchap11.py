##names
#from name_function import get_formatted_name
#
#print("Enter 'q' at any time to quit.")
#while True:
#    first = input("\nPlease give me a first name: ")
#    if first == 'q':
#        break
#    last = input("Please give me a last name: ")
#    if last == 'q':
#        break
#    formatted_name = get_formatted_name(first, last)
#    print(f"\nNeatly formatted name: {formatted_name}")

#test_name_function
import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """Tests for 'name_function.py"""

    def test_first_last_name(self):
        """Do names like janis joplin work?"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

if __name__ == '__main__':
    unittest.main()