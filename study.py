from random import choice, randint
import sqlite3

RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
RESET = "\033[0m"

con = sqlite3.connect("verbs.db")
cur = con.cursor()

res = cur.execute("SELECT name FROM pragma_table_info('verbs')")
col_names = [name for (name,) in res.fetchall()]
col_names.remove("infinitivo")
col_names.remove("level")

max_level = 0
while max_level < 1 or max_level > 4:
    max_level = int(input("level: "))

res = cur.execute(f"SELECT infinitivo FROM verbs WHERE level < {max_level + 1}")
verbs = [verb for (verb,) in res.fetchall()]

end = False
while end == False:
    person = choice(col_names)
    verb = choice(verbs)

    res = cur.execute(f"SELECT {person} FROM verbs WHERE infinitivo='{verb}'")
    correct = res.fetchone()[0]
    answer = input(f"{person} {verb}: ")
    if answer == "q":
        end = True
    elif answer == correct:
        print(f"{GREEN}CORRECT!{RESET}")
    else:
        print(f"{RED}WRONG!{RESET}")
        print(f"{YELLOW}{correct}{RESET}")

