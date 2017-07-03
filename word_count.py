s = "Hi my name is Daniel and I love to jump over people with the name Daniel."

def word_count(s):
  s_list = s.lower().split()
  dict_string = {}
  for word in s_list:
    count = s_list.count(word)
    dict_string =count[word]
  return dict_string

  word_count(s)
