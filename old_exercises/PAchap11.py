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
#import unittest
#from name_function import get_formatted_name
#
#class NamesTestCase(unittest.TestCase):
#    """Tests for 'name_function.py"""
#
#    def test_first_last_name(self):
#        """Do names like janis joplin work?"""
#        formatted_name = get_formatted_name('janis', 'joplin')
#        self.assertEqual(formatted_name, 'Janis Joplin')
#
#if __name__ == '__main__':
#    unittest.main()

#test_survey
#import unittest
#from survey import AnonymousSurvey
#
#class TestAnonymousSurvey(unittest.TestCase):
#    """Tests for the class AnonymousSurvey"""
#
#    def test_store_single_response(self):
#    """Test that a single response is stored properly."""
#        question = "What language did you first learn to speak?"
#        my_survey = AnonymousSurvey(question)
#        my_survey.store_response('English')
#        self.assertIn('English', my_survey.responses)
#
#    def test_store_three_responses(self):
#        """Test that three individual responses are stored properly."""
#        question = "What language did you first learn to speak?"
#        my_survey = AnonymousSurvey(question)
#        responses = ['English', 'Spanish', 'Mandarin']
#        for response in responses:
#            my_survey.store_response(response)
#        for response in responses:
#            self.assertIn(response, my_survey.responses)
#
#if __name__ == '__main__':
#unittest.main()

#test survey with setUp method
import unittest
from survey_chap11 import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """Tests for Anonymous Survey"""

    def setUp(self):
        """
        Create a survey and a set of responses for use in all
        test methods
        """
        #question provided in setUp
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        #responses provided in setUp
        self.responses = ['English', 'French', 'Spanish']

    def test_store_single_response(self):
        """Test that a single response is store properly"""
#        question = "What language did you first learn to speak?"
#        my_survey = AnonymousSurvey(question)
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_three_response(self):
        """Test that three responses are stored properly"""
#        question = "What language did you first learn to speak?"
#        my_survey = AnonymousSurvey(question)
#        responses = ['English', 'French', 'Spanish']
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)

if __name__ == '__main__':
    unittest.main()