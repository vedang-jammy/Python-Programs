# this is the example to learn about functions in pyhon
def greet(lang):
    if lang == "jp":
        return "konichiva"
    elif lang == "mar":
        return "namaste"
    elif lang == "es":
        return "hola"
    else:
        return "hello"


lan = input("enter your language: ")
print(greet(lan), ", jack")
