#!/usr/bin/env python3
import re
# In Python, the re module is a standard library module, so you don't need to import it from an external source. It should be available by default.
class MyString:
    def __init__(self, value=""):
        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if not isinstance(new_value, str):
            print("The value must be a string.")
        else:
            self._value = new_value
    
    def is_sentence(self):
        return self._value.endswith(".")
    
    def is_question(self):
        return self._value.endswith("?")
    
    def is_exclamation(self):
        return self._value.endswith("!")
    
        
    def count_sentences(self):
        # Split the value into sentences based on common punctuation.
        sentences = re.split(r'[.!?]', self.value)
        # Filter out empty strings from the split result.
        sentences = [s.strip() for s in sentences if s.strip()]
        # Print the number of sentences.
        print(f"Number of sentences: {len(sentences)}")
        return len(sentences)
        
        
        
      
