import os
import sqlite3

import word_lists

def is_reflexivo(word: str): # reflexivo (verbs with -se suffix) is independent of other rules, so it is best to deal with it at the beggining
    if word[-2:] == "se":
        return True, word[:-2] # just remove "-se"
    else:
        return False, word

def regular(word :str):
    all_forms = [word]
    reflexivo, word = is_reflexivo(word)
    core, sufix = word[:-2], word[-2:]
    sufixes = word_lists.sufixes_dict[sufix]
    for i in range(6): # 6 person
        # probably not the most optimal approach, but it is meant to be run once to set up database
        if reflexivo: # preapring appriopriate prefix followed by space if needed
            prefix = word_lists.se_prefixes[i] + " "
        else:
            prefix = ""

        all_forms.append(prefix + core + sufixes[i])

    return all_forms

def irregular(word, old, new): # word, old letter, new letter, e.g. cerrar, e, ie (e -> ie)
    all_forms = [word]
    reflexivo, word = is_reflexivo(word)
    core, sufix = word[:-2], word[-2:]
    sufixes = word_lists.sufixes_dict[sufix]
    # letter change occurs for all singular and 3rd person pluar
    # change for singular
    new_core = new.join(core.rsplit(old, 1))
    for i in range(3):
        if reflexivo:
            prefix = word_lists.se_prefixes[i] + " "
        else:
            prefix = ""

        all_forms.append(prefix + new_core + sufixes[i])

    for i in range(3, 5):
        if reflexivo:
            prefix = word_lists.se_prefixes[i] + " "
        else:
            prefix = ""

        all_forms.append(prefix + core + sufixes[i])

    if reflexivo:
            prefix = word_lists.se_prefixes[5] + " "
    else:
        prefix = ""

    all_forms.append(prefix + new_core + sufixes[5])

    return all_forms



def setup_db():
    try:
        os.remove("verbs.db")
        print("Database removed")
    except:
        print("No databse found")

    con = sqlite3.connect("verbs.db")
    print("New database created")

    con.execute("CREATE TABLE verbs(infinitivo TEXT PRIMARY KEY, yo TEXT, tu TEXT, el TEXT, nosotros TEXT, vosotros TEXT, ellos TEXT, level INT) WITHOUT ROWID")

    for word in word_lists.regular:
        all_forms = regular(word)
        con.execute("INSERT INTO verbs VALUES (?,?,?,?,?,?,?, 1)", all_forms)
        con.commit()

    first_person_list = word_lists.cer_suffix + word_lists.cir_suffix + word_lists.first_person_irregular

    for word in first_person_list:
        all_forms = regular(word)
        all_forms[1] = word_lists.first_person_dict[word]
        con.execute("INSERT INTO verbs VALUES (?,?,?,?,?,?,?, 2)", all_forms)
        con.commit()

    sets = [(word_lists.vacalicos_e_ie, "e", "ie"), (word_lists.vacalicos_e_i, "e", "i"), (word_lists.vacalicos_o_ue, "o", "ue"), (word_lists.vacalicos_u_ue, "u", "ue"), (word_lists.vacalicos_i_y, "i", "yi")]

    for _set in sets:
        for word in _set[0]:
            all_forms = irregular(word, _set[1], _set[2])
            con.execute("INSERT INTO verbs VALUES (?,?,?,?,?,?,?,3)", all_forms)
            con.commit()

    for word in word_lists.muy_irregulares:
        con.execute("INSERT INTO verbs VALUES (?,?,?,?,?,?,?,4)", word)
        con.commit()


if __name__ == "__main__":
    setup_db()
