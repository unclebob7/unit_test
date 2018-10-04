class languang_class():

    def __init__(self,question,language = []):
        self.question = question
        self.language = language

    #changed
    def show_question(self):
        """
        >>> test = languang_class('hello',['python'])
        >>> test.show_question()
        question is hello
        """
        print(f'question is {self.question}')

    def store_language(self,new_language):
        self.language.append(new_language)

    def show_language(self):
        """display each element in language"""
        print("language in repo :\n");
        for element in self.language:
            print('-' +element)

