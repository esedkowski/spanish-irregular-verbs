import random
from termcolor import colored, cprint

    }
    return _dict

persons = create_dict("Yo", "Tú", "él/ella/usted", "nosotros/nosotras", "vosotros/vosotras", "ellos/ellas/ustedes")

se_prefixes = create_dict("me", "te", "se", "nos", "os", "se")

ar_sufixes = create_dict("o", "as", "a", "amos", "ais", "an")
er_sufixes = create_dict("o", "es", "e", "emos", "eis", "en")
ir_sufixes = create_dict("o", "es", "e", "imos", "is", "en")

sufixes = {
        "ar": ar_sufixes,
        "er": er_sufixes,
        "ir": ir_sufixes
}

for i in range(10):
    print("lesson", i)
    words = ["hablar", "comer", "vivir", "llamarse", "preguntar", "comprar", "amar", "terminar", "acabar", "escuchar", "completar", "bailar", "nadar", "beber", "leer", "correr", "romper", "subir", "escribir", "abir"]
    word = random.choice(words)
    print(word)

    prefix, core, sufix = "", word[:-2], word[-2:]

    person = random.choice(list(persons.keys()))

    if sufix == "se":
        prefix, core, sufix = se_prefixes[person] + " ", core[:-2], core[-2:]

    suf = sufixes[sufix]

    answer = input(persons[person]+" ")
    word = prefix+core+suf[person]
    if answer == word:
        cprint("correct", "green")
    else:
        cprint("wrong", "red")
        cprint(word, "yellow")"""
