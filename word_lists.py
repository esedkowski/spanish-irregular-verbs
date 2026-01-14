# list of verbs, can be moved to different file or DB if neccesary later

regular = ["hablar", "comer", "vivir", "preguntar", "comprar", "amar", "terminar", "acabar", "escuchar", "completar", "bailar", "nadar", "beber", "leer", "correr", "romper", "subir", "escribir", "abrir", "llamarse", "ponerse", "quitarse",  "probarse", "cambiarse"]

cer_suffix = ["conocer", "obedecer"] # in 1st person -cer -> -zco
cir_suffix = ["conducir", "traducir"] # in 1st person -cir -> -zco

first_person_irregular = ["estar", "dar", "hacer", "salir", "poner", "saber", "ver", "caer", "traer", "caber", "coger"] # does not include verbs wit -cer or -cir suffix. those are included in cer_suffix and cir suffix

# dictionary for all verbs which have irregular first person
first_person_dict = {
        "conocer": "conozco",
        "obedecer": "obedezco",
        "conducir": "conduzco",
        "traducir": "traduzco",
        "estar": "estoy",
        "dar": "doy",
        "hacer": "hago",
        "salir": "salgo",
        "poner": "pongo",
        "saber": "sé",
        "ver": "veo",
        "caer": "caigo",
        "traer": "traigo",
        "caber": "quepo", 
        "coger": "cojo"
}

# change in 1st, 2nd, 3rd person in singular and 3rd person in plural
vacalicos_e_ie = ["cerrar", "comenzar", "entender", "mentir", "pensar", "querer", "sentirse"] # e -> ie
vacalicos_e_i = ["pedir", "servir", "medir", "vestirse", "repetir"] # e -> i
vacalicos_o_ue = ["contar", "acostarse", "costar", "recordar", "poder", "volver", "dormir"]
vacalicos_u_ue = ["jugar"] # u -> ue
vacalicos_i_y = ["construir", "destruir", "huir", "obstruir", "fluir"] # y -> i, effective for all with -uir suffix

muy_irregulares = ["ser", "ir", "haber", "tener", "decir", "venir", "oir", "oler"] # no rules here

# reflextivos prefixes
se_prefixes = ["me", "te", "se", "nos", "os", "se"]

# regular sufixes
ar_sufixes = ["o", "as", "a", "amos", "áis", "an"]
er_sufixes = ["o", "es", "e", "emos", "éis", "en"]
ir_sufixes = ["o", "es", "e", "imos", "ís", "en"]

sufixes_dict = {
        "ar": ar_sufixes,
        "er": er_sufixes,
        "ir": ir_sufixes
}

muy_irregulares = [
    ["ser", "soy", "eres", "es", "somos", "sois", "son"],
    ["ir", "voy", "vas", "va", "vamos", "vais", "van"],
    ["haber", "he", "has", "ha/hay", "hemos", "habéis", "han"],
    ["tener", "tengo", "tienes", "tiene", "tenemos", "tenéis", "tienen"],
    ["decir", "digo", "dices", "dice", "decimos", "decís", "dicen"],
    ["venir", "vengo", "vienes", "viene", "venimos", "venís", "vienen"],
    ["oír", "oigo", "oyes", "oye", "oímos", "oís", "oyen"],
    ["oler", "huelo", "hueles", "huele", "olemos", "oléis", "huelen"],
    ["elegir", "elijo", "eliges", "elige", "elegimos", "elegís", "eligen"],
    ["seguir", "sigo", "sigues", "sigue", "seguimos", "seguís", "siguen"]
]

persons = ["Yo", "Tú", "él/ella/usted", "nosotros/nosotras", "vosotros/vosotras", "ellos/ellas/ustedes"]
