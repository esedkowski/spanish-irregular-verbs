import sqlite3
from word_lists import persons

con = sqlite3.connect("verbs.db")
cur = con.cursor()

for i in range(1, 5):
    level = i

    res = cur.execute(f"SELECT * FROM verbs WHERE level={level}")

    verbs = res.fetchall()
    with open(f"export_{level}.txt", "w") as f:
        for verb_set in verbs:
            verb = verb_set[0]
            line = verb + "; "
            for i in range(1,7):
                line += f"{persons[i-1]} {verb_set[i]}<br>"

            f.write(line + "\n")
