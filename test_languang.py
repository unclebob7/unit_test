from random import choice
from unittest import TestCase
from languange import languang_class

class TestLanguang(TestCase):
    def setUp(self):
        """
        setup(instanlize) object for global(static--Java) testing

        """
        question = "what is your favourite language for programming ?"
        self.tester = languang_class(question); #instanlize an object(tester) of language_class
        self.languages = ["python","java","php","css"]

    def test_store_language(self):
        self.tester.store_language(self.languages[0])
        self.assertIn(self.languages[0],self.tester.language)