#!/usr/bin/env python3

class MyString:
  def __init__(self, value=""):
    self.value = value
  @property
  def value(self):
    return self._value
  @value.setter
  def value(self, value):
    if isinstance(value, str):
      self._value = value
    else:
      print("The value must be a string.")
  def is_sentence(self):
    value_list = [letter for letter in self.value]
    if value_list[-1] == '.':
      return True
    else:
      return False
  def is_question(self):
    value_list = [letter for letter in self.value]
    if value_list[-1] == '?':
      return True
    else:
      return False
  def is_exclamation(self):
    value_list = [letter for letter in self.value]
    if value_list[-1] == '!':
      return True
    else:
      return False
  def count_sentences(self):
    sentence_endings = [".", "?", "!"]
    for ending in sentence_endings:
      self.value = self.value.replace(ending, ".")
    print(f"After replace: {self.value}")
    sentences = self.value.split(".")
    print(f"After split: {sentences}")
    valid_sentences = [sentence.strip() for sentence in sentences if sentence.strip()]
    print(f"Remove white spaces: {valid_sentences}")
    return len(valid_sentences)
  
string = MyString()
string.value = "This, well, is a sentence. This is too!! And so is this, I think? Woo..."
print(string.value)
print(string.count_sentences())