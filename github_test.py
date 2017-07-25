print("Hello! What's your name and age?")

name = input("> ")
age = input("> ")

def hello_word(name, age):
    print("Nice to meet you {}, I'm also {} years old.".format(name, age))

hello_word(name, age)
